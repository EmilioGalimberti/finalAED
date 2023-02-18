__author__ = 'Cátedra AED'

class Empleado:
    pass

def test():
    e1 = Empleado()
    # Agrego los campos al registro tipo Empleado (e1)
    e1.legajo = 1
    e1.nombre = 'Maria'
    e1.direccion = 'Calle1'
    e1.sueldo = 100000
    e1.antiguedad = 5

    print(e1)
    print('Legajo del empleado:', e1.legajo)

if __name__== "__main__":
    test()
