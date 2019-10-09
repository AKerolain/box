class Moto(Veiculo):
    def __init__ (self, nome, marca, cor, potencia, ano, placa, guidao):
        super().__init__ (nome, marca, cor, potencia, ano, placa)
        self.guidao = guidao

def __str__(self):
    return f'{ super().__str__() } - {self.guidao}'       