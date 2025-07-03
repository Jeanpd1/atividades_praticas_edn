'''
Crie um programa que verifique se uma senha é forte. Uma senha forte 
deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa 
deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
'''

#functions
def verificar_senha():
 
    print("--- Verificador de Senha Forte ---")
    print("Uma senha forte deve ter no mínimo 8 caracteres e conter pelo menos um número.")
    
    while True:
        senha = input("\nCrie uma senha ou digite 'sair' para terminar: ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        # Validação das regras
        erros = []

        if len(senha) < 8:  # Verifica o comprimento da senha
            erros.append("A senha deve ter pelo menos 8 caracteres.")

        if not any(char.isdigit() for char in senha):   # Verifica se contém pelo menos um número
            erros.append("A senha deve conter pelo menos um número (0-9).")
            
        # Verifica o resultado
        if not erros:
            # Se a lista de erros estiver vazia, a senha é forte
            print("\nSucesso! Sua senha é forte e foi definida.")
            break
        else:
            # Se houver erros, exibe todos eles para o usuário
            print("Senha fraca. Por favor, corrija os seguintes pontos:")
            for erro in erros:
                print(f"- {erro}")

#main
if __name__ == "__main__":
    verificar_senha()
