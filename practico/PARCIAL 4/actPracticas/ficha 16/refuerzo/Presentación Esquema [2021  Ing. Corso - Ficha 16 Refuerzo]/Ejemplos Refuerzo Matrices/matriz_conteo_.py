__author__ = 'Catedra AED'

'''Se desea almacenar un arreglo de registro que almacene la información de los “n”
clientes de una compañía de viajes que adquirieron algún viaje con esa empresa.
De cada cliente se almacena: apellido de cliente, destino del viaje (un número entre 0 y 3)
y la forma de pago (un número entre 0 y 2).

Se desea saber cuántos clientes viajaron a cada destino posible usando cada forma de
pago disponible (es decir: cuántos clientes que viajaron al destino 0 usaron la forma
de pago 0; cuántos clientes que viajaron al destino 0 usaron la forma de pago 1, y
así sucesivamente. En total, se necesitan entonces 4*3 = 12 contadores, pues los
destinos posibles son 4, y las formas de pago posibles son 3).

Items de tarea:
e.) Ordenar el vector de clientes por apellido de manera ascendente.
f.)  Mostrar el vector ordenado.
g.) Buscar un cliente en el vector por apellido de cliente. Informar si se encontró o
no.

'''

import clientes

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def validate_range(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor (entre ' + str(inf) + ' y ' + str(sup)+ '): '))
        if n < inf or n > sup:
            print('Se pidió entre', inf, 'y', sup, '... cargue de nuevo...')
    return n

def read(vector_clientes):
    n = len(vector_clientes)
    for i in range(n):
        ape = input('Ingrese apellido del cliente:')
        dest = validate_range(0, 3)
        f_pago = validate_range(0, 2)
        vector_clientes[i] = clientes.Cliente(ape, dest, f_pago)
    print('Vector cargado')

def display(vector_clientes):
    n = len(vector_clientes)
    print('Datos de los clientes registrados:')
    for i in range(n):
        clientes.write(vector_clientes[i])

def count(vector_clientes):
    conteo = [[0] * 3 for f in range(4)]
    n = len(vector_clientes)
    for i in range(n):
        f = vector_clientes[i].destino
        print(f)
        c = vector_clientes[i].forma_pago
        print(c)
        conteo[f][c] += 1
    return conteo

def display_count(conteo):
    filas, columnas = len(conteo), len(conteo[0])
    print()
    print('Conteo de clientes por destino y forma de pago')
    for f in range(filas):
        for c in range(columnas):
            if conteo[f][c] != 0:
                print('Destino', f, '\tForma', c, '\tCantidad:', conteo[f][c])

def sort(vector_clientes):
    n = len(vector_clientes)
    for i in range(n-1):
        for j in range(i+1, n):
            if vector_clientes[i].apellido > vector_clientes[j].apellido:
                vector_clientes[i], vector_clientes[j] = vector_clientes[j], vector_clientes[i]

def search_binary(vector_clientes, ape):
    # busqueda binaria... asume arreglo ordenado...
    izq, der = 0, len(vector_clientes) - 1
    while izq <= der:
        c = (izq + der) // 2
        if ape == vector_clientes[c].apellido:
            return c
        if ape < vector_clientes[c].apellido:
            der = c - 1
        else:
            izq = c + 1
    return -1


def test():
    # cargar cantidad de clientes...
    print('Cantidad de clientes -', end=' ')
    n = validate(0)
    print()
    # crear y cargar los arreglos paralelos...
    vector_clientes = n * [None]

    # menú de opciones..
    opc = 0
    while opc != 8:
        print('\nMenu de opciones:')
        print('1. Cargar vector de clientes')
        print('2. Mostrar vector de clientes')
        print('3. Generar matriz de conteo')
        print('4. Mostrar matriz de conteo')
        print('5. Ordenar vector por apellido (ascendente)')
        print('6. Mostrar vector ordenado')
        print('7. Búsqueda de cliente por nombre')
        print('8. Salir')

        opc = int(input('Ingrese su eleccion: '))

        if opc == 1:
            read(vector_clientes)
            print()
        elif opc == 2:
            # mostrar todos los clientes...
            display(vector_clientes)
            print()
        elif opc == 3:
            # contar por destino y forma de pago...
            conteo = count(vector_clientes)
        elif opc == 4:
            # mostrar por pantalla el listado...
            display_count(conteo)
        elif opc == 5:
            # ordenamiento de vector
            sort(vector_clientes)
        elif opc == 6:
            # mostrar vector de clientes..
            display(vector_clientes)
        elif opc == 7:
            ape = input('Ingrese el apellido del cliente que desea buscar:')
            ind = search_binary(vector_clientes, ape)
            if ind != -1:
                print('Apellido encontrado!! esta en la posición', ind)
            else:
                print('No se encontró registrado el apellido buscado!')
        elif opc == 8:
            print('Programa finalizado!!')


if __name__ == '__main__':
    test()
