'''
Crie uma função que verifique se uma palavra ou frase é um palíndromo 
(lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado 
é True, responda “Sim”, se o resultado for False, responda "Não"
'''

#librarys
import unicodedata

#functions
def verificar_palindromo(texto):
    # Normaliza o texto para remover acentos.
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))

    # Converte para minúsculas e remove tudo que não for letra ou número.
    texto_limpo = ''.join(char.lower() for char in texto_sem_acentos if char.isalnum())
    
    return texto_limpo == texto_limpo[::-1] # Compara o texto limpo com sua versão invertida.

#main
if __name__ == "__main__":
    print("--- Verificador de Palíndromos ---")
    print("Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente.")
    
    frase_usuario = input("\nDigite uma palavra ou frase para verificar: ")
    resultado_e_palindromo = verificar_palindromo(frase_usuario)    # Chama a função.
    
    # Exibe o resultado de acordo com a especificação
    print("\nÉ um palíndromo?")
    if resultado_e_palindromo:
        print("Resultado: Sim")
    else:
        print("Resultado: Não")
