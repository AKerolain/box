 class Veiculo:
    def __init__ (self, nome, marca, cor, potencia, ano, placa):
        self.nome = nome
        self.marca = marca
        self.cor = cor
        self.potencia = potencia
        self.ano = ano
        self.placa = placa

    def __str__(self):
        return f'{self.nome} - {self.marca} - {self.cor} - {self.potencia} - {self.ano} - {self.placa}'
