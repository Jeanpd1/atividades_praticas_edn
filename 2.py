'''
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
'''

#functions
def imc():
  try:
    peso = float(input("Digite seu peso (em kg): "))
    altura = float(input("Digite sua altura (em metros, ex: 1.75): "))

    
    if peso <= 0 or altura <= 0:
      print("\nO peso e a altura devem ser valores positivos.")
      return # Encerra a função se os valores forem inválidos.

    imc = peso / (altura ** 2) # Calcula o IMC.

    if imc < 18.5:
      classificacao = "Abaixo do peso"
    elif imc < 25:
      classificacao = "Peso normal"
    elif imc < 30:
      classificacao = "Sobrepeso"
    else:
      classificacao = "Obeso"

    print(f"\nSeu IMC é de {imc:.2f}.")
    print(f"Classificação: {classificacao}")

  except ValueError:
    # Trata o erro caso o usuário digite algo que não seja número.
    print("\nDigite apenas números.")
  except ZeroDivisionError:
    # Trata o erro caso a altura seja zero.
    print("\nA altura não pode ser zero.")


#main
if __name__ == "__main__":
  imc()

