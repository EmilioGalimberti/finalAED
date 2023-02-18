__author__ = 'Cátedra AED'

'''Creación de inicialización de variables tipo registros mediante constructores'''

#Inicialización de registro mediante función constructora.. INIT y self
class Empleado:
    def __init__(self, leg, nom, dir, suel, ant):
        self.legajo = leg
        self.nombre = nom
        self.direccion = dir
        self.sueldo = suel
        self.antiguedad = ant

# Esta función permite retornar los datos completos del registro
# de tipo Empleado.

def write(registro):                    #to_string
    print('Legajo: ', registro.legajo)
    print('Nombre: ', registro.nombre)
    print('Dirección: ', registro.direccion)
    print('Sueldo: ', registro.sueldo)
    print('Antiguedad:', registro.antiguedad)

def test():
    e1 = Empleado(100,'Pedro','General Paz',90000,5)
    write(e1)


if __name__=="__main__":
    test()
