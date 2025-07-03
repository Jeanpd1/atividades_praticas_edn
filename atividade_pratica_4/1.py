'''
Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve 
ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:​

1-A calculadora deve solicitar ao usuário que insira dois números e uma operação.​
2-As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).​
3-O programa deve continuar solicitando entradas até que uma operação válida seja concluída.​
4-Trate os seguintes erros:​
    -Entrada inválida (não numérica) para os números​
    -Divisão por zero​
    -Operação inválida​
1.Use try/except para capturar e tratar os erros apropriadamente.​
2.Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.​
3.Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.​
'''

#functions

def calculadora():
    while True:  # Inicia um loop infinito.
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            conta = input("Digite a operação (+, -, *, /): ")

            
            if conta == '+':
                resultado = n1 + n2
            elif conta == '-':
                resultado = n1 - n2
            elif conta == '*':
                resultado = n1 * n2
            elif conta == '/':
                if n2 == 0:    # Verifica a divisão por zero antes.
                    raise ZeroDivisionError # Retorna uma exceção ZeroDivisionError.
                resultado = n1 / n2
            else:
                raise ValueError("Operação inválida.")  # Retorna um ValueError.

           
            print(f"\n{n1} {conta} {n2} é igual a: {resultado}")  
            break   # Encerra o loop caso a conta seja bem sucedida.

        except ValueError as e:
            # Imprime erros de conversão(entrada não numérica).
            # Ou imprime exceção de operação inválida.
            if "Operação inválida" in str(e):
                print("\nOperação inválida. Use '+', '-', '*' ou '/'.")
            else:
                print("\nEntrada inválida. Digite apenas números.")
            print("Tente novamente.\n")

        except ZeroDivisionError:
            # Imprime a tentativa de divisão por zero.
            print("\nNão é possível dividir por zero.")
            print("Tente novamente.\n")

        except Exception as e:
            # Imprime qualquer outro erro inesperado.
            print(f"\nOcorreu um erro inesperado: {e}")
            print("Tente novamente.\n")

#Main
if __name__ == "__main__":
    calculadora()
