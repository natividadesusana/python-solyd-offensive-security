import requests
import json

req = None
try:
    req = requests.get('https://www.omdbapi.com/?apikey=e9409fce&t=Divergent')
except:
    print('Erro na conexão!')
    exit()

dicionario = json.loads(req.text)
print(dicionario)
print('Titulo Filme: ', dicionario['Title'])
print('Ano: ', dicionario['Year'])
print('Atores: ', dicionario['Actors'])
print('Diretores: ', dicionario['Director'])
print('Nota: ', dicionario['imdbRating'])