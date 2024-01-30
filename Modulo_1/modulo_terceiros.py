# pip3 install requests==2.31.0

import requests

url = "https://exemplo.com.br"
response = requests.get(url)
print(f"Solicitação http para {url} retornou o status {response.status_code}")