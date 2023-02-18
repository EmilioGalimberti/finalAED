class Programa:
    def __init__(self, clave, nombre, descripcion, cantidad, tipo_deporte, nivel):
        self.clave = clave
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.tipo_deporte = tipo_deporte
        self.nivel = nivel
    def __str__(self):
        renglon = ""
        renglon += '{:>6}'.format(self.clave)
        renglon += '   '
        renglon += '{:<25}'.format(self.nombre)
        renglon += ' '
        renglon += '{:<15}'.format(self.descripcion)
        renglon += '{:>8}'.format(self.cantidad)
        renglon += '  '
        renglon += '{:>8}'.format(self.tipo_deporte)
        renglon += '  '
        renglon += '{:>10}'.format(self.nivel)
        return renglon


def titulos():
        renglon = ""
        renglon += '{:>6}'.format("Clave")
        renglon += '   '
        renglon += '{:>30}'.format("Nombre")
        renglon += ' '
        renglon += '{:>35}'.format("Descripcion")
        renglon += '{:>37}'.format("Cantidad")
        renglon += '  '
        renglon += '{:>4}'.format("Tipo de deporte")
        renglon += '  '
        renglon += '{:>4}'.format("Nivel")
        return renglon
