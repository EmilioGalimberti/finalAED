__author__ = 'Catedra AED'

'''Una empresa de venta de artículos de ferretería mantiene información sobre los distintos artículos que tiene a la venta.
Por cada artículo se registran los datos siguientes: número de identificación (un entero), descripción del artículo (una cadena),
precio de venta, precio de compra, país de fabricación (un valor entre 0 y 24 incluidos, por ejemplo: 0: Argentina, 1: Uruguay, etc.),
tipo de artículo (un número entero entre 0 y 29 incluidos, para indicar (por ejemplo): 0: martillo, 1: tornillos, etc.) y su cantidad en stock.
Se pide definir un tipo registro Artículo con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Artículo en un arreglo de registros (cargue n por teclado). Puede cargar los datos manualmente,
o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser
automática). El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los artículos,
 y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la solución
  basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea, pero deben mostrarse solo aquellos registros cuya ganancia
(diferencia entre el precio de venta y el de compra) sea mayor a un valor m indicado por teclado por el usuario.

3- Buscar en el arreglo creado en el punto 1 un registro cuya descripción sea igual al valor d ingresado por el usuario. Si existe,
mostrar por pantalla solamente: el número del artículo, tipo del artículo, y su stock. Si no existe, informar con un mensaje.
El proceso debe deternerse al encontrar el primer registro que cumpla la condición.

4- Determine el stock disponible de los artículos de cada tipo posible y de cada país de fabricación posible (o sea, 25 * 30 acumuladores en
una matriz de acumulación). Muestre sólo los resultados que sean mayores que cero.

5- Guarde en un archivo los registros del arreglo cuyo precio de venta sea menor que el precio promedio entre todos los artículos del vector.

6- Muestre el archivo que creó en el item 5, a razón de un registro por línea en la pantalla.'''

import os
import pickle
import random
from articulos import *

# Desarrollo de funciones
def validar_mayor(inf, mje='Ingrese un valor'):
    n = inf - 1
    while n <= inf:
        n = int(input(mje))
        if n <= inf:
            print("Error, se pidió mayor a ", inf)
    return n

def add_in_order(reg, linea):
    izq, der = 0, len(reg) - 1
    pos = len(reg)
    while izq <= der:
        c = (izq + der) // 2
        if reg[c].identificacion == linea.identificacion:
            pos = c
            break
        if reg[c].identificacion > linea.identificacion:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    reg[pos:pos] = [linea]

# Punto 1
def cargar_registro(n, reg):
    descripcion = ('clavos', 'tornillos', 'arandelas', 'tuercas')
    for i in range(n):
        iden = random.randint(0, 600)
        desc = random.choice(descripcion)
        venta = random.randint(1000, 10000)
        compra = random.randint(500, 5000)
        pais = random.randint(0, 24)
        tipo = random.randint(0, 29)
        stock = random.randint(1, 300)
        linea = Articulo(iden, desc, venta, compra, pais, tipo, stock)
        add_in_order(reg, linea)

# Punto 2
def display_registro(reg, m):
    for num in reg:
        if (num.precio_venta - num.precio_compra) > m:
            print(to_string(num))

# Punto 3
def busqueda(reg, desc):
    for i in range(len(reg)):
        if reg[i].descripcion == desc:
            return i
    return -1

# Punto 4
def generar_matriz(reg):
    # Matriz de acumulacion
    mat = [[0] * 30 for i in range(25)] # 25 filas y 30 columnas, valor de incializacion 0, en esta casilla se iran acumulando #tipo fila pais columa
    for j in range(len(reg)):
        # Acceso directo
        fila = reg[j].tipo
        col = reg[j].pais # reg[j] Es lo que tiene en esa posicion el vector
        # Cargando matriz de acum
        mat[fila][col] += reg[j].stock
        # mat[reg[j].pais][reg[j].tipo] += reg[j].stock
    return mat


def display_matriz(mat):
    fila, columna = len(mat), len(mat[0])
    for i in range(fila):
        for j in range(columna):
            if mat[i][j] > 0:
                print('Pais:', str(i), 'Tipo:', str(j), ' es:', mat[i][j])


def calcular_promedio(reg):
    total = 0
    prom = 0
    for i in range(len(reg)):
        total += reg[i].precio_venta
    prom = total / len(reg)
    return prom


def generar_archivo(reg, fd, prom):
    arch = open(fd, 'wb')
    for num in reg:
        if num.precio_venta < prom:
            pickle.dump(num, arch)
    arch.close()


def display_archivo(fd):
    if not os.path.exists(fd):
        print('ERROR! No se puede leer un archivo que no existe.')
        return

    tam = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < tam:
        registro = pickle.load(m)
        print(to_string(registro))
    m.close()


# funcion principal
def principal():
    fd = 'articulos.dat'
    reg = []
    op = -1
    flag_carga = False

    while op != 7:
        print('\nMenu de Opciones')
        print('1 - Generar Registro')
        print('2 - Mostrar Registro')
        print('3 - Buscar una descripcion')
        print('4 - Generar Matriz de stock')
        print('5 - Generar Archivo')
        print('6 - Mostrar Archivo')
        print('7 - Salir')
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            n = validar_mayor(0, '\nIngrese la cantidad de registros a cargar:')
            cargar_registro(n, reg)
            print('\nRegistro cargado correctamente\n')
            flag_carga = True

        elif op == 2:
            if flag_carga:
                m = int(input('\nIngrese la ganancia a evaluar: '))
                print()
                display_registro(reg, m)
            else:
                print('\nPrimero debe cargar el registro (opcion 1)')

        elif op == 3:
            if flag_carga:
                d = input('\nIngrese la descripcion a buscar: ')
                res = busqueda(reg, d)
                if res != -1:
                    print()
                    print('Nro de identificacion:', reg[res].identificacion,'\n')
                    print('Tipo de articulo:', reg[res].tipo,'\n')
                    print('Stock articulo:', reg[res].stock)
                else:
                    print('\nLa descripcion', d, 'no se encuentra en el registro')
            else:
                print('\nPrimero debe cargar el registro (opcion 1)')

        elif op == 4:
            if flag_carga:
                print()
                mat = generar_matriz(reg)
                display_matriz(mat)
            else:
                print('\nPrimero debe cargar el registro (opcion 1)')
        elif op == 5:
            if flag_carga:
                prom = calcular_promedio(reg)
                generar_archivo(reg, fd, prom)
                print('\nArchivo generado correctamente\n')
            else:
                print('\nPrimero debe cargar el registro (opcion 1)')

        elif op == 6:
            print()
            display_archivo(fd)

        elif op == 7:
            print('\nPrograma finalizado')
        else:
            print('\nOpcion incorrecta')


if __name__ == '__main__':
    principal()

