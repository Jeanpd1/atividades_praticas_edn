'''
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação 
ao Real Brasileiro (BRL). O usuário deve informar o código da moeda 
desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação.
'''

#librarys
import requests
from datetime import datetime

#functions
def consultar_cotacao(codigo_moeda):
    moeda_limpa = codigo_moeda.upper().strip()  # Padroniza o código da moeda.
       
    if not moeda_limpa:  # Verifica se o código da moeda foi informado.
        print("O código da moeda não pode estar em branco.")
        return None

    # Monta a URL da API com a moeda desejada. O par é sempre MOEDA-BRL.
    url_api = f"https://economia.awesomeapi.com.br/last/{moeda_limpa}-BRL"
    
    try:
        resposta = requests.get(url_api)
        resposta.raise_for_status() # Retorna uma exceção para erros HTTP.        
        dados_api = resposta.json() # Converte a resposta JSON em um dicionário.
        
        # A API retorna um dicionário onde a chave principal é o par de moedas.
        chave_principal = f"{moeda_limpa}BRL"
        if chave_principal in dados_api:
            return dados_api[chave_principal]
        else:
            # Caso a resposta seja ok mas o formato seja inesperado.
            print(f"Não foram encontrados dados para a moeda '{codigo_moeda}'.")
            return None

    except requests.exceptions.HTTPError as e:
        # Trata especificamente o erro 404, que significa que a moeda não existe na API.
        if e.response.status_code == 404:
            print(f"A moeda '{codigo_moeda}' não é válida ou não foi encontrada.")
        else:
            print(f"Erro HTTP ao consultar a API: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível consultar a API. ({e})")   # Trata outros erros de conexão.
        return None

#main
if __name__ == "__main__":
    print("--- Consulta de Cotação de Moedas ---")
    
    moeda_usuario = input("Digite o código da moeda desejada (ex: USD, EUR, GBP): ")
    cotacao = consultar_cotacao(moeda_usuario)   # Chama a função.
    
    # Verifica se a função retornou uma cotação com sucesso.
    if cotacao:
        # Formata a data e hora para um padrão mais legível.
        data_hora_atualizacao = datetime.strptime(cotacao.get('create_date'), '%Y-%m-%d %H:%M:%S')
        data_hora_formatada = data_hora_atualizacao.strftime('%d/%m/%Y às %H:%M:%S')
        
        print(f"\n--- Cotação de {cotacao.get('name', '')} ---")
        print(f"Valor Atual (Venda): R$ {cotacao.get('bid', 'N/A')}")
        print(f"Máxima do Dia:      R$ {cotacao.get('high', 'N/A')}")
        print(f"Mínima do Dia:      R$ {cotacao.get('low', 'N/A')}")
        print(f"Última Atualização: {data_hora_formatada}")
    else:
        print("\nNão foi possível obter os dados da cotação. Verifique o código da moeda e sua conexão.")