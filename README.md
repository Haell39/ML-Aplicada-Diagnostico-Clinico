# 💻 Projeto de Machine Learning Aplicado a Dados de Diagnóstico Médico 🔬

Este repositório contém um estudo abrangente de Machine Learning aplicado a um dataset de diagnóstico médico. O objetivo é explorar os dados, construir e otimizar modelos de classificação para prever diagnósticos, e realizar agrupamento para descobrir padrões latentes nos dados.

## 📊 Tópicos Abordados:

-   **Análise Exploratória de Dados (EDA)**:
    -   Visualizações de distribuições de características e relações entre variáveis.
    -   Análise da distribuição da variável alvo (diagnóstico Benigno/Maligno).
    -   Mapa de calor de correlações.

-   **Modelagem de Classificação Supervisionada**:
    -   **K-Nearest Neighbors (KNN)**: Implementação e otimização para a melhor acurácia.
    -   **Árvore de Decisão**: Construção e ajuste de hiperparâmetros para alta precisão.
    -   **Redes Neurais (MLPClassifier - Scikit-learn)**: Treinamento e otimização de modelos de redes neurais simples.

-   **Agrupamento Não Supervisionado (Clustering)**:
    -   **K-Means**: Aplicação para identificar grupos naturais nos dados e análise da sua correlação com os diagnósticos reais.

-   **Download de Dados Programático**:
    -   Código para baixar automaticamente o dataset do Kaggle usando a API.

## 📁 Dataset

O projeto utiliza o dataset **Breast Cancer Wisconsin (Diagnostic) Data**, uma base de dados popular obtida do Kaggle. Este dataset contém características computadas a partir de imagens digitalizadas de biópsias de massa mamária, usadas para predizer se um tumor é benigno ou maligno.

## 🛠️ Tecnologias e Ferramentas

-   **Python**
-   **Pandas**: Manipulação e análise de dados.
-   **NumPy**: Operações numéricas.
-   **Scikit-learn**: Implementação dos algoritmos de Machine Learning (Classificação, Agrupamento, Pré-processamento).
-   **Matplotlib** e **Seaborn**: Criação de gráficos e visualização de dados.
-   **Kaggle API**: Para o download programático do dataset.

## ✨ Como Rodar o Projeto

1.  **Clone o Repositório:**

    ```bash
    git clone https://github.com/Haell39/ML-Aplicada-Diagnostico-Clinico
    cd ML-Aplicada-Diagnostico-Clinico
    ```
    
2.  **Instale as Dependências:**
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn kaggle
    ```
3.  **Configure a API do Kaggle:**
    Siga as instruções para criar um token da API do Kaggle (`kaggle.json`) e coloque-o no diretório `~/.kaggle/` (ou `C:\Users\<Seu_Usuario>\.kaggle\` no Windows).
4.  **Execute o Notebook Jupyter:**
    Abra o arquivo `.ipynb` em um ambiente Jupyter (Jupyter Lab, Jupyter Notebook, ou VS Code com extensão Python) e execute as células em sequência.
    
