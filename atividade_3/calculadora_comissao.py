"""Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""
# Entrada
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo (R$): "))
vendas = float(input("Digite o total de vendas (R$): "))

# Cálculo da comissão (15% sobre as vendas)
comissao = vendas * 0.15
salario_total = salario_fixo + comissao

# Saída formatada
print("\n--- Resultado ---")
print(f"Vendedor: {nome}")
print(f"Salário fixo: R$ {salario_fixo:.2f}")
print(f"Vendas no mês: R$ {vendas:.2f}")
print(f"Total a receber: R$ {salario_total:.2f}")