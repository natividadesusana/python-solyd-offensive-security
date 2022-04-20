print('--------------------------------------')


# try:
#     a = 1200 / 0
# except:
#     print('Divisão por zero, não da pra fazer!!')

# print('\nrodando restante do programa ...')


# try:
#     teste()
# except Exception as erro:
#     print('Aconteceu algum erro: ', erro)

# print('\nrodando restante do programa ...')


# try:
#     a = 2 / 0
# except Exception as erro:
#     print('Aconteceu algum erro: ', erro)

# print('\nrodando restante do programa ...')


import time

def abre_arquivo():
    try:
        arquivo = open('arquivo-teste.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro: ', erro)
        return False

while not abre_arquivo():
    print('\nTentando abrir o aquivo ...')
    time.sleep(5)

print('\nConsegui abrir o arquivo !!')