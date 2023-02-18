'''Una empresa de venta de artículos de pesca deportiva mantiene información sobre los distintos artículos que tiene a la venta. Por cada artículo se registran los datos siguientes:

 >> número de identificación (un entero),

 >> descripción del artículo (una cadena),

 >> precio de venta,

 >> lugar de origen del artículo (un valor entre 0 y 24 incluidos, por ejemplo: 0: Argentina, 1: Canadá, etc.)

 >> tipo de artículo (un número entero entre 0 y 29 incluidos, para indicar (por ejemplo): 0: anzuelo, 1: caña, etc.)

 Se pide definir un tipo registro Articulo con los campos que se indicaron, y un programa completo con menú de opes para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Articulo en un arreglo de registros (cargue n por teclado). Valide los campos que sea necesario. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los artículos, y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea.


Muestre solo los registros cuyo lugar de origen sea diferente del valor p que se carga por teclado.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación del artículo sea igual a num (cargar num por teclado).
Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe, informar con un mensaje. La búsqueda debe detenerse al encontrar el primer
registro que coincida con el patrón pedido.

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros cuyo tipo no sea igual al valor tip que se
carga por teclado.

5- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla. Muestre al final del listado dos líneas adicionales:
una con la cantidad de registros que se mostraron, y otra con el precio de venta promedio de todos los registros que se mostraron.

'''


from funciones import*
from registro import *

def principal():
    fd = 'tipo_articulo'
    op = - 1
    archivo_creado = False
    while op != 6:
        print('\nMenú de Opciones')
        print('1. Generar artículos: ')
        print('2. Mostrar registro de artículos: ')
        print('3. Buscar registro por número de identificación: ')
        print('4. Generar archivo de registros diferentes a "tip": ')
        print('5. Mostrar archivo - cantidad de registros y precio promedio: ')
        print('6. Finalizar el programa')

        op = int(input('Ingrese una op: '))

        if op == 1:
            n = int(input('Ingrese la cantidad de articulos que desea generar: '))
            articulos = generar_arreglo(n)
            print('Se generaron los articulos exitosamente.')

        elif op == 2:
            if len(articulos) == 0:
                print('Primero debe cargar los archivos')
            else:
                if op == 2:
                    p = int(input('Ingrese que pais de origen no desea ver: '))
                    mostrar_articulos(articulos,p)


        elif op == 3:
            num = int(input('Ingrese el número de identificacion deseado: '))
            pos = buscar_articulo(articulos, num)
            if pos == -1:
                print('No existe ninguna lectura con el código')
            else:
                print('\n¡Se ha encontrado!')
                mostrar(articulos[pos])
        elif op == 4:
            tip = int(input('Ingrese que tipo de articulos no desea guardar entre 0 y 49 '))
            crear_archivo(articulos, fd,tip)
            print('>> Su archivo fue generado.')
            archivo_creado = True

        elif op == 5:
            if archivo_creado:
                print('Contenido del archivo: ')
                mostrar_archivo(articulos,fd)
            else:
                print('El archivo aún no ha sido generado.')
        elif op == 7:
            print('Programa finalizado.')
            break


if __name__ == '__main__':
    principal()

