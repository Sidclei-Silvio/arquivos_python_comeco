import pandas as pd

# Ler o dataframe
# listar os 5 primeiros
df = pd.read_excel("./raw-data/online_retail_II.xlsx")
print(df.head())
