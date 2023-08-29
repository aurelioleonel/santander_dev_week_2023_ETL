# Explorando ETL com Python
# Santader Dev Week 2023
# Marcos Aurélio Leonel

# Importando as bibliotecas nescessarias
import pandas as pd
import json

import csv

# Carregando os dados do arquivo
df = pd.read_csv('dados/clientes.csv')
print(df.to_string()+"\n")  # exibindo em formato de tabela


# Localizando o registro pelo 'id'
def get_user(user_id):
    usuario = df.loc[df['User_ID'] == user_id]

    # Converte o DataFrame para dicionário
    dict_usuario = usuario.to_dict('records')

    # Converte o dicionário para JSON
    json_usuario = json.dumps(dict_usuario[0], indent=2)

    return json_usuario


print(get_user(10)+"\n")


# Atualizando o registro pelo 'id'
def put_user(user_id, novo_nome, novo_email):
    # Encontra o índice da linha correspondente ao usuário com o User_ID fornecido
    indice = df[df['User_ID'] == user_id].index[0]

    # Atualiza o nome e o e-mail do usuário no DataFrame
    df.loc[indice, 'Nome'] = novo_nome
    df.loc[indice, 'Email'] = novo_email

    # Salva as alterações no arquivo CSV
    df.to_csv("dados/clientes.csv", encoding='utf-8-sig', index=False)

    return "Usuário atualizado com sucesso."


# Atualiza o nome e o e-mail do usuário com User_ID = 10
user_id = 10
novo_nome = "Marcos Aurelio Leonel"
novo_email = "etlcompython@python.com"
resultado = put_user(user_id, novo_nome, novo_email)

print(resultado+"\n")


# listando todos os registro em formato json
def get_all_user_json():
    # df = pd.read_csv('clientes.csv')

    # Converte o dataframe inteiro para dicionário
    data = df.to_dict('records')

    # Converte o dicionário para JSON
    json_data = json.dumps(data, indent=2)

    print(json_data)


get_all_user_json()


# Pode ser usado com for

# for index, row in df.iterrows():
#     # Converte cada linha para dicionário
#     linha = row.to_dict()
#
#     # Converte para JSON e imprime
#     json_row = json.dumps(linha, indent=2)
#     print(json_row)
