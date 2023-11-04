# Importa o módulo 'requests', necessário para realizar chamadas HTTP.
import requests

# Define a chave de acesso à API do AccuWeather.
CHAVE_API = 'OssvRcDsPAwXu6ijWycAFqjrabUAPAN2'
# Define a URL base para o serviço AccuWeather.
URL_BASE = 'http://dataservice.accuweather.com/'

# Define uma função que retorna a chave da localidade com base no nome da cidade.
def obter_chave_localidade(nome_cidade):
    # Cria o endpoint para buscar a chave da localidade usando a chave da API e o nome da cidade.
    endpoint = f"locations/v1/cities/search?apikey={CHAVE_API}&q={nome_cidade}"
    # Realiza a chamada HTTP GET para obter os dados.
    resposta = requests.get(URL_BASE + endpoint)
    # Transforma a resposta em formato JSON para um objeto Python.
    dados = resposta.json()
    # Se houver dados na resposta, retorna a chave da primeira cidade encontrada.
    if dados:
        return dados[0]["Key"]
    # Se não houver dados, retorna None (nenhum valor).
    else:
        return None

# Define uma função que imprime as informações do clima com base na chave da localidade.
def obter_clima(chave_localidade):
    # Cria o endpoint para obter a condição atual do tempo usando a chave da API e da localidade.
    endpoint = f"currentconditions/v1/{chave_localidade}?apikey={CHAVE_API}"
    # Realiza a chamada HTTP GET para obter os dados.
    resposta = requests.get(URL_BASE + endpoint)
    # Transforma a resposta em formato JSON para um objeto Python.
    dados = resposta.json()
    # Se houver dados na resposta, extrai e imprime as informações relevantes.
    if dados:
        temperatura = dados[0]["Temperature"]["Metric"]["Value"]
        texto_clima = dados[0]["WeatherText"]
        print(f"A temperatura é {temperatura}°C e o clima está {texto_clima}")
    # Se não houver dados, imprime uma mensagem de erro.
    else:
        print("Não foi possível obter a previsão do tempo.")

# Verifica se este script está sendo executado como programa principal.
if __name__ == "__main__":
    # Solicita ao usuário que insira o nome de uma cidade.
    nome_cidade = input("Digite o nome da cidade: ")
    # Utiliza a função definida anteriormente para obter a chave da localidade.
    chave_localidade = obter_chave_localidade(nome_cidade)
    # Se uma chave de localidade for encontrada, busca e imprime a previsão do tempo.
    if chave_localidade:
        obter_clima(chave_localidade)
    # Se não for encontrada nenhuma chave de localidade, imprime uma mensagem de erro.
    else:
        print("Cidade não encontrada!")
