'''
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
'''

#librarys
from datetime import date # Biblioteca para obter a data atual

#functions
def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year   # Obtém o ano atual.
    
    # Validação para garantir que o ano de nascimento não seja no futuro.
    if ano_nascimento > ano_atual:
        return 0

    idade_em_anos = ano_atual - ano_nascimento  # Calcula a idade em anos
    idade_em_dias = idade_em_anos * 365 # Converte a idade em anos para dias.
    return idade_em_dias

#main
if __name__ == "__main__":
    print("--- Calculadora de Idade em Dias ---")
    
    # Coleta e valida o ano de nascimento.
    while True:
        try:
            ano_input = int(input("Digite o seu ano de nascimento: "))
            
            # Valida se o ano inserido é um valor razoável.
            if 1900 < ano_input <= date.today().year:
                break
            else:
                print(f"Insira um ano válido (entre 1901 e {date.today().year}).")
        except ValueError:
            print("Digite um número inteiro para o ano.")
            
    dias_de_vida = calcular_idade_em_dias(ano_input)    # Chama a função.
    
    if dias_de_vida > 0:
        print(f"\nVocê tem aproximadamente {dias_de_vida} dias de vida.")
    else:
        # Mensagem para o caso de o ano ser inválido, embora já validado acima.
        print("\nNão foi possível calcular a idade. Verifique o ano inserido.")
