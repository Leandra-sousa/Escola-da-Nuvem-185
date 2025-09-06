"""Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade."""

import pandas as pd

def escrever_dados_pessoais_csv(nome_arquivo):
    
    try:
   
        dados = {
            'Nome': ['Henrique', 'Maria', 'João', 'Ana', 'Bruno'],
            'Idade': [30, 25, 45, 28, 35],
            'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba','Maceió']
        }

        df = pd.DataFrame(dados)


        df.to_csv(nome_arquivo, index=False, encoding='utf-8')

        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")

    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

nome_arquivo = 'informacoes_pessoais.csv'


escrever_dados_pessoais_csv(nome_arquivo)