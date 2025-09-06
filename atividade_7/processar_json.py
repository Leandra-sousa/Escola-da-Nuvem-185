"""Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade."""

import json

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print(f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            print("\n--- Dados do JSON ---")
            print(f"Nome: {dados['nome']}")
            print(f"Idade: {dados['idade']}")
            print(f"Cidade: {dados['cidade']}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Execução principal
pessoa = {
    "nome": "Leandra",
    "idade": 25,
    "cidade": "São Paulo"
}

arquivo = "pessoa.json"

# Escreve os dados no arquivo JSON
escrever_json(arquivo, pessoa)

# Lê os dados do arquivo JSON
ler_json(arquivo)