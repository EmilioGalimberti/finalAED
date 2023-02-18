class Paciente:
    def __init__(self, numeroHistoria, nombre, numeroEspecialidad, numeroCobertura, monto):
        self.numeroHistoria = numeroHistoria
        self.nombre = nombre
        self.numeroEspecialidad = numeroEspecialidad
        self.numeroCobertura = numeroCobertura
        self.monto = monto
    def __str__(self):
        renglon = ''
        renglon += '{:>10}'.format(self.numeroHistoria)
        renglon += " "
        renglon += '{:>20}'.format(self.nombre)
        renglon += " "
        renglon += '{:>10}'.format(self.numeroEspecialidad)
        renglon += " "
        renglon += '{:>20}'.format(self.numeroCobertura)
        renglon += '{:>20}'.format(self.monto)
        return renglon


def titulos():
    renglon = ''
    renglon += '{:>16}'.format('Numero historia')
    renglon += " "
    renglon += '{:>15}'.format('Nombre')
    renglon += " "
    renglon += '{:>20}'.format('Numero especialidad')
    renglon += " "
    renglon += '{:>15}'.format('Numero Cobertura')
    renglon += " "
    renglon += '{:>10}'.format('Monto')
    return renglon

def to_string(obj):
    return ' |Numero Historia: ' + str(obj.numeroHistoria) + \
            ' |Nombre: ' + str(obj.nombre) + \
            ' |Numero Especialidad: ' + str(obj.numeroEspecialidad) + \
            ' |Numero Cobuertura: ' + str(obj.numeroCobertura) + \
            ' |Monto: ' + str(obj.monto)