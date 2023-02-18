_author_ = 'Emilio'
'''Desarrollar un programa que permita cargar dos arreglos uno con los nombres
de los empleados y otros con los sueldos.La cantidad de empleados debe cargarse
por teclado. Se pide: a) Informar el nombre de todos los empleados mayores a 18 años
que cobren un sueldo mayor a 10.000 ordenados alfabéticamente.
'''
import arreglos

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese la cantidad de empleados a cargar: '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n


def test():
    # Ingreso la cantidad de empleados a cargar.-
    n = validate(0)
    # Crear 3 arreglos paralelos o correspondientes
    nombres = n * [' ']
    sueldos = n * [0]
    edades = n * [0]

    # Cargar arreglos.
    arreglos.read(nombres, sueldos, edades)

    # Ordenar los arreglos
    arreglos.sort(nombres, sueldos, edades)

    # Creo una función para mostrar los nombres de emp. cuyo sueldo es superior a 10000
    arreglos.mostrar_nombres(nombres, edades, sueldos)

if __name__ == "__main__":
    test()
