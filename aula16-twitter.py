import oauth2
import json
import urllib.parse
#import pprint

consumer_key = 'WRXnyJds71yDayQaXFxPpI2jv'
consumer_secret = 'AjpaogRVFUyuZTfvaNgwj08J0pD3n6f1k08BjUUlapnUFca2w4'

token_key = '799122088594460672-vzJloX2qozKzEuJhNuyB1oew8rJSEzF'
token_secret = 'COd1bb65SodeBgD7zPTseuZ9lUBpkeeapROr0MXFprlqz'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()