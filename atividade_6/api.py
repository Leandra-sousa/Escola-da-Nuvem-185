"""Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado"""

import requests 
url = "https://randomuser.me/api/"
resposta = requests.get(url)

# Verifica se deu certo
if resposta.status_code == 200:
    dados = resposta.json()
    usuario = dados['results'][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print("=== Perfil de Usuário Gerado ===")
    print("Nome :", nome)
    print("Email:", email)
    print("País :", pais)
else:
    print("Erro ao acessar a API:", resposta.status_code)