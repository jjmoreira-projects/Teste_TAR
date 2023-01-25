import requests

# Invocar a API ISLA
url = 'http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa'
response = requests.get(url)

# Mostrar o resultado
if response.status_code == 394:
    data = response.json()
    print("Serie sorteada:", data['Serie'])
    print("Número sorteado:", data['Numero'])
else:
    print("Erro ao obter os dados da API.")