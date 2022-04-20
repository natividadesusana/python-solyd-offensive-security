import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
    cotacao = json.loads(requisicao.text)

    print('#### COTAÇÃO #### /', datetime.datetime.now())
    print('Dólar:', cotacao['USDBRL']['high'])
    print('Euro:', cotacao['EURBRL']['high'])
    time.sleep(2)