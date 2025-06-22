'''
2- Calculadora de Desconto
 Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
 O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

#vars
produto = "Camiseta"
preco = 50.00
desconto = 20
valor_desconto = (preco * desconto) / 100 #Calcula o valor do desconto
preco_final = preco - valor_desconto #Calcula o preço final

#main
print("--- Calculadora de Desconto ---")
print(f"Produto: {produto}")
print(f"Preço Original: R$ {preco:.2f}")
print(f"Percentual de Desconto: {desconto}%")
print("---------------------------------")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final com Desconto: R$ {preco_final:.2f}")
