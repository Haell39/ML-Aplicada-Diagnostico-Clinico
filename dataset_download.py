import kaggle
import os
import zipfile

# Link do dataset: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data
dataset_name = 'uciml/breast-cancer-wisconsin-data'

download_path = './data'

# cria a pasta "data" se não existir
if not os.path.exists(download_path):
    os.makedirs(download_path)

print(f"Baixando o dataset '{dataset_name}' para '{download_path}'...")

# usando try e except para capturar erros de forma + profissional
try:
    kaggle.api.dataset_download_files(dataset_name, path=download_path, unzip=True)
    print("Download e descompactação concluídos com sucesso!")

    zip_file_path = os.path.join(download_path, os.path.basename(dataset_name.split('/')[1]) + '.zip')
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
        print(f"Arquivo zip '{os.path.basename(zip_file_path)}' removido.")

except Exception as e:
    print(f"Ocorreu um erro durante o download ou descompactação: {e}")
    print("Verifique se suas credenciais da API do Kaggle estão configuradas corretamente (arquivo kaggle.json em ~/.kaggle/).")


print("\nArquivos no diretório de download:")
for file in os.listdir(download_path):
    print(f"- {file}")