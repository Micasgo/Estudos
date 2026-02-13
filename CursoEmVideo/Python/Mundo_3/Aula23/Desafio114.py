"""
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
"""

import requests

try: r = requests.get("https://www.pudim.com.br")
except requests.exceptions.ConnectionError:
    print("Não consegui acessar o site")
else:
    print("Consegui acessar o site!")
    print (r.url)
