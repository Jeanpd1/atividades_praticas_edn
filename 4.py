'''
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) 
que não são divisíveis por 400.
'''

#functions
def ano_bissexto():
    try:
        ano = int(input("Digite um ano(ex: 2024): "))
        # Garante que o ano seja um número positivo.
        if ano <= 0:
            print("\nInsira um ano válido (positivo).")
            return

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"\nO ano {ano} é bissexto.")
        else:
            print(f"\nO ano {ano} não é bissexto.")

    except ValueError:
        # Trata o erro se o usuário não digitar um número inteiro.
        print("\nDigite um número de ano inteiro.")

#main
if __name__ == "__main__":
    ano_bissexto()
