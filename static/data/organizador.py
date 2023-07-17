import pandas as pd

# Ler o arquivo .txt
with open('tabela2.csv', 'r') as file:
    linhas = file.readlines()

# Dividir cada linha em uma lista de frases
tabela = [linha.strip().split(',') for linha in linhas]

# Converter a lista em um DataFrame usando pandas
df = pd.DataFrame(tabela)

df.to_csv('nova_tabela.csv', index=False)

