'''
4- Calculadora de Preço Total
 Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
 O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
'''

#vars
produto = "Cadeira Infantil"
preco = 12.40
quant = 3

preco_total = preco * quant # Calcula preço total


#main
print(f"Detalhes da Compra:")
print(f"Produto: {produto}")
print(f"Preço Unitário: R$ {preco:.2f}")
print(f"Quantidade: {quant}")
print("--------------------")
print(f"Preço Total: R$ {preco_total:.2f}")