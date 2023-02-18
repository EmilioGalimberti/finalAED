class Gasto:
    def __init__(self, cod, des, me, suc, imp):
        self.codigo = cod
        self.descripcion = des
        self.mes = me  # 1-12
        self.sucursal = suc  # 0-2
        self.importe = imp

    def __str__(self):  # Convierte a string la variable registro
        renglon = ''
        renglon += '{:>5}'.format(self.codigo)
        renglon += ' '
        renglon += '{:<20}'.format(self.descripcion)
        renglon += ' '
        renglon += '{:>3}'.format(self.mes)
        renglon += ' '
        renglon += '{:>10}'.format(self.sucursal)
        renglon += ' '
        renglon += '{:>10.2f}'.format(self.importe)
        return renglon


def to_string(gas):  # Convierte a string la variable registro
    renglon = ''
    renglon += '{:>5}'.format(gas.codigo)
    renglon += ' '
    renglon += '{:<20}'.format(gas.descripcion)
    renglon += ' '
    renglon += '{:>3}'.format(gas.mes)
    renglon += ' '
    renglon += '{:>10}'.format(gas.sucursal)
    renglon += ' '
    renglon += '{:>10.2f}'.format(gas.importe)
    return renglon


def get_titulos():
    renglon = ''
    renglon += '{:>5}'.format("Cód.")
    renglon += ' '
    renglon += '{:<20}'.format("Descripción")
    renglon += ' '
    renglon += '{:>3}'.format("Mes")
    renglon += ' '
    renglon += '{:>10}'.format("Sucursal")
    renglon += ' '
    renglon += '{:>10}'.format("Importe")
    return renglon
