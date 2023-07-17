import pandas as pd

# Ler o arquivo CSV e criar o DataFrame
df = pd.read_csv('tabela.csv')

# Remover a última coluna vazia
df = df.drop(df.columns[-1], axis=1)

# Exibir o DataFrame resultante
df.to_csv('tabela2.csv', index=False)