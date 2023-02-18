
class Plantas:
    def __init__(self, numero, nombre, tipo, precio, disponibles):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.disponibles = disponibles


def to_string(a):
    return 'Número:{:>5} Nombre: {:<5} Tipo: {:<5} Precio: {:>5.2f} Disponibles: {:>3}'.format(a.numero, a.nombre, a.tipo, a.precio, a.disponibles)
