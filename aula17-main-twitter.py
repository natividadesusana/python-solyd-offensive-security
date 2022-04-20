from unittest import result
from twitter import Twitter
import time

consumer_key = 'WRXnyJds71yDayQaXFxPpI2jv'
consumer_secret = 'AjpaogRVFUyuZTfvaNgwj08J0pD3n6f1k08BjUUlapnUFca2w4'

token_key = '799122088594460672-vzJloX2qozKzEuJhNuyB1oew8rJSEzF'
token_secret = 'COd1bb65SodeBgD7zPTseuZ9lUBpkeeapROr0MXFprlqz'

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)

#resp = twitter.tweet('Vamos testar nossa lib')

pesquisa = twitter.tweet('solyd', 'pt')

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])

#print(pesquisa)

# for i in range(1, 100):
#     twitter.tweet('Vamos testar nossa lib' + str(i))
#     time.sleep(1)