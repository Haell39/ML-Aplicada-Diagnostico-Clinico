import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("--- Gerando Visualização de Separação de Diagnóstico ---")
print("\n1. Carregando o dataset...")

dataset_path = '../data/Breast_Cancer.csv'
if not os.path.exists(dataset_path):
    print(f"Erro: O arquivo '{dataset_path}' não foi encontrado.")
    print("Certifique-se de ter baixado o dataset usando o script do Kaggle na pasta 'data'.")
    exit()

df = pd.read_csv(dataset_path)
df = df.drop(columns=['id', 'Unnamed: 32'])

print("   Dataset carregado e colunas desnecessárias removidas.")
print("\n2. Criando gráfico de dispersão de características por diagnóstico...")

sns.set_style("whitegrid")
plt.figure(figsize=(10, 7))

feature_x = 'radius_mean'
feature_y = 'texture_worst'

sns.scatterplot(x=feature_x, y=feature_y, hue='diagnosis', data=df,
                palette={'M': 'red', 'B': 'green'},
                s=80, alpha=0.7)

plt.title(f'Dispersão de {feature_x.replace("_", " ").title()} vs {feature_y.replace("_", " ").title()} por Diagnóstico')
plt.xlabel(feature_x.replace('_', ' ').title())
plt.ylabel(feature_y.replace('_', ' ').title())
plt.legend(title='Diagnóstico')
plt.grid(True)

output_directory = '../Images' #vale lembrar que é fora da pasta Scripts, por isso o '../'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

output_filename = os.path.join(output_directory, 'dispersao_diagnostico.png')
plt.savefig(output_filename)
plt.show()

print(f"\n3. Gráfico de dispersão gerado e salvo como '{output_filename}'.")
print("--- Fim do Script ---")