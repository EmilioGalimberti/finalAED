__author__ = 'Catedra AED'

'''
Un coto de caza ha solicitado un programa para procesar los datos de los clientes que han asistido al predio para
practicar la caza en ambientes controlados y permitidos. Por cada Cliente se conoce su nombre, cantidad de acompañantes,
tipo de trofeo de caza (un valor del 0 al 14) que obtuvo y el precio total que debe abonar. Se desea almacenar la
información referida a los n clientes en un arreglo de registros de tipo Cliente (definir el tipo Cliente y cargar n
por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones,  que permita gestionar las siguientes
tareas:

1) Cargar el arreglo con los datos de los n clientes. Valide que el precio total a abonar sea mayor a cero y que el tipo de
trofeo de caza esté en el rango especificado. Puede hacer la carga en forma manual, o puede generar los datos en forma
automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2) Mostrar todos los datos de todos los clientes, en un listado ordenado de menor a mayor, según el precio a pagar.

3) Determinar el total que se ganó por cada tipo de pieza de trofeo, 15 acumuladores en total con un vector de acumulacion.

4) Determinar y mostrar los datos del cliente con mayor cantidad de acompañantes.
Si ese cliente pagó un precio inferior al valor p que se carga por teclado, cargar un nuevo
precio, asignarlo en el registro del cliente, y volver a mostrar sus
datos.

5) Determinar si existe un cliente cuyo nombre sea igual x, siendo x un valor que se carga por teclado. Si existe, mostrar
sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de
búsqueda, debe mostrar sólo el primero que encuentre.
'''

import random
from clientes import *

def validate(inf, mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def cargar_vector(n):
    v = [None] * n
    for i in range(n):
        nom = random.choice(['Pedro', 'Pablo', 'Juan', 'Luz', 'María', 'Mario', 'José', 'Carmen', 'Lucas', 'Lucía',
                             'Luis', 'Ramón', 'Carla', 'Nahuel'])
        acomp = random.randint(0, 10)
        trof = random.randint(0, 14)
        precio = random.randint(1000, 9000)
        v[i] = Cliente(nom, acomp, trof, precio)
    return v


def mostrar_vector(vec_clientes):
    n = len(vec_clientes)
    for i in range(n):
        write(vec_clientes[i])


def ordenar(vec_clientes):
    n = len(vec_clientes)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec_clientes[i].precio_tot > vec_clientes[j].precio_tot:
                vec_clientes[i], vec_clientes[j] = vec_clientes[j], vec_clientes[i]


def mayor_acomp(vec_clientes):
    band = True
    for i in range(len(vec_clientes)):
        if band:
            may = vec_clientes[i]
            band = False
        elif vec_clientes[i].acomp > may.acomp:
            may = vec_clientes[i]
    return may


def buscar_nombre(vec_clientes, nom):
    for i in range(len(vec_clientes)):
        if vec_clientes[i].nombre == nom:
            return i
    return -1


def acumular_precios(vec_clientes):
    acum = [0] * 15
    for i in range(len(vec_clientes)):
        acum[vec_clientes[i].tipo_trofeo] += vec_clientes[i].precio_tot
    return acum

def principal():
    print('¡Bienvenid@!')
    op = -1
    generado = False

    while op != 0:
        print('\n>>> Menú de opciones:')
        print('     1) Generar clientes.')
        print('     2) Mostrar datos de clientes.')
        print('     3) Mostrar total de dinero por tipo de trofeo.')
        print('     4) Modif. precio del cliente con más acompañantes.')
        print('     5) Buscar cliente.')
        print('     0) Salir.')

        op = int(input('Ingrese una opción del menú:'))

        if op == 1:
            print('\nGenerar clientes.')
            n = validate(0,'Ingresar cantidad de clientes a generar')
            vec_clientes = cargar_vector(n)
            generado = True

        elif generado:

            if op == 2:
                print('\nListado de clientes:')
                ordenar(vec_clientes)
                mostrar_vector(vec_clientes)

            elif op == 3:
                print('\nCantidad de dinero por tipo de trofeo:')
                acumulador = acumular_precios(vec_clientes)
                for i in range(len(acumulador)):
                    print('Tipo de trofeo: ' , str(i) , 'Dinero total conseguido: $' , acumulador[i])


            elif op == 4:
                mayor = mayor_acomp(vec_clientes)
                print('\nCliente con mayor cant. de acompañantes:')
                write(mayor)
                p = float(input('Ingresar un precio mínimo $:'))
                if mayor.precio_tot < p:
                    nuevo_precio = float(input('Ingresar un nuevo precio $:'))
                    mayor.precio_tot = nuevo_precio
                    print('Precio total modificado en base al mínimo ingresado.')
                    write(mayor)
                else:
                    print('El precio mínimo es menor al precio existente. No se realizaron modificaciones.')

            elif op == 5:
                print()
                nom = input('Ingrese nombre del cliente a buscar: ')
                ind = buscar_nombre(vec_clientes, nom)
                if ind != -1:
                    print('Cliente encontrado:')
                    write(vec_clientes[ind])
                else:
                    print('No se ha encontrado cliente con ese nombre.')

        else:
            print('¡Debe seleccionar la opción 1 antes de continuar con las demás opciones!')


if __name__ == '__main__':
    principal()

