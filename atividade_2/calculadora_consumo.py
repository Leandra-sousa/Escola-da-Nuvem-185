""" Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:



Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# entrada
distancia_percorrida = 300 # quilometros (km)
combustivel_gasto = 25 # litros (l)

# calculo
consumo = distancia_percorrida / combustivel_gasto # 300 / 25

# saida
print("dados da viagem:")
print("distancia percorrida:", distancia_percorrida, "km")
print("combustivel gasto:", combustivel_gasto, "l")
print(f"consumo medio {consumo:.2f} km/l")
