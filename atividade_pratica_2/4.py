'''
4- Calculadora de Consumo de Combustível
 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. 
Use os seguintes dados:
* Distância percorrida: 300 km
* Combustível gasto: 25 litros
 O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,
incluindo o resultado final arredondado para duas casas decimais.
'''
#vars
distancia = 300  #em km
combustivel = 25 #em litros
consumo_medio = distancia / combustivel # Calcula o consumo

#main
print("Dados da Viagem:")
print(f"Distância Percorrida: {distancia} km")
print(f"Combustível Gasto: {combustivel} litros")
print("--------------------------------")
print("Resultado:")
print(f"O consumo médio foi de {consumo_medio:.2f} km/l.")
