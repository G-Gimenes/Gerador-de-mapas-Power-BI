
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
✔️ Arquivo leve, limpo e pronto para uso  

---

## 🧩 Como funciona (visão geral)

1. O script acessa a URL oficial da malha municipal do IBGE  
2. Filtra apenas o estado escolhido (UF)  
3. Normaliza e organiza os campos necessários ao Power BI  
4. Converte o shapefile original em **TopoJSON**  
5. Salva automaticamente no diretório configurado  

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
conda install -c conda-forge geopandas fiona shapely pyproj
pip install topojson
```

---

## 🛠️ Como usar no Power BI

1. Abra o **Power BI Desktop**  
2. Insira o visual **Shape Map**  
3. Vá em **Formatar → Shape → Add Map**  
4. Importe o TopoJSON gerado  
5. Relacione sua tabela com:
   - **codigo** (recomendado)  
   - ou **name** (quando idêntico ao IBGE)

Seu mapa está pronto!

---

## 📦 Estrutura do TopoJSON Gerado

| Campo      | Descrição |
|------------|-----------|
| **name**   | Nome do município (padrão IBGE) |
| **codigo** | Código IBGE normalizado (6 dígitos) |
| **geometry** | Geometria otimizada para o Power BI |

---

## 🧪 Status do projeto

| Item | Status |
|------|--------|
| Automação Python | ✔ Concluído |
| Compatibilidade Power BI | ✔ Validado |
| Geração por UF | ✔ 100% operacional |
| **Front-end** | 🔄 Em desenvolvimento |

> O front-end permitirá escolher a UF, visualizar os polígonos e gerar o TopoJSON sem nenhuma necessidade de código.

---

## 📣 Melhorias planejadas

- Pré-visualização dos polígonos antes da exportação  
- Ajuste do nível de simplificação geométrica  
- Exportação em múltiplos formatos (TopoJSON + GeoJSON)  
- Geração de mapas regionais completos  
