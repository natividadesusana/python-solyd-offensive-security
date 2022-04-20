# Biblioteca para trabalhar com partes/documentações de uma página:
# Beautiful Soup 4 BS4 - (pip install bs4) -

import requests

cabecalho = {'Users-agent': 'Windows Natividade Susana',
             'Referer': 'https:google.com',
             'Version': 'open'}

meus_cookies = {'Ultima-visita': '06/03/2022'}

dados = {'username': 'nativesana',
         'password': '123'}

texto = None

try:
    requisicoes = requests.post('https://putsreq.com/OryVndaJ4E5IQ6GFqd5i', # utilizando site Putsreq
                                headers=cabecalho,
                                cookies=meus_cookies,
                                data=dados)
    texto = requisicoes.text
except Exception as erro:
    print('Requisição deu erro: ', erro)

print(requisicoes)
print(requisicoes.text)
# print(type(requisicoes))
# print(requisicoes.status_code)
