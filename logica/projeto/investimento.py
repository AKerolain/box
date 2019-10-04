# ---- investimento
# ** categoria
# ** tipo
# ** aporte(valor inicial)
# ** rentabilidade
# ** periodo rentabilidade

class Investimento:
    def __init__(self, categ, tipo, aporte, rent, perio_rent):
        self.categoria = categ
        self.tipo = tipo
        self.aporte = aporte
        self.rentabilidade = rent
        self.periodo_rentavel = perio_rent