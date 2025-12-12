# back.py
import geopandas as gpd
from topojson import Topology
import os
import matplotlib.pyplot as plt
import requests
import io
from zipfile import ZipFile
import tempfile

# URL shapefile IBGE para municípios
URL_MUNICIPIOS = "https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/Brasil/BR/BR_Municipios_2022.zip"

def baixar_gdf(url):
    """Baixa shapefile do IBGE e retorna GeoDataFrame"""
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError(f"Erro ao baixar shapefile: HTTP {r.status_code}")

    # Salva ZIP em arquivo temporário
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "mapa.zip")
        with open(zip_path, "wb") as f:
            f.write(r.content)

        # Encontra o arquivo .shp dentro do ZIP
        with ZipFile(zip_path) as z:
            shapefile_path = [f for f in z.namelist() if f.endswith(".shp")]
            if not shapefile_path:
                raise ValueError("Shapefile não encontrado no ZIP")
            shapefile_name = shapefile_path[0]

            # Extrai shapefile e arquivos relacionados
            z.extractall(tmpdir)

        # Caminho completo do shapefile extraído
        shp_full_path = os.path.join(tmpdir, shapefile_name)
        gdf = gpd.read_file(shp_full_path)

    return gdf

def gerar_topojson(tipo, estado_selecionado=None):
    """
    Gera TopoJSON para o município selecionado:
    - tipo: deve ser "Municipal"
    - estado_selecionado: obrigatório
    """
    if tipo != "Municipal":
        raise ValueError("Apenas tipo 'Municipal' é permitido.")

    if not estado_selecionado:
        raise ValueError("Selecione um estado para gerar o mapa municipal.")

    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    pasta_saida = os.path.join(pasta_atual, "mapas_powerbi")
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
    """
    Retorna uma figura matplotlib para pré-visualização do município:
    - tipo: deve ser "Municipal"
    - estado_selecionado: obrigatório
    """
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