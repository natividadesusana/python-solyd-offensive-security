print('Controle de Festa ')
print('~~~~~~~~~~~~~~~~~~')

'''numero_de_convidados = input('Coloque o número de convidados: ')
lista_de_convidados = []

i = 1
while i <= int(numero_de_convidados):
    nome_do_convidados = input('Coloque o nome do convidado #'+ str(i) +': ')
    lista_de_convidados.append(nome_do_convidados)
    i += 1

print('\n# Serão', numero_de_convidados, 'convidados.')

print('\n# LISTA DE CONVIDADOS:')
for convidado in lista_de_convidados:
    print('-', convidado)
'''
'''
print('Controle de Festa')
print('-----------------')

qtd_convidados = int(input('Informe o número de convidados: '))
lista = []
i = 1

while i <= int(qtd_convidados):
    nome = input('%iº Convidado' %i + ': \n')
    lista.append(nome)
    i += 1

print('\n# Serão', qtd_convidados, 'convidados.')

print('\n# LISTA DE CONVIDADOS:')

for convidado in lista:
    print('-', convidado)
'''



# o for (for nome in nomes:) se lê, => para cada objeto dentro de uma lista de coleção, você executa tal coisa.
# a função range cria uma lista de números

# coleção => for i in nomes:
# item => for i in range():

# i = i+1 ou são iguais i += 1


lista_compras = []
print('# Bem vindo')
print('Informe as compras')

for item in range(5):
    lista_compras.append((input('Item ' + str(item+1) + ': \n')))
    print(lista_compras)

print('\nLista de compras completas: ', lista_compras)


'''
lista = ['caju', 'uva', 'amora', 'pera', 'chuchu']
contador = 0

for fruta in lista:
    contador += 1

print('Quantidade de Frutas : ', contador)

        OU PODE SER FEITO MAIS SIMPLES:
        
lista = ['caju', 'uva', 'amora', 'pera', 'chuchu']
print('Quantidade de Frutas : ', len(lista))
'''

'''
from time import sleep

n = 1

while True:
    print(n)
    if n == 10:
        break
    n += 1
    sleep(0.7)

print('\nSaiu do while!')
'''