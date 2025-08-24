"""Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações,
 incluindo o resultado final.
"""

produto = "Cadeira Infantil"
preco_utilitario = 12.40
quantidade = 3 

total = preco_utilitario * quantidade
print(f"produto: {produto}")
print(f"Preço utilitario: R$ {preco_utilitario:.2f}")
print(f"quantidade: {quantidade}")
print(f"total: R$ {total:.2f}")