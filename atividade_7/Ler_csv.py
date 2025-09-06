"""Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes."""

import pandas as pd

def ler_e_exibir_csv(nome_arquivo):
   
    try:
        # Lê o arquivo CSV em um DataFrame
        df = pd.read_csv(nome_arquivo)

        print("\nDados do arquivo CSV:")
        # Exibe o DataFrame completo no terminal
        print(df)

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


nome_do_arquivo = 'informacoes_pessoais.csv'
ler_e_exibir_csv(nome_do_arquivo)