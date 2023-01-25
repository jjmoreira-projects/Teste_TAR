import requests
url = "http://instituto.islagaia.pt/ws/wsrifa.asmx/Rifa"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Erro ao acessar a API. Código de status", response.status_codee)
        