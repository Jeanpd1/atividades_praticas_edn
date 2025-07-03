'''
Desenvolva um programa que consulte informações de endereço a partir de um CEP
fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir
o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
'''

#librarys
import requests

#functions
def consultar_cep(cep):
    # Remove caracteres não numéricos.
    cep_limpo = "".join(filter(str.isdigit, cep))

    # Verifica se o CEP limpo tem o tamanho padrão.
    if len(cep_limpo) != 8:
        print("O CEP deve conter 8 dígitos.")
        return None

    # Monta a URL da API com o CEP fornecido.
    url_api = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        resposta = requests.get(url_api)    # Faz a requisição GET.
        resposta.raise_for_status() # Retorna uma exceção se a resposta da API indicar um erro.
        dados_endereco = resposta.json()    # Converte a resposta JSON em um dicionário.
        
        # A API retorna um dicionário com a chave 'erro' se o CEP não for encontrado.
        if dados_endereco.get('erro'):
            print(f"CEP '{cep}' não encontrado.")
            return None
            
        return dados_endereco

    except requests.exceptions.RequestException as e:
        print(f"Não foi possível consultar a API. ({e})")   # Trata erros de conexão.
        return None

#main
if __name__ == "__main__":
    print("--- Consulta de Endereço por CEP ---")
    
    cep_usuario = input("Digite o CEP que deseja consultar: ")
    endereco = consultar_cep(cep_usuario)   # Chama a função.
    
    # Verifica se a função retornou um endereço com sucesso.
    if endereco:
        print("\n--- Endereço Encontrado ---")
        print(f"Logradouro: {endereco.get('logradouro', '')}")
        print(f"Bairro:     {endereco.get('bairro', '')}")
        print(f"Cidade:     {endereco.get('localidade', '')}")
        print(f"Estado:     {endereco.get('uf', '')}")
    else:
        print("\nNão foi possível obter as informações do endereço. Verifique o CEP e sua conexão.")
