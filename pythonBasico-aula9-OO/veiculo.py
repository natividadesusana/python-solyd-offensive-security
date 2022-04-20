# classe é a receita do objeto, ou seja, um veiculo tem um tipo, uma cor, uma potencia, qtd rodas...
# objeto é quando nós pegamos a classe e instânciamos ela, criamos um objeto real a partir daquela classe.
# sempre criar métodos dentro da classe, o método é chamado construtor, ou seja, ele que constroi o objeto

class Veiculo:

    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        self.tanque += litros

