__author__ = 'Cátedra AED'

''' Combinación de estructuras: arreglos-registros-archivos.
Desarrollar un programa controlado por menú de opciones, que permita gestionar
un archivo que contiene registros (el mismo tipo Libro que hemos usado como
ejemplo anterior), y a partir de las opciones del menú proceda a generar
un vector con los datos del arreglo.
a.) Crear y cargar un archivo con los registros de tipo Libro (puede hacer esta carga
en forma automática).
b.) Mostrar el archivo generado en el punto a.
c.) Crear un vector que contenga todos los registros del arreglo original.
d.) Mostrar el vector generado en el punto c.
'''

import random
import pickle
import os
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

def crear_archivo(fd, n):
    m = open(fd, 'wb')
    for i in range(n):
        cod = random.randint(1, 10000)
        tit = 'Título ' + str(i)
        aut = 'Autor ' + str(i)
        tem = random.randint(0, 10)
        ubi = random.randint(0, 5)
        lib = Libro(cod, tit, aut, tem, ubi)
        pickle.dump(lib, m)
    m.close()
    print('Fin de grabación los registros en el archivo')

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    print('Contenido actual del achivo', fd, ':')
    m = open(fd, 'rb')
    # forma 2: si el archivo contenía registros almacenados
    # uno a uno en forma secuencial...
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)
    m.close()
    print()

def crear_arreglo_todos(fd, v):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print()
        return
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        v.append(lib)
    m.close()
    print('Se generó el vector con TODOS los libros del archivo')

def mostrar_arreglo(v):
    if len(v) == 0:
        print('No hay datos en el arreglo...')
        print()
        return
    print('Visualización completa del vector generado')
    for libro in v:
        display(libro)

def test():
    v = []
    fd = 'libros.dat'
    op = -1
    while op != 5:
        print('Procesamiento combinado de arreglos, registros y archivos...')
        print('1. Crear el archivo de libros (en forma automática)')
        print('2. Mostrar el archivo de libros')
        print('3. Crear el arreglo con TODOS de los datos del archivo')
        print('4. Mostrar el arreglo de libros')
        print('5. Salir')
        op = int(input('\t\tIngrese número de opción: '))
        print()

        if op == 1:
            n = int(input('Ingrese cantidad de libros a cargar:'))
            crear_archivo(fd, n)
        elif op == 2:
            mostrar_archivo(fd)
        elif op == 3:
            crear_arreglo_todos(fd, v)
        elif op == 4:
            mostrar_arreglo(v)
        elif op == 5:
            print('Fin del programa!!!')

if __name__ == '__main__':
    test()
