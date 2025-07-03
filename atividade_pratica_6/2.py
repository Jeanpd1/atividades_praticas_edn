'''
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'.
O programa deve exibir o nome, email e país do usuário gerado."
'''

# librarys
import requests

# functions
def gerar_perfil():
    
    url_api = "https://randomuser.me/api/"  # URL da API para obter um usuário aleatório.
    
    try:
        resposta = requests.get(url_api)    # Faz a requisição GET para a API.
        resposta.raise_for_status() # Retorna uma exceção se a resposta da API for um erro.      
        dados = resposta.json() # Converte a resposta JSON em um dicionário Python.
        usuario = dados['results'][0]   # A API retorna os dados dentro de uma lista.
        
        # Extrai as informações desejadas do dicionário.
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        # Retorna os dados extraídos em um novo dicionário.
        perfil = {
            'nome': nome_completo,
            'email': email,
            'pais': pais
        }
        return perfil

    except requests.exceptions.RequestException as e:
        # Trata erros de conexão, timeout, etc.
        print(f"Falha ao se conectar com a API. ({e})")
        return None
    except (KeyError, IndexError):
        # Trata erros caso a estrutura do JSON seja inesperada.
        print("Não foi possível processar os dados recebidos da API.")
        return None

# main
if __name__ == "__main__":
    print("--- Gerador de Perfil de Usuário Aleatório ---")
    print("Buscando um novo perfil...")

    perfil_gerado = gerar_perfil()
    
    # Verifica se a função retornou um perfil com sucesso.
    if perfil_gerado:
        print("\n--- Perfil Gerado com Sucesso ---")
        print(f"Nome:   {perfil_gerado['nome']}")
        print(f"Email:  {perfil_gerado['email']}")
        print(f"País:   {perfil_gerado['pais']}")
    else:
        print("\nNão foi possível gerar o perfil. Tente novamente mais tarde.")
