#Ej: lectura secuencial de archivo binario
import os.path
import pickle

class Libro:
    def __init__(self,cod,tit,aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut

def display(libro):
    print('ISBN: ', libro.isbn, end='')
    print(' Titulo: ', libro.titulo, end='')
    print(' Autor: ', libro.autor, end='')


def grabar_archivo(fd, n):
    m = open(fd,'wb')
    for i in range(n): #hasta n , cant de registro que quiero crear
        isbn_lib = int(input('Ingrese el ISBN del libro: '))
        tit = input("Ingrese titulo del libro: ")
        aut = input("Ingrese el autor del libro: ")
        lib = Libro(isbn_lib,tit,aut) #registro cargado y guardado en la varibale lib
        pickle.dump(lib,m) #almaceno los registro en un archivo
        #m.close() si estuviera aca dentro solo var a guardar el primero registro
    m.close()
    print('Grabacion finalizada....')

def leer_archivo(fd):
    m = open(fd,'rb')
    tam = os.path.getsize(fd) #para saber tamaño del archivo
    print('Tamaño del archivo: ', tam)
    while m.tell() < tam: #tell() retorna la ubicación actual del “file pointer” Es muy útil para q conocer en qué byte está posicionado un archivo en un momento dado.
        lib = pickle.load(m) #con load el file pointer se mueve automaticamente
        display(lib)
        print('\nValor del puntero: ', m.tell())
    m.close()
    print("Lectura finalizada!!")


def test():
    fd = 'libros.dat' #nombre de archivo
    n = int(input('Ingrese la cantidad de libros a cargar: ')) #en este caso cuanto registro almacenaremos en el grabar archivo

    grabar_archivo(fd, n)

    leer_archivo(fd) #solo contiene el nombre del archivo que quiero leer

if __name__ == '__main__':
    test()
