from veiculo import Veiculo

class Carro(Veiculo):
    def __init__ (self, nome, marca, cor, potencia, ano, placa, volante):
        super().__init__ (nome, marca, cor, potencia, ano, placa)
        self.volante = volante

def __str__(self):
    return f'{ super().__str__() } - {self.volante}'       