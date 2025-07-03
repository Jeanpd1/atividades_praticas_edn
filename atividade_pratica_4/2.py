'''
Crie um programa que permita a um professor registrar as notas de uma turma. O programa 
deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. 
O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir 
a média da turma. Notas = [] -> len(Notas)
'''

#functions
def notas_classe():
    notas = []  # Lista que armazena as notas.
    
    print("--- Sistema de Registro de Notas ---")
    print("Digite as notas dos alunos (0 a 10).")
    print("Para finalizar e calcular a média, digite 'fim'.\n")

    while True:
        entrada = input("Digite uma nota ou 'fim': ")
       
        if entrada.lower() == 'fim':    # Verifica se o usuário digitou 'fim'.
            break

        try:
            # Converte a entrada para um número do tipo float.
            # Se a entrada não for um número, gerará um ValueError.
            nota = float(entrada)

            if 0 <= nota <= 10: # Verifica se a nota está dentro do intervalo válido.
                notas.append(nota)  # Adiciona a nota válida à lista.
                print(f"Nota {nota} adicionada com sucesso.")
            else:
                # Informa ao usuário que a nota está fora do intervalo permitido.
                print("Nota inválida. Insira um valor entre 0 e 10.")

        except ValueError:
            # Retorna o erro se a entrada não puder ser convertida para um número.
            print("Entrada inválida. Digite um número ou 'fim'.")
                
    print("\n--- Resultado Final ---")  # Após o fim do loop, o programa calcula e exibe o resultado.

    # Verifica se a lista de notas não está vazia para evitar divisão por zero.
    if len(notas) > 0:
        soma_notas = sum(notas)
        quantidade_notas = len(notas)
        media = soma_notas / quantidade_notas

        print(f"Total de notas válidas registradas: {quantidade_notas}")
        print(f"Média: {media:.2f}")
    else:
        # Mensagem para o caso de nenhuma nota válida ter sido inserida.
        print("Nenhuma nota válida foi registrada. Não é possível calcular a média.")

#main
if __name__ == "__main__":
    notas_classe()
