'''
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

#functions
def conversor_temp():
    try:
        valor_temp = float(input("Digite a temperatura: "))
        origem = input("Qual unidade de medida? (C, F ou K): ").upper().strip()
        convertido = input("Para qual unidade converter? (C, F ou K): ").upper().strip()
        validos = ["C", "F", "K"]

        # Validar se unidades são válidas
        if origem not in validos or convertido not in validos:
            print("\nErro: Unidade inválida. Por favor, use 'C', 'F' ou 'K'.")
            return

        if origem == convertido:
            print(f"\nA temperatura já está em {origem}. O valor é {valor_temp:.2f}°{origem}.")
            return

        # Converte a temperatura para celsius
        temp_em_celsius = 0
        if origem == 'C':
            temp_em_celsius = valor_temp
        elif origem == 'F':
            temp_em_celsius = (valor_temp - 32) * 5 / 9 # Fórmula Fahrenheit
        elif origem == 'K':
            temp_em_celsius = valor_temp - 273.15   # Fórmula Kelvin

        # Converter de celsius para unidade desejada
        resultado_final = 0
        if convertido == 'C':
            resultado_final = temp_em_celsius
        elif convertido == 'F':
            resultado_final = (temp_em_celsius * 9 / 5) + 32    # De celsius para Fahrenheit
        elif convertido == 'K':
            resultado_final = temp_em_celsius + 273.15  # De celsius para Kelvin

        # Resultado final
        print(f"\nConversão concluída:")
        print(f"{valor_temp:.2f}°{origem} é igual a {resultado_final:.2f}°{convertido}")

    except ValueError:
        print("\nO valor da temperatura deve ser válido.")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

#main
if __name__ == "__main__":
    conversor_temp()
