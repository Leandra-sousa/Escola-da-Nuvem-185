"""Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

import string

def eh_palindromo(texto):
    # Coloca em minúsculas
    texto = texto.lower()
    # Remove espaços e pontuação
    texto = ''.join(ch for ch in texto if ch.isalnum())
    # Verifica se é igual ao reverso
    return texto == texto[::-1]

# Entrada
frase = input("Digite uma palavra ou frase: ")

# Saída
if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")