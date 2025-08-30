"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória."""

import random

def gerar_senha(tamanho):
   

    letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
    letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    especiais = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    todos_caracteres = letras_minusculas + letras_maiusculas + numeros + especiais

    
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha



tamanho = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho)
print(f"Sua senha gerada é: {senha_gerada}")
