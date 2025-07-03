'''
Crie um programa que gera uma senha aleatória com o módulo random, utilizando 
caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres
dessa senha aleatória.
'''

#librarys
import random
import string

#functions
def gerar_senha_aleatoria(tamanho):
    # Define os conjuntos de caracteres que serão usados.
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation

    # Cria o "pool" completo de todos os caracteres possíveis.
    pool_completo = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

    # Garante que a senha contenha pelo menos um de cada tipo de caractere.
    senha_temporaria = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    # Preenche o restante da senha com caracteres aleatórios.
    tamanho_restante = tamanho - 4
    for _ in range(tamanho_restante):
        senha_temporaria.append(random.choice(pool_completo))

    # Embaralha a lista para que os caracteres garantidos não fiquem sempre no início.
    random.shuffle(senha_temporaria)

    # Converte a lista de caracteres em uma string.
    senha_final = "".join(senha_temporaria)
    
    return senha_final

#main
if __name__ == "__main__":
    print("--- Gerador de Senhas Aleatórias ---")
    
    while True:
        try:
            # Solicita ao usuário o tamanho da senha.
            tamanho_da_senha = int(input("Digite a quantidade de caracteres para a senha (mínimo 8): "))

            # Valida se o tamanho é suficiente para uma senha segura.
            if tamanho_da_senha < 8:
                print("Para uma senha segura, escolha no mínimo 8 caracteres.")
                continue
            
            # Chamando a função.
            senha_gerada = gerar_senha_aleatoria(tamanho_da_senha)

            # Exibe a senha gerada.
            print(f"\nSua senha aleatória é: {senha_gerada}")
            break

        except ValueError:
            # Trata o erro caso o usuário não digite um número
            print("Entrada inválida. Digite um número inteiro.")
