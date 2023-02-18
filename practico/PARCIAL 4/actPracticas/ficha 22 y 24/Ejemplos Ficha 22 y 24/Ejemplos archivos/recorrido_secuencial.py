__author__ = 'Catedra AED'

# Ejemplificación: Lectura secuencial de un archivo binario..

import pickle
import os.path

class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut

def display(libro):
    print('ISBN:', libro.isbn, end='')
    print(' - Título:', libro.titulo, end='')
    print(' - Autor:', libro.autor)

def grabar_archivo(fd, n):
    m = open(fd, 'wb')
    for i in range(n):
        isbn_lib = int(input('Ingrese el ISBN del libro:'))
        tit = input('Ingrese titulo del libro:')
        aut = input('Ingrese autor del libro:')
        lib = Libro(isbn_lib, tit, aut)
        pickle.dump(lib, m)
    m.close()
    print('Grabación finalizada...')

def leer_archivo(fd):
    m = open(fd, 'rb')
    tam = os.path.getsize(fd)
    print('Tamaño del archivo:', tam)
    while m.tell() < tam:
        lib = pickle.load(m)
        display(lib)
        print('Valor del puntero:', m.tell())
    m.close()
    print('Lectura finalizada!!')

def test():
    fd = 'libros.dat'
    n = int(input('Ingrese la cantidad de libros a cargar:'))

    grabar_archivo(fd, n)

    leer_archivo(fd)

if __name__ == '__main__':
    test()
