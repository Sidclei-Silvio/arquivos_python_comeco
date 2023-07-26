import pandas as pd

# URL do arquivo CSV do dataset da FIFA
url = "https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv"

# Baixar o arquivo CSV e criar o DataFrame
try:
    df_fifa = pd.read_csv(url)
    print("DataFrame da FIFA baixado com sucesso!")
    print(df_fifa)  # Exibir as primeiras linhas do DataFrame
except Exception as e:
    print("Erro ao baixar o DataFrame da FIFA:", e)
