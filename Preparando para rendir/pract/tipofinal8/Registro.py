'''Un centro de alto rendimiento deportivo necesita un programa que le permita operar con los diferentes planes de
entrenamiento que tiene disponibles. De cada Plan, se tiene
una clave de identificación (una cadena que puede tener dígitos y caracteres),
el nombre o título del plan (una cadena),
la descripción del contenido detallado del plan (una cadena con un texto terminado en punto y con palabras separadas por un blanco (por ejemplo: “Plan semanal de
caminata intensiva con al menos una hora de recorrido y seis kilómetros de alcance.”),
el monto a abonar para tomar ese plan,
un número entre 1 y 10 que indica el tipo de plan (por ejemplo: 1: Básico, 2: Mantenimiento, 3: Deporte
profesional, etc.),
y otro número, pero entre 1 y 5 para indicar el rango de edad recomendable para tomar el plan (por
ejemplo: 1: niños y adolescentes entre 6 y 14 años, 2: Jóvenes entre 15 y 18, etc.).'''


class Plan:
    def __init__(self, claveIdent, nombre, descripcion, monto, tipoPlan, rangoEdad):
        self.claveIdent = claveIdent
        self.nombre = nombre
        self.descripcion = descripcion
        self.monto = monto
        self.tipoPlan = tipoPlan
        self.rangoEdad = rangoEdad

    def __str__(self):
        renglon = ''
        renglon += '{:>10}'.format(self.claveIdent)
        renglon += " "
        renglon += '{:>10}'.format(self.nombre)
        renglon += " "
        renglon += '{:>10}'.format(self.descripcion)
        renglon += " "
        renglon += '{:>10}'.format(self.monto)
        renglon += " "
        renglon += '{:>10}'.format(self.tipoPlan)
        renglon += " "
        renglon += '{:>10}'.format(self.rangoEdad)
        return renglon


def titulos():
    renglon = ''
    renglon += '{:>10}'.format("Clave Identificacion")
    renglon += " "
    renglon += '{:>10}'.format('Nombre')
    renglon += " "
    renglon += '{:>10}'.format('Descripcion')
    renglon += " "
    renglon += '{:>10}'.format('Monto')
    renglon += " "
    renglon += '{:>10}'.format('Tipo PLan')
    renglon += " "
    renglon += '{:>10}'.format('Rango Edad')
    return renglon


def to_string(obj):
    return ' |Clave Identificacion: ' + str(obj.claveIdent) + \
        ' |Nombre: ' + str(obj.nombre) + \
        ' |Descripcion: ' + str(obj.descripcion) + \
        ' |Monto: ' + str(obj.monto) + \
        ' |Tipo Plan' + str(obj.tipoPlan) + \
        ' |Rango Edad' + str(obj.rangoEdad)
