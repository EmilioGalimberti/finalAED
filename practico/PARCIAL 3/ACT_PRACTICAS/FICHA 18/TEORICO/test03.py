__author__ = 'Cátedra AED'

'''Enunciado: Se desea almacenar en un arreglo la información de los n estudiantes que se
registraron para participar de un curso de programación.
Por cada estudiante se tiene su:
número de legajo,su nombre y su promedio en la carrera que cursa.
Muestre los datos de los estudiantes cargados que hayan obtenido una nota superior a 8.'''


class Estudiante:
    def __init__(self, leg, nom, prom):
        self.legajo = leg
        self.nombre = nom
        self.promedio = prom

def validate(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def write(reg_estudiante):
    print('Legajo:', reg_estudiante.legajo, end=' ')
    print('Nombre:', reg_estudiante.nombre, end=' ')
    print('Promedio:', reg_estudiante.promedio)

def read(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        leg = int(input('Ingrese un legajo:'))
        nom = input('Ingrese el nombre:')
        prom = int(input('Ingrese un promedio:'))

        # Creación de un registro tipo Estudiante.

        estudiantes[i] = Estudiante(leg, nom, prom)

def mostrar(estudiantes):
    for i in range(len(estudiantes)):
        if estudiantes[i].promedio >= 8:
            write(estudiantes[i])


def test():
    n = validate(0, 'Ingrese el tamaño del vector:')
    estudiantes = n * [None]

    # Carga del arreglo de estudiantes..
    read(estudiantes)

    # Muestro los estudiantes ..(Completar)
    mostrar(estudiantes)


if __name__ == "__main__":
    test()
