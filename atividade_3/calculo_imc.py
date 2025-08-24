"""Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"

"""
peso = float(input("digite seu peso em kg (ex. 70.5): "))
altura = float(input("digite sua altura em metros (ex. 1.82): "))
imc = peso / (altura ** 2) 
if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc < 25:
    classificacao = "peso normal"
elif imc < 30:
    classificacao = "sobrepeso"
else:
    classificacao = "obeso"
print(f"seu imc é {imc:.1f}")
print(f"classificação: {classificacao}")