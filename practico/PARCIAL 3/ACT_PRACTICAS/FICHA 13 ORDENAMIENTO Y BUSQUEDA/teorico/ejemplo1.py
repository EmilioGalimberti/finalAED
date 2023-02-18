_author_ = 'Emilio'

'''Consigna: Cargue un arreglo unidimensional con números enteros.
 La cantidad de componentes debe ser ingresado por teclado. Informar al usuario
 los números cargados.'''

import modulos

def validar(inf): #valida que no se carguen numeros menores o iguales a  cero para comenzar el vector
        n = inf
        while n <= inf:
            n = int(input('Cantidad de elementos (> a ' + str(inf) + ' por favor): '))
            if n <= inf:
                print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
            return n

def test():
    #--------------------------------- VALIDAR------------------------------------------------
    # cargar cantidad de elementos...
    n = validar(0) #le asigna a inf el valor cero
    # Creación del arreglo.
    v1 = n * [0]
    print(v1)
    #--------------------------------- CARGA DE ARREGLO------------------------------------------------
    modulos.carga(v1)  #funcion carga v1 como parametro se lo mandamos a la funcion
    print(' Carga finalizada del arreglo!!')
    # Comprobación rápida carga..
    print(v1)
    #--------------------------------- BUSQUEDA SECUENCIAL------------------------------------------------
    # Activo la función de búsqueda secuencial.
    x = int(input('Ingrese el valor a buscar:'))
    ind = modulos.linear_search(v1, x) #V1 es la lista que remplaza V en la funcion
    #ind = i que encontro el indice del vector
    if ind >= 0:
        print('El valor', x, ' se encontró en la casilla:', ind, 'VECTOR NO ORDENADO BUSQUEDA SECUENCIAL')
    else:
        print('El valor buscado no se encuentra en el vector!!')

    #--------------------------------- ORDENAMIENTO DE  MENOR A MAYOR------------------------------------------------

    #activo la funcion para ordinamiento directo de menor a mayor
    modulos.selection_sort(v1) #se toma v1 como parametro para que remplaze v en la funcion, esta seria la lista
    #check de arreglo ordenado
    print('el arreglo ordenado de menor a mayor es: ', v1)

    #--------------------------------- BUSQUEDA BINARIA------------------------------------------------
    x = int(input('Ingrese el valor a buscar:'))
    ind = modulos.binary_search(v1, x) #solo se puede usar si el vector esta ordenado
    if ind >= 0:
        print('Elemento se encontró en la posición', ind)
    else:
        print('Elemento no se encontró en el vector')

# Control de ejecución del módulo ejemplo1.py. esto si o si en el programa general o bajan puntos
if __name__ == '__main__':
    test()
