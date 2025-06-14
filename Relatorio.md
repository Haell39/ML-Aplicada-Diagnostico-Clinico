### **Relatório de Projeto: Análise e Modelagem de Dados de Diagnóstico de Câncer de Mama**

 O projeto teve como objetivo principal a compreensão do conjunto de dados e o desenvolvimento de modelos preditivos para auxiliar no diagnóstico.

#### **1. Análise Exploratória de Dados (EDA)**

* **Composição do Dataset**: O conjunto de dados contém 569 amostras e 33 colunas. A coluna `id` foi identificada como um identificador único e `Unnamed: 32` como uma coluna vazia, ambas descartadas para a análise.
* **Distribuição dos Diagnósticos**: A proporção de casos no dataset é de **62.74% Benignos (B)** e **37.26% Malignos (M)**. Essa leve assimetria foi considerada na avaliação dos modelos através do uso de estratificação na divisão dos dados.
* **Características Chave**: A análise dos histogramas e box plots revelou que características como `radius_mean`, `perimeter_mean`, e `area_mean` (e suas variantes `worst` e `se`) mostram distribuições visivelmente diferentes entre os diagnósticos Benigno e Maligno. Tumores malignos tendem a apresentar valores maiores nessas métricas.
* **Correlações**: O mapa de calor de correlação indicou uma alta correlação positiva entre muitas das características de "mean", "se" e "worst" (ex: `radius_mean` e `perimeter_mean` são fortemente correlacionadas). Isso sugere que estas características medem aspectos semelhantes da massa do tumor.

#### **2. Modelagem de Classificação Supervisionada**

Três modelos de classificação foram aplicados e otimizados para prever o diagnóstico (`B` ou `M`), após pré-processamento com escalonamento das features e codificação da variável alvo.

* **K-Nearest Neighbors (KNN)**:
    * **Achado**: O KNN demonstrou uma excelente performance, com o melhor `k` encontrado sendo **5**.
    * **Resultado**: A acurácia final no conjunto de teste foi de **0.9649 (96.49%)**. Isso indica que o modelo é altamente capaz de classificar corretamente os diagnósticos.

* **Árvore de Decisão**:
    * **Achado**: Otimização via `GridSearchCV` identificou que uma profundidade máxima sem restrição (`max_depth: None`) com `min_samples_leaf: 2` e `min_samples_split: 10` apresentou o melhor desempenho.
    * **Resultado**: A acurácia final no conjunto de teste foi de **0.9298 (92.98%)**. O relatório de classificação mostrou alta precisão e recall para ambas as classes, com um F1-score de 0.95 para 'B' e 0.90 para 'M'.
    * **Diferença na Probabilidade**: Observou-se que a Árvore de Decisão pode gerar probabilidades "duras" (ex: `[0. 1.]`), indicando 100% de certeza, quando a decisão é clara.

* **Rede Neural (MLPClassifier)**:
    * **Achado**: O modelo de Rede Neural alcançou a maior acurácia entre os classificadores testados. Os melhores hiperparâmetros foram `activation: 'relu'`, `alpha: 0.0001`, `hidden_layer_sizes: (100, 50)` e `solver: 'adam'`.
    * **Resultado**: A acurácia final no conjunto de teste foi impressionante: **0.9708 (97.08%)**. O relatório de classificação mostrou resultados quase perfeitos, especialmente para a classe 'B' (1.00 de recall).
    * **Notação Científica nas Probabilidades**: As probabilidades de previsão são exibidas em notação científica (ex: `[6.49725797e-04 9.99350274e-01]`), o que é comum em Redes Neurais e representa valores muito próximos de 0 ou 1, mas raramente exatos.

#### **3. Agrupamento Não Supervisionado (K-Means)**

* **Determinação do K**: O Método do Cotovelo (Elbow Method) sugeriu `k=2` como um número ideal de clusters, o que alinha-se perfeitamente com os dois diagnósticos (Benigno e Maligno) existentes no dataset.
* **Achado Principal**: A análise da distribuição do diagnóstico original dentro dos clusters revelou uma **alta correlação** entre os clusters formados pelo K-Means e os diagnósticos reais.
    * **Cluster 0**: Contém majoritariamente casos **Benignos** (339 B vs 36 M).
    * **Cluster 1**: Contém majoritariamente casos **Malignos** (18 B vs 176 M).
* **Visualização**: A projeção dos clusters e dos diagnósticos reais em componentes principais (PCA) demonstrou visualmente essa forte semelhança, indicando que o K-Means conseguiu agrupar as amostras de forma a refletir a distinção biológica do diagnóstico. Os centróides dos clusters (no espaço escalado) também mostraram padrões de características consistentes com as médias dos grupos benignos e malignos.

#### **Conclusão Geral**

O projeto demonstrou que as características do dataset de câncer de mama são altamente discriminativas. Os modelos de Machine Learning aplicados, especialmente a Rede Neural e o KNN, alcançaram **altíssima acurácia na classificação de diagnósticos**, sugerindo um grande potencial para auxiliar na triagem e no diagnóstico. Além disso, o agrupamento K-Means revelou a existência de **estruturas naturais nos dados que correspondem de perto aos diagnósticos clínicos**, reforçando a validade das características para o problema em questão.