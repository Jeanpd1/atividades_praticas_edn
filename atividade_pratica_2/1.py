'''
1- Conversor de Moeda
 Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
 O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
'''

#vars 
valor_reais = 100.00    #Define os valores
taxa_dolar = 5.20
taxa_euro = 6.15
valor_dolar = valor_reais / taxa_dolar  #cálculo de taxas
valor_euro = valor_reais / taxa_euro

#main
print(f"Valor original: R$ {valor_reais:.2f}")
print("--- Conversão ---")
print(f"Valor em Dólares: US$ {valor_dolar:.2f}")
print(f"Valor em Euros: € {valor_euro:.2f}")