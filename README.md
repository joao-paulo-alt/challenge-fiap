# Next Data
![Imagem do projeto](docs/assets/img/nextdata.jpg)


## 📌 Visão Geral

Este projeto foi desenvolvido para enfrentar desafios críticos no setor de **e-commerce e logística de entregas**, utilizando **ciência de dados** e **machine learning**. O objetivo principal é **otimizar operações**, **reduzir custos** e **aumentar a satisfação do cliente** por meio de decisões orientadas por dados.

---

## 🎯 Objetivos

✅ Prever **taxas de cancelamento** e identificar entregas com risco de falha  
✅ Otimizar **modalidades de entrega** com base em custo/distância  
✅ Estimar **distâncias de entrega** para planejamento mais eficiente  
✅ Identificar **gargalos operacionais** na jornada do pedido  
✅ Melhorar a **experiência do cliente** com insights acionáveis  

---

## 🔍 Justificativa

O crescimento do e-commerce trouxe uma série de desafios:

1. 📂 **Fragmentação de informações**: dados dispersos dificultam a visão unificada  
2. 🔮 **Falta de previsibilidade**: cancelamentos e atrasos não são previstos  
3. 🛑 **Ineficiência operacional**: processos custosos e desorganizados  
4. 😡 **Insatisfação do cliente**: falhas logísticas afetam fidelização  

Este projeto busca resolver esses problemas por meio de:

- 📉 **Redução de custos logísticos**  
- 📈 **Aumento na taxa de sucesso das entregas**  
- 📊 **Melhor tomada de decisão baseada em dados**  
- ⏱️ **Antecipação de problemas operacionais**

---

## 📊 Metodologia

### 🔹 Etapa 1 — Definição do Problema (Design Thinking)
- Análise SWOT
- Personas e jornadas
- Mapeamento de pontos críticos

### 🔹 Etapa 2 — Coleta & Preparação de Dados
- **Fontes**: 7 datasets do Kaggle
- **ETL Customizado**:
  - Extração de CSVs
  - Limpeza (nulos, outliers, duplicatas)
  - Transformação e padronização
  - Carga no SQLite
- **EDA** (Análise Exploratória):
  - Estatísticas, distribuições, correlações

### 🔹 Etapa 3 — Modelagem Preditiva

**🔸 a) Classificação (Sucesso/Falha na Entrega)**  
- Algoritmo: Regressão Logística  
- Acurácia: **100%** ⚠️ (possível overfitting)  

**🔸 b) Modalidade (Motoboy/Biker)**  
- Algoritmo: Árvore de Decisão  
- Acurácia: **93%**, F1-Score: Motoboy (0.95), Biker (0.87)  

**🔸 c) Regressão (Distância de Entrega)**  
- Algoritmo: Random Forest  
- MAE: **1.317m**, R²: **0.34**

### 🔹 Etapa 4 — Validação
- Interpretação de coeficientes
- Análise de viéses

### 🔹 Etapa 5 — Visualização & Dashboard
- Painéis em **Power BI** com:
  - KPIs logísticos
  - Mapas de calor
  - Análise temporal
  - Recomendações inteligentes

### 🔹 Etapa 6 — Documentação & Versionamento
- Código modular e comentado
- Estrutura clara no GitHub
- README completo 📘
- Dicionário de dados incluído

---

## 🛠️ Tecnologias Utilizadas

| Categoria            | Ferramentas / Tecnologias                          |
|----------------------|----------------------------------------------------|
| 🐍 Linguagem         | Python                                             |
| 📚 Bibliotecas       | Pandas, Scikit-learn, Matplotlib, Seaborn         |
| 🗃️ Banco de Dados   | SQLite (design pronto para PostgreSQL/MySQL)      |
| 📈 Visualização      | Power BI                                           |
| 🗂️ Versionamento     | GitHub                                             |
| ⚙️ Processamento     | ETL customizado em Python                          |

---

## 📂 Estrutura do Repositório
.
├── data/              # Diretório contendo todos os arquivos de dados
│   ├── external/      # Arquivos de dados de fontes externas
│   ├── interim/       # Arquivos de dados intermediários
│   ├── processed/     # Arquivos de dados processados
│   └── raw/           # Arquivos de dados originais, imutáveis
├── docs/              # Documentação gerada através da biblioteca mkdocs
├── models/            # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/         # Diretório contendo todos os notebooks utilizados nos passos
├── references/        # Dicionários de dados, manuais e todo o material exploratório
├── src/               # Código fonte utilizado nesse projeto
│   ├── data/          # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/    # Classes e funções utilizadas para implantação do modelo
│   └── model/         # Classes e funções utilizadas para modelagem
├── app.py             # Arquivo com o código da aplicação do streamlit
├── Procfile           # Arquivo de configuração do heroku
├── pyproject.toml     # Arquivo de dependências para reprodução do projeto
├── poetry.lock        # Arquivo com sub-dependências do projeto principal
├── README.md          # Informações gerais do projeto
└── tasks.py           # Arquivo com funções para criação de tarefas utilizadas pelo invoke


---

## 🚀 Como Executar

### 🔧 Pré-requisitos
- Python 3.8+
- Bibliotecas listadas em `requirements.txt`

### 📦 Instalação
```bash
git clone https://github.com/seu-usuario/repositorio.git
cd repositorio
pip install -r requirements.txt
```

### ▶️ Execução

**Pipeline ETL**  
```bash
python src/etl/main.py
```

**Modelos de Machine Learning**  
```bash
python src/models/train.py
```

---

## 📈 Sobre os Dados

Conjuntos obtidos no [Kaggle](https://www.kaggle.com/datasets/...) com informações sobre:

- 🛒 Canais de venda  
- 🚚 Entregas e entregadores  
- 🏢 Hubs logísticos  
- 📦 Pedidos e pagamentos  
- 🏪 Lojas parceiras  

---

## 🤝 Contribuições

Contribuições são muito bem-vindas!  
Siga os passos abaixo:

1. Faça um fork ✨  
2. Crie uma branch: `git checkout -b feature/sua-feature`  
3. Commit: `git commit -m 'Nova feature'`  
4. Push: `git push origin feature/sua-feature`  
5. Crie um Pull Request 🚀

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.  
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✉️ Contato

| Nome     | [João Paulo Ferreira](https://github.com/joao-paulo-alt) |
|----------|---------------------------------------------|
| Email    | joaopauloferreirag173@gmail.com                     |

| Nome     | [Caio Guimarães](https://github.com/caioguimaraes18) |
|----------|---------------------------------------------|
| Email    | contatocaioguimaraess@gmail.com                     |


---

> **Nota**: Projeto desenvolvido como parte do projeto CHALLENGE da _FIAP_.  
Agradecimentos especiais aos mentores e colegas pela colaboração!
```