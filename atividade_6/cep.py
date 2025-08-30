"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória."""

import requests

# Solicita o CEP ao usuário
cep = input("Digite o CEP (somente números): ")

# Monta a URL da API
url = f"https://viacep.com.br/ws/{cep}/json/"

# Faz a requisição
resposta = requests.get(url)

# Verifica se deu certo
if resposta.status_code == 200:
    dados = resposta.json()
    
    if "erro" not in dados:
        print("\n=== Endereço Encontrado ===")
        print("Logradouro:", dados["logradouro"])
        print("Bairro    :", dados["bairro"])
        print("Cidade    :", dados["localidade"])
        print("Estado    :", dados["uf"])
    else:
        print(" CEP não encontrado!")
else:
    print("Erro ao consultar a API:", resposta.status_code)