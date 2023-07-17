import csv
import os

# Ler o arquivo CSV e obter as listas de dados
with open('ambosfalta.csv', 'r') as file:
    csv_reader = csv.reader(file)
    listas_csv = list(csv_reader)

# Gerar o conteúdo HTML da tabela
html_table = '<table>'
for lista in listas_csv:
    html_table += '<tr>'
    for item in lista:
        html_table += '<td>{}</td>'.format(item)
    html_table += '</tr>'
html_table += '</table>'

# Ler o arquivo HTML existente
with open('../../templates/ambos2.html', 'r') as file:
    html_content = file.read()

# Encontrar o local onde deseja inserir a tabela no arquivo HTML
# e substituir o marcador pelo conteúdo da tabela em CSV
marcador = '<!-- INSERIR_TABELA_CSV -->'
html_content = html_content.replace(marcador, html_table)

# Salvar o conteúdo HTML modificado em um arquivo
with open('../../templates/ambos2.html', 'w') as file:
    file.write(html_content)