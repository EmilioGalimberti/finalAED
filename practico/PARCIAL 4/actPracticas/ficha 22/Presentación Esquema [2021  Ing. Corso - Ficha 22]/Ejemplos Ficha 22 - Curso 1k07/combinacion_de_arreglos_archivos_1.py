'''
Combinacion de estrucutras: arreglos-registro-archivos.

Desarrollar un programa controlado por meno de opciones, que permita gestionar
una arreglo de registros ( puede suponer el mismo tipo Libro que hemos usado com ejemplo en la clase anterior), y a partir de las opciones del menu proceda a generar
un archivo con los datos del arreglo.

a) crear y cargar un arreglo "v" de n regegistros de tipo Libro(puede hacer esta carga
en forma automatica). El arreglo debe mantenerse siempre ordenado por isbn a medida que
se vc cargando. No puede cargar el vector y luego aplicar un algoritmo de ordenamiento..
b) mostrar el arreglo
c) crea un archivo libros.dat que contenga todos los registro del arreglo originarl.
si el archivo ya existia eliminar su contenido y comenzar desde cero.
d) mostrar el contendio del archivo.dat
e)A partir del archivo generado en el punto c: contar la cantidad de libros por tema y ubiaccion 11*6 contandors, para resolver este punto generar una matriz de conteo
'''
import os.path
import pickle
import random


class Libro:
    def __init__(self, cod, tit, aut, tem , ubi):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut
        self.tematica = tem # valores entre 0 y 10
        self.ubicacion = ubi # valores entre 0 y 5

def display(libro):
    print('ISBN:', libro.isbn, end='')
    print(' - Título:', libro.titulo, end='')
    print(' - Autor:', libro.autor, end='')
    print(' - Tematica:', libro.tematica, end='')
    print(' - Ubicacion:', libro.ubicacion)

def cargar_arreglo(v,n):
    for i in range(n): #hasta n , cant de registro que quiero crear
        isbn_lib = int(input('Ingrese el ISBN del libro: '))
        tit = input("Ingrese titulo del libro: ")
        aut = input("Ingrese el autor del libro: ")
        tem = random.randint(0,10)
        ubi = random.randint(0,5)
        lib = Libro(isbn_lib,tit,aut, tem, ubi) #creo registro tipo libro y guardado en la varibale lib
        #add_in_order(v,lib)
        v.append(lib)  # voy agregando los registros

def mostrar_arreglo(v):
    if len(v) == 0:
        print('No hay datos en el arreglo...')
        print()
        return
    print('Los libros registrados son: ')
    for libro in v:
        display(libro)
    print()

def crear_archivo_todos(v,fd):
    if len(v) == 0:
        print('No hay datos en el arreglo...')
        print()
        return
    m = open(fd, 'wb')
    # forma 1: si se desea que el archivo contenga un vector...
    # pickle.dump(v, m) #solo si no se necesita ir recuperando registro a registro
    # FORMA 2: so se desea qie al archivo contenga los registros almacenados uno a uno en forma secuencial

    for libro in v: #la variable libro, permite ir recuperando lo que tiene v que serian los registros
        pickle.dump(libro,m)
    # otra forma de la version 2..
    # for i in range(len(v)):
        #pickle.dump(v[i], m)
    m.close()
    print('Se creo el archivo', fd, ' con todos los registros del vector')
    print()

def mostrar_archivo(fd):
    if not os.path.exists(fd):  #validacion existe devuelve True, si encuentra un archivo
        print('El archivo',fd,'no existe...')
        print()
        return
    print('Contenido actual del archivo', fd,' :')
    m = open(fd,'rb')
    #forma 1: si el archivo contenia un vector...
    # v = pickle.load(m)
    # for lib in v:
    #       display(lib)
    #forma 2: si el archivo contenia registros almacenados
    # uno a uno en forma secuencial...
    t = os.path.getsize(fd)
    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)
    m.close()
    print()

def test():
    v = []
    fd = 'libros.dat'
    op = -1
    while op != 6:
        print('Procesamiento combinado de arreglos, registros y archivos...')
        print('1. Crear el arreglo de libros (en forma automatica) ')
        print('2. Mostrar el arreglo de libros) ')
        print('3. Crear el archivo con TODOS los libroes del arreglo ')
        print('4. Mostar el archivo con TODOS los libros ')
        print('5. Generar matriz de conteo a partir del archivo y mostrarla.. ')
        print('6. Salir')
        op = int(input('\t\tIngrese numero de opcion: '))
        print()

        if op == 1:
            n = int(input('Cuantos libros desea cargar?: '))
            cargar_arreglo(v,n)

