'''
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros:
    -valor_conta (float): O valor total da conta
    -porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna:
    -float: O valor da gorjeta calculada
'''

#functions
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    # Validação para garantir que os valores não sejam negativos
    if valor_conta < 0 or porcentagem_gorjeta < 0:
        return 0.0

    valor_calculado_gorjeta = (valor_conta * porcentagem_gorjeta) / 100
    return valor_calculado_gorjeta

#main
if __name__ == "__main__":
    print("--- Calculadora de Gorjetas ---")
    
    # Valida o valor total da conta.
    while True:
        try:
            conta_input = float(input("Digite o valor total da conta: R$ "))
            if conta_input >= 0:
                break
            else:
                print("O valor da conta não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Digite um número.")

    # Valida a porcentagem da gorjeta.
    while True:
        try:
            porcentagem_input = float(input("Digite a porcentagem de gorjeta desejada: "))
            if porcentagem_input >= 0:
                break
            else:
                print("A porcentagem não pode ser negativa. Tente novamente.")
        except ValueError:
            print("Digite um número.")
    
    gorjeta = calcular_gorjeta(conta_input, porcentagem_input)  # Chama a função.
    total_a_pagar = conta_input + gorjeta   # Calcula o valor total a ser pago.
    
    print("\n--- Resumo do Pagamento ---")
    print(f"Valor da Conta: R$ {conta_input:.2f}")
    print(f"Gorjeta ({porcentagem_input}%): R$ {gorjeta:.2f}")
    print(f"Valor Total a Pagar: R$ {total_a_pagar:.2f}")
