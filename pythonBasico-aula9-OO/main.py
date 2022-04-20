# Aqui usamos 1 classe, chamada Veiculo que é a receitinha do veiculo
# para criar 2 objetos, criamos o caminhão verde e o carro azul.

from veiculo import Veiculo
from carro import Carro

caminhao_verde = Veiculo('Verde', 6, 'Honda', 100)
print('CAMINHÃO VERDE')
print('Cor: ', caminhao_verde.cor)
print('Qtd Rodas: ', caminhao_verde.rodas)
print('Marca: ', caminhao_verde.marca)
print('Tanque: ', caminhao_verde.tanque)

print('---------------------')

carro_azul = Carro('Azul', 'BMW', 30)
print('CARRO AZUL')
print('Cor: ', carro_azul.cor)
print('Qtd Rodas: ', carro_azul.rodas)
print('Marca: ', carro_azul.marca)
print('Tanque: ', carro_azul.tanque)
carro_azul.abastecer(40)
print('Tanque: ', carro_azul.tanque)

print('---------------------')

caminhao_verde.abastecer(20)
print('Tanque: ', caminhao_verde.tanque)



