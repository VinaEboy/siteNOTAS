import pandas as pd

# Ler o arquivo CSV e criar o DataFrame
df = pd.read_csv('tabela3.csv')

feitos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,21,
23,24,25,26,29,30,31,32,36,37,39,40,41,45,46,47,50,51,52,53,54,57,59]

fazendo = [46,47,50,52]

x = []

for i in range(60):
    if i in feitos and i not in fazendo:
        x.append(i)

df_selecionado = df.iloc[fazendo]

df_selecionado.to_csv('ambosfazendo.csv', index=False)