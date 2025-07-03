'''
Crie um programa que solicite ao usuário que insira números inteiros. O programa 
deve continuar solicitando números até que o usuário digite 'fim'. Para cada número 
inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo 
que não seja um número inteiro, o programa deve informar o erro e continuar. No final,
o programa deve exibir a quantidade de números pares e ímpares inseridos.
'''

#functions
def classificar_numeros():
    # Inicializa os contadores.
    contador_pares = 0
    contador_impares = 0

    print("--- Classificador de Números ---")
    print("Digite números inteiros ou digite 'fim' para encerrar.\n")

    while True:
        entrada_usuario = input("Digite um número ou 'fim' para encerrar: ")

        if entrada_usuario.lower() == 'fim':    # Verifica a condição de saída.
            break

        try:
            numero = int(entrada_usuario)   # Tenta converter a entrada para um número inteiro.

            if numero % 2 == 0: # Verifica se o número é par ou ímpar usando módulo.
                print(f"O número {numero} é PAR.")
                contador_pares += 1  # Incrementa o contador de pares
            else:
                print(f"O número {numero} é ÍMPAR.")
                contador_impares += 1  # Incrementa o contador de ímpares

        except ValueError:
            # Retorna o erro se a entrada não for um número válido
            print("Entrada inválida. Insira um número válido.\n")
                
    # Exibe o resumo final após o término do loop
    print("\n--- Fim do Programa ---")
    print(f"Total de números pares inseridos: {contador_pares}")
    print(f"Total de números ímpares inseridos: {contador_impares}")


#main
if __name__ == "__main__":
    classificar_numeros()
