class Alquiler:
    def __init__(self, numero, descripcion, tipo, importe, dias):
        self.numero = numero
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.dias = dias


def to_string(a):
    return "{:>5} {:<20} {:1} Precio: {:>12.2f} {:>3}".format(a.numero, a.descripcion, a.tipo, a.importe, a.dias)

