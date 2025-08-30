"""Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento."""

from datetime import datetime

# Função para calcular idade em dias
def idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

# Entrada
ano = int(input("Digite o ano de nascimento: "))

# Saída
print(f"Sua idade em dias é aproximadamente: {idade_em_dias(ano)} dias")