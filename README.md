# 🗺️ Gerador Automático de TopoJSON  
### **Conversão direta da malha municipal do IBGE para uso em mapas do Power BI**

> ⚠️ **Aviso importante:** Um **front-end está em desenvolvimento** para oferecer uma experiência totalmente visual, simples e rápida ao usuário.  
> Em breve será possível gerar mapas TopoJSON **com 1 clique**, sem precisar utilizar código.

---

## 📌 Sobre o projeto
Este projeto automatiza a geração de arquivos **TopoJSON** utilizando as malhas municipais oficiais do **IBGE**, tornando o processo extremamente simples para quem trabalha com:

- Power BI (Shape Map / Map visuals)  
- Dashboards geográficos  
- Análise e visualização territorial  

O sistema baixa os dados diretamente do site do IBGE, filtra pelo estado desejado, organiza o dataset e exporta um TopoJSON limpo e compatível.

---

## 🚀 Funcionalidades principais

✔️ Download direto do ZIP do IBGE  
✔️ CRS ajustado para **EPSG:4326** (necessário no Power BI)  
✔️ Normalização dos campos `name` e `codigo`  
✔️ Exportação automática para TopoJSON  
✔️ Pré-visualização do mapa dentro do próprio aplicativo (em desenvolvimento)  
✔️ Arquivo leve, limpo e pronto para uso  

---

## 🧩 Como funciona (visão geral)

1. O script acessa a URL oficial da malha municipal do IBGE  
2. Filtra apenas o estado escolhido (UF)  
3. Normaliza e organiza os campos necessários ao Power BI  
4. Converte o shapefile original em **TopoJSON**  
5. Salva automaticamente no diretório configurado  
6. (Em breve) Permite pré-visualização e geração via front-end sem código

---

## 🔧 Requisitos técnicos

- Python 3.10+  
- geopandas  
- topojson  
- fiona  
- shapely  
- pyproj  

Instalação recomendada (Windows):

```bash
pip install geopandas topojson fiona shapely pyproj
```

---

## 💻 Front-end (em desenvolvimento)
O front-end é construído em **CustomTkinter** e permitirá:

- Seleção de estado para gerar o TopoJSON municipal  
- Pré-visualização do mapa dentro do aplicativo  
- Geração do TopoJSON com **1 clique**, sem precisar abrir o script  

> 🔜 Em breve, a interface ficará totalmente funcional para facilitar o uso a qualquer usuário, mesmo sem conhecimento técnico.

---

## 🗂️ Estrutura do projeto

```
/projeto-topojson
│
├─ back.py                # Funções para download, geração de TopoJSON e pré-visualização
├─ front_mapa.py          # Interface gráfica em CustomTkinter
├─ mapas_powerbi/         # Diretório onde os TopoJSON são salvos
└─ README.md              # Este arquivo
```

---

## 📥 Download de dados oficiais
As malhas municipais são baixadas diretamente do IBGE:

- Municípios 2022: [BR_Municipios_2022.zip](https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2022/Brasil/BR/BR_Municipios_2022.zip)  

> Todos os dados são obtidos dinamicamente pelo script, sem necessidade de download manual.

---

## ⚡ Como usar

1. Abra o **front_mapa.py** com Python 3.10+  
2. Selecione o **estado desejado**  
3. Clique em **Visualizar** para ver o mapa  
4. Clique em **Gerar TopoJSON** para salvar o arquivo pronto para uso no Power BI

---

## 📄 Licença

Este projeto é open-source e pode ser utilizado livremente em projetos pessoais ou comerciais.
