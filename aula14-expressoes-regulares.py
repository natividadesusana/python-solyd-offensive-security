import re
import requests

requisicao = requests.get('https://hospitalbaiasul.com.br/contato/')
padrao = re.findall(r'[\w+@]\w+\.\w\.', requisicao.text)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado!')



# re = regular ou regex / regular expression / espressão regular
# site - regex101.com.br

'''
string_de_teste = 'O gato, a gata, gatinhos, gatões!'

padrao = re.findall(r'gat\w+', string_de_teste)    # r = RAW String.
# search p/ pesquisar uma palavra e findall p/pesquisar por tudo.
# podemos especificar \w{4,6} para achar de 4 a 6 letras

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado!')
'''


'''
emails = 'teste@eu-22.com.br'
padrao = re.findall(r'\w+@\w+\w-\w+\.', emails)
print(padrao)
'''
