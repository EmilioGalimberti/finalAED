_author_ = 'Emilio'

'''Consigna: Cargue un arreglo unidimensional con las edades de ciertas personas.
 La cantidad de componentes debe ser ingresado por teclado. a)Informar al usuario
 los elementos cargados en el arreglo.
 b) Informar las edades que se encuentren en una posición par.
 '''

import arreglos

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Ingrese la cantidad de componentes que tendra el vector '+ str(inf) + ':'))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def test():
    # cargar cantidad de elementos...
    n = validate(0)
    # Creación del arreglo.
    v1 = n * [0]

    # Carga del arreglo.
    arreglos.carga(v1)

    print('Carga finalizada del arreglo!!')
    # Comprobación rápida carga..
    print(v1)

    # Visualización de edades que estan en casillas cuyo indice es par.
    arreglos.posiciones_par(v1)

# Control de ejecución del módulo ejemplo0.py.
if __name__ == '__main__':
    test()
