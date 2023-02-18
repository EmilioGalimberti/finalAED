__author__ = 'Cátedra AED'

''' Combinación de estructuras: arreglos-registros-archivos.
Desarrollar un programa controlado por menú de opciones, que permita gestionar
un arreglo de registros (puede suponer el mismo tipo Libro que hemos usado como
ejemplo en la clase anterior), y a partir de las opciones del menú proceda a generar
un archivo con los datos del arreglo.
a.) Crear y cargar un arreglo "v" de n registros de tipo Libro (puede hacer esta carga
en forma automática).El arreglo debe mantenerse siempre ordenado por isbn a medida que
se va cargando.No puede cargar el vector y luego aplicar un algoritmo de ordenamiento..
b.) Mostrar el arreglo.
c.) Crear un archivo libros.dat que contenga todos los registros del arreglo original.
Si el archivo ya existía, eliminar su contenido y comenzar desde cero.
d.) Mostrar el contenido del archivo libros.dat.
e.) A partir del archivo generado en el punto c, contar la cantidad de libros por tema y
ubicación 11 * 6 contadores.Para resolver este punto generar una matriz de conteo.
'''

import random
import pickle
import os.path


class Libro:
    def __init__(self, cod, tit, aut, tem, ubi):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut
        self.tematica = tem # Valores posibles 0 y 10.
        self.ubicacion = ubi # Valores permitidos entre 0 y 5 (estante).

def display(libro):
    print('ISBN:', libro.isbn, end='')
    print(' - Título:', libro.titulo, end='')
    print(' - Autor:', libro.autor, end='')
    print(' - Temática', libro.tematica, end='')
    print(' - Ubicación', libro.ubicacion)

def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup)+ ' : '))
        if n < inf or n > sup:
            print('\t\tError... cargue de nuevo...')
    return n

# Ordenamiento de menor a mayor.
def add_in_order(v, lib):
    n = len(v)
    pos = n
    for i in range(n):
        if lib.isbn < v[i].isbn:
            pos = i
            break
    v[pos:pos] = [lib]

'''La misma función add_in_order pero con búsqueda binaria..
def add_in_order(v, lib):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].isbn == lib.isbn:
            pos = c
            break
        if lib.isbn < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1
        print('izq', izq)
        print('der', der)
    if izq > der:
        pos = der
    v[pos:pos] = [lib]
'''

def cargar_arreglo(v, n):
    for i in range(n):
        cod = int(input('Ingrese el código:'))
        tit = input('Ingrese un titulo:')
        aut = input('Ingrese un autor:')
        tem = validar_intervalo(0, 10)
        ubi = validar_intervalo(0, 5)
        lib = Libro(cod, tit, aut, tem, ubi)
        add_in_order(v, lib)

def mostrar_arreglo(v):
    if len(v) == 0:
        print('No hay datos en el arreglo...')
        print()
        return
    print('Los libros registrados son:')
    for libro in v:
        display(libro)
    print()

def crear_archivo_todos(v, fd):
    if len(v) == 0:
        print('No hay datos en el arreglo...')
        print()
        return
    m = open(fd, 'wb')
    # forma 1: si se desea que el archivo contenga un vector...
    # pickle.dump(v, m)
    # forma 2: si se desea que al archivo contenga los registros
    # almacenados uno a uno en forma secuencial...
    for libro in v:
        pickle.dump(libro, m)
    # Otra forma de la version 2..
    # for i in range(len(v)):
        # pickle.dump(v[i], m)
    m.close()
    print('Se creó el archivo', fd, 'con todos los registros del vector')
    print()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    print('Contenido actual del achivo', fd, ':')
    m = open(fd, 'rb')
    # forma 1: si el archivo contenía un vector...
    # v = pickle.load(m)
    # for lib in v:
        #  display(lib)
    #  forma 2: si el archivo contenía registros almacenados
    #  uno a uno en forma secuencial...
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)
    m.close()
    print()

def generar_matriz(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    mat = [[0] * 6 for i in range(11)]
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        fila = lib.tematica
        col = lib.ubicacion
        mat [fila][col]+= 1
    m.close()
    return mat

def mostrar_matriz(mat):
    for i in range(11):
        for j in range(6):
            if mat[i][j] > 0:
                print('La cantidad de libros por temática: ', i , ' y ubicación:', j, 'es: ', mat[i][j])

def test():
    v = []
    fd = 'libros.dat'
    op = -1
    while op != 6:
        print('Procesamiento combinado de arreglos, registros y archivos...')
        print('1. Crear el arreglo de libros (en forma automática)')
        print('2. Mostrar el arreglo de libros')
        print('3. Crear el archivo con TODOS los libros del arreglo')
        print('4. Mostrar el archivo con TODOS los libros')
        print('5. Generar matriz de conteo a partir del archivo y mostrarla..')
        print('6. Salir')
        op = int(input('\t\tIngrese número de opción: '))
        print()

        if op == 1:
            n = int(input('Cuantos libros desea cargar?: '))
            cargar_arreglo(v, n)
        elif op == 2:
            mostrar_arreglo(v)
        elif op == 3:
            crear_archivo_todos(v, fd)
        elif op == 4:
            mostrar_archivo(fd)
        elif op == 5:
            mat = generar_matriz(fd)
            mostrar_matriz(mat)
        elif op == 6:
            print('Fin del programa!!!')

if __name__ == '__main__':
    test()
