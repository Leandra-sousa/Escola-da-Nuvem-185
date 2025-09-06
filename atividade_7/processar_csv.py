import pandas as pd

def ler_csv(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo, encoding="utf-8")
        print("\n--- Dados do Arquivo ---")
        print(df)  # Exibe a tabela inteira
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Execução
nome_arquivo = input("Digite o nome do arquivo CSV: ")
ler_csv(nome_arquivo)