'''
EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''

from cliente import Cliente
from conta import Conta

print('---------------')
cliente1 = Cliente('Susana', '084.559.887-33', 26)
conta_da_susana = Conta(5000, 1000)

print(conta_da_susana.consulta_saldo())
conta_da_susana.sacar(1000)
print(conta_da_susana.consulta_saldo())
conta_da_susana.depositar(100)
print(conta_da_susana.consulta_saldo())
conta_da_susana.sacar(4200)
print(conta_da_susana.consulta_saldo())


'''print('---------------')
cliente2 = Cliente('Cleonilde', '123.456.789-10', 40)
print(cliente2)'''

