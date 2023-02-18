__author__ = 'Catedra AED'

class Consumo:
    def __init__(self, el, gs, ag):
        self.electricidad = el
        self.gas = gs
        self.agua = ag

def write(cons):
    print('Gasto de electricidad:', cons.electricidad, end=' ')
    print('- Gas:', cons.gas, end=' ')
    print('- Agua:', cons.agua)

