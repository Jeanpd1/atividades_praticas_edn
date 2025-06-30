'''
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).
'''

#functions
def classificador_de_idade():
  """
  Solicita a idade do usuário e o classifica em Criança, Adolescente,
  Adulto ou Idoso.
  """
  try:
    idade = int(input("Digite sua idade: "))    # Insere a idade e converte para inteiro.

    # Condicional que verifica a idade inserida.
    if idade < 0:
      print("Digite uma idade válida.")
    elif 0 <= idade <= 12:
      print(f"Com {idade} anos, você é uma Criança")
    elif 13 <= idade <= 17:
      print(f"Com {idade} anos, você é um(a) Adolescente")
    elif 18 <= idade <= 59:
      print(f"Com {idade} anos, você é um(a) Adulto(a)")
    else: # Se a idade for 60 ou mais
      print(f"Com {idade} anos, você é um(a) Idoso(a)")

  except ValueError:
    # Trata o erro de números não inteiros
    print("Digite um número inteiro para a idade.")

#main
if __name__ == "__main__":
  classificador_de_idade()
  