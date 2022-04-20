'''
def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(maior([1,2,3,4,5,6,7,8,9,10]))
'''



# EXEMPLOS FUNÇÕES E MÉTODOS

'''print(len('native'))'''

'''
def soma(a, b):
    resp = a + b
    return resp
    
print(soma(50,50))
'''

'''
def imprime_oi():
    print('OI')

imprime_oi()
imprime_oi()
'''


'''
def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return '--deu ruim--'

print(tem_sete_itens('natividade'))

'''


