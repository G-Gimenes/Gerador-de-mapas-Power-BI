import geopandas as gpd
from topojson import Topology

url = 'https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/Brasil/BR/BR_Municipios_2022.zip'
gdf = gpd.read_file(url)

gdf_ro = gdf[gdf['SIGLA_UF'] == 'MT']


gdf_ro = gdf_ro[['NM_MUN', 'CD_MUN', 'geometry']]

gdf_ro = gdf_ro.rename(columns={
    'NM_MUN': 'name',      
    'CD_MUN': 'codigo'     
})

topology = Topology(gdf_ro, object_name="municipios_ro", prequantize=False)

output_path = r"C:\Users\gustavo.moura\Pictures\mapas_powerbi\Mato_Grosso_Municipios.json"
topology.to_json(output_path)

print("✔ TopoJSON criado com sucesso!")
print("Arquivo salvo em:", output_path)