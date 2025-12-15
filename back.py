import geopandas as gpd
from topojson import Topology
import os
import matplotlib.pyplot as plt
import requests
from zipfile import ZipFile
import tempfile
import winreg

# URL shapefile IBGE para municípios
URL_MUNICIPIOS = "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/Brasil/BR/BR_Municipios_2022.zip"

# ---------------- Registro do Windows ----------------
DEFAULT_DIR = os.path.join(os.path.expanduser("~"), "Documents", "maps")
REG_PATH = r"Software\FormatMapGenerator"

def get_output_dir():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        value, _ = winreg.QueryValueEx(reg_key, "OutputDir")
        winreg.CloseKey(reg_key)
        return value
    except FileNotFoundError:
        return DEFAULT_DIR

def set_output_dir(path):
    reg_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
    winreg.SetValueEx(reg_key, "OutputDir", 0, winreg.REG_SZ, path)
    winreg.CloseKey(reg_key)
# -----------------------------------------------------

def baixar_gdf(url):
    """Baixa shapefile do IBGE e retorna GeoDataFrame"""
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError(f"Erro ao baixar shapefile: HTTP {r.status_code}")

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "mapa.zip")
        with open(zip_path, "wb") as f:
            f.write(r.content)

        with ZipFile(zip_path) as z:
            shapefile_path = [f for f in z.namelist() if f.endswith(".shp")]
            if not shapefile_path:
                raise ValueError("Shapefile não encontrado no ZIP")
            shapefile_name = shapefile_path[0]
            z.extractall(tmpdir)

        shp_full_path = os.path.join(tmpdir, shapefile_name)
        gdf = gpd.read_file(shp_full_path)

    return gdf

def gerar_topojson(tipo, estado_selecionado=None, pasta_saida=None):
    if tipo != "Municipal":
        raise ValueError("Apenas tipo 'Municipal' é permitido.")
    if not estado_selecionado:
        raise ValueError("Selecione um estado para gerar o mapa municipal.")

    # Se não passar pasta_saida, usa o valor do registro
    if not pasta_saida:
        pasta_saida = get_output_dir()

    os.makedirs(pasta_saida, exist_ok=True)

    gdf = baixar_gdf(URL_MUNICIPIOS)
    gdf = gdf[gdf['SIGLA_UF'] == estado_selecionado]
    gdf = gdf[['NM_MUN', 'CD_MUN', 'geometry']].rename(columns={'NM_MUN':'name','CD_MUN':'codigo'})

    object_name = f"municipios_{estado_selecionado.lower()}"
    output_path = os.path.join(pasta_saida, f"{estado_selecionado}_municipios.json")

    topology = Topology(gdf, object_name=object_name, prequantize=False)
    topology.to_json(output_path)

    return output_path

def gerar_preview(tipo, estado_selecionado=None):
    if tipo != "Municipal":
        raise ValueError("Apenas tipo 'Municipal' é permitido.")
    if not estado_selecionado:
        raise ValueError("Selecione um estado para pré-visualização.")

    gdf = baixar_gdf(URL_MUNICIPIOS)
    gdf = gdf[gdf['SIGLA_UF'] == estado_selecionado]

    fig, ax = plt.subplots(figsize=(10,7), dpi=100)
    ax.set_facecolor('#C8C6C4')
    gdf.plot(ax=ax, facecolor='#C8C6C4', edgecolor='#605E5C', linewidth=1)
    ax.axis('off')
    return fig