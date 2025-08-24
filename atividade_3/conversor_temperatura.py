"""A fórmula para calcular a área de uma circunferência é: área = π ×raio2. Considerando para
este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável
raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal.

"""

print("=== Conversor de Temperaturas ===")

# Entrada
temperatura = float(input("Digite a temperatura: "))
origem = input("Informe a unidade de origem (Celsius, Fahrenheit ou Kelvin): ").capitalize()
destino = input("Informe a unidade de destino (Celsius, Fahrenheit ou Kelvin): ").capitalize()

resultado = None

# Conversões
if origem == "Celsius":
    if destino == "Fahrenheit":
        resultado = (temperatura * 9/5) + 32
    elif destino == "Kelvin":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura

elif origem == "Fahrenheit":
    if destino == "Celsius":
        resultado = (temperatura - 32) * 5/9
    elif destino == "Kelvin":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura

elif origem == "Kelvin":
    if destino == "Celsius":
        resultado = temperatura - 273.15
    elif destino == "Fahrenheit":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura

else:
    print("Unidade de origem inválida!")
    exit()

# Saída formatada
print(f"\n{temperatura:.2f} {origem} = {resultado:.2f} {destino}")