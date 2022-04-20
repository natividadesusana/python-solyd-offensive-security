arquivo = open('arquivo.txt', 'r')
# r = ler, w = escrever, a = apend/adicionar, rb = ler arquivo binário


# for i in range(1, 11):
#     arquivo.write('~ testando em '+ str(i) + '\n')
# arquivo.write('\nHELLO ~ SUSANA NATIVIDADE')


print(arquivo.read())

for linha in arquivo:
    print(linha)