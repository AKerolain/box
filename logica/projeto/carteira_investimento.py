# ---- carteira investimento
# ** investimento
# ** quantidade
# ** rentabilidade mensal
# ** rentabilidade anual
class Carteira_investimento:
    def __init__(self, invest, qtd, rent_mensal, rent_anual):
        self.investimento = invest
        self.quantidade= qtd
        self.rentabilidade_mensal = rent_mensal
        self.rentabilidade_anual = rent_anual