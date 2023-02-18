class Deportista:
    def __init__(self, numIdent, nombre, deporte, codigoBeca, monto):
        self.numIdent = numIdent
        self.nombre = nombre
        self.deporte = deporte
        self.codigoBeca = codigoBeca
        self.monto = monto
    def __str__(self):
        renglon = ""
        renglon += "{:>10}".format(self.numIdent)
        renglon += " "
        renglon += "{:>10}".format(self.nombre)
        renglon += " "
        renglon += "{:>10}".format(self.deporte)
        renglon += " "
        renglon += "{:>10}".format(self.codigoBeca)
        renglon += " "
        renglon += "{:>10}".format(self.monto)
        renglon += " "
        return renglon

def titulos():
    renglon = ""
    renglon += "{:>10}".format("numIdentificacion")
    renglon += " "
    renglon += "{:>10}".format("nombre")
    renglon += " "
    renglon += "{:>10}".format("deporte")
    renglon += " "
    renglon += "{:>10}".format("codigoBeca")
    renglon += " "
    renglon += "{:>10}".format("monto")
    return renglon

def to_string(obj):
    return " |NumeroIdentificacion: " + str(obj.numIdent) + \
            " |Nombre: " + str(obj.nombre) + \
            " |deporte: " + str(obj.deporte) + \
            " |codigoBeca: " + str(obj.codigoBeca) + \
            " |monto: " + str(obj.monto)