# Next Data
<p align="center">
    
![Imagem do projeto](C:\Users\joaop\challenge-fiap\docs\assets\img\nextdata.jpg)

Com tantos produtos parecidos no e-commerce, fica cada vez mais difícil para o consumidor escolher o que comprar, e para os comerciantes, é um desafio se destacar. Pensando nisso, criamos o NextData, um sistema de recomendação que usa dados de pedidos, entregas, avaliações e vendas para ajudar os consumidores a encontrarem o produto ideal de forma mais fácil e rápida, ao mesmo tempo em que dá mais visibilidade aos lojistas.

# Justificativa
No cenário atual do e-commerce, a grande variedade de produtos semelhantes e com boas avaliações cria uma sobrecarga cognitiva para os consumidores, dificultando a escolha do produto ideal. Isso afeta tanto os consumidores, que ficam indecisos, quanto os lojistas, que têm dificuldades em destacar seus produtos entre tantas opções. Esse problema pode reduzir a taxa de conversão, a fidelização de clientes e as vendas no geral.

No NextData, a proposta é utilizar dados de pedidos, entregas, avaliações de clientes e histórico de vendas para criar um sistema de recomendação inteligente, que ajude a priorizar e recomendar os produtos mais relevantes para os consumidores. O objetivo é entender as relações entre os dados, como quais produtos são mais vendidos, quais canais de venda geram mais transações, e como o tempo de entrega impacta as avaliações.

**Com essa abordagem, buscamos responder a questões como**:

1. Quais produtos têm mais chances de serem comprados juntos?
2. Quais categorias ou lojas estão dominando as vendas no marketplace?
3. O tempo de entrega influencia a satisfação do cliente e suas avaliações?
4. Quais canais de venda geram mais transações e como isso pode influenciar as recomendações?

Com essas análises, queremos oferecer uma solução que melhore a experiência de compra, aumente a taxa de conversão e ajude os lojistas a se destacarem no marketplace. Além disso, o sistema de recomendação será mais intuitivo e personalizado, promovendo uma experiência mais eficiente para os consumidores e ajudando os lojistas a alcançarem melhores resultados.

## Metodologia

O projeto será desenvolvido utilizando a metodologia CRISP-DM, seguindo os seguintes passos:

1. Entendimento de negócio
2. Entendimento de dados
3. Preparação dos dados
4. Modelagem

O projeto também é dividido em entregas, a saber:

1. **Criação do Banco de Dados**: Estruturar o banco de dados necessário para armazenar e gerenciar os dados de pedidos, entregas, avaliações, e histórico de vendas.
2. **Análise Exploratória de Dados (EDA)**: Entender profundamente as variáveis que impactam o desempenho do sistema de recomendação e identificação de padrões nos dados através de hipóteses, visualizações e insights.
3. **Análise comparativa de modelos**: Avaliar diferentes modelos de aprendizado de máquina para prever o consumo e classificar os produtos com base nos dados analisados.
4. **Dashboard Interativo**: Desenvolver uma interface interativa para visualizar os resultados do sistema de recomendação de produtos e permitir a interação com os dados.

# Resultados
Em síntese, a proposta de um sistema de recomendação visa otimizar a experiência de compra, tornando-a mais personalizada e eficiente. Focando em aspectos como preço, popularidade, avaliações e histórico de compras, a solução ajudará os consumidores a escolherem produtos de forma mais rápida e assertiva. Isso não só melhora a experiência do usuário, mas também oferece uma vantagem competitiva para a plataforma, ao atender melhor às necessidades do cliente e aumentar as vendas.

## Desenvolvedores
 - [João Paulo Ferreira](https://github.com/joao-paulo-alt)
 - [Caio Guimaraes](https://github.com/caioguimaraes18)


### Organização de diretórios


```
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

```
