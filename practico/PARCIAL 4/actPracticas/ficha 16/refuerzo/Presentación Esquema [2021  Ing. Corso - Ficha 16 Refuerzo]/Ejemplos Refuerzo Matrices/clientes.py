__author__ = 'Catedra AED'

class Cliente:
    def __init__(self, ape , dest, f_pago):
        self.apellido = ape
        self.destino = dest
        self.forma_pago = f_pago

def write(cli):
    print('Apellido:', cli.apellido, end=' ')
    print('- Destino:', cli.destino, end=' ')
    print('- Forma pago:', cli.forma_pago)