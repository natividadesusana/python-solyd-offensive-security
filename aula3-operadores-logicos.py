#Exercício Operadores Lógicos

idade = int(input('Escreva sua idade:'))
peso = float(input('Escreva seu peso:'))
altura = float(input('Escreva sua altura:'))

if idade > 18 and peso >= 60 and altura >= 1.70:
    print('Você está apto para entrar no exército!')
else:
    print('Você não está apto para entrar no exército!')