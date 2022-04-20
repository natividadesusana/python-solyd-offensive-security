from veiculo import Veiculo

# Aqui o Carro herdou as caracteristicas do pai Veiculo
class Carro(Veiculo):

# Aqui toda vez que está iniciando o carro o construtor carro
# na seguinte linha ele está criando um Veiculo
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print('Erro: tanque com incapacidade inferior!')
        else:
            self.tanque += litros
