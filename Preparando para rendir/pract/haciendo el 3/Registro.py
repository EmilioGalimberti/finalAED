class Programa:
    #FIJATSE BIEN DE PONER INIT NO INT XDXDXD
    def __init__(self, clave, nombre, descripcion, cantDeportistasReg, tipo_deporte, nivel):
        self.clave = clave
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantDeportistasReg = cantDeportistasReg
        self.tipo_deporte = tipo_deporte
        self.nivel = nivel

    def __str__(self):
        renglon = ""
        renglon += "{:>6}".format(self.clave)
        renglon += "  "
        renglon += "{:>25}".format(self.nombre)
        renglon += "  "
        renglon += "{:>25}".format(self.descripcion)
        renglon += ""
        renglon += "{:>25}".format(self.cantDeportistasReg)
        renglon += ""
        renglon += "{:>25}".format(self.tipo_deporte)
        renglon += ""
        renglon += "{:>25}".format(self.nivel)
        return renglon

def titulos():
    renglon = ""
    renglon += '{:>6}'.format("Clave")
    renglon += '   '
    renglon += '{:>39}'.format("Nombre")
    renglon += ' '
    renglon += '{:>35}'.format("Descripcion")
    renglon += '{:>37}'.format("cantDeportistasReg")
    renglon += '  '
    renglon += '{:>15}'.format("Tipo de deporte")
    renglon += '  '
    renglon += '{:>14}'.format("Nivel")
    return renglon



def to_string(reg):
    return "  |clave : " + str(reg.clave) + \
            "  |Nombre : " + str(reg.nombre) + \
            "  |Descriocuib : " + str(reg.descripcion) + \
            "  |cantDeportista : " + str(reg.cantDeportistasReg) + \
            "  |tipo_deporte : " + str(reg.tipo_deporte) + \
            "  |nivel: " + str(reg.nivel)