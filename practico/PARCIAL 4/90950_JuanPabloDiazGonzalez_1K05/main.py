"""
Una empresa de venta de artículos de peluquería mantiene información sobre los distintos artículos que tiene a la venta. Por cada artículo se registran los datos siguientes:
- Número de identificación (un entero),
- Descripción del artículo (una cadena),
- Precio de venta,
- País de fabricación (un valor entre 0 y 29 incluidos, por ejemplo: 0: Argentina, 1: Italia, etc.),
- Tipo de artículo (un número entero entre 0 y 49 incluidos, para indicar (por ejemplo): 0: tijeras, 1: secadores de pelo, etc.)
- Y su cantidad en stock (que puede ser cero).

Se pide definir un tipo registro Artículo con los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Artículo en un arreglo de registros (cargue n por teclado). Puede cargar los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática). Valide los campos que sean necesarios. El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor, según el número de identificación de los artículos, y para hacer esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea.

3- Buscar en el arreglo creado en el punto 1 un registro cuyo número de identificación sea igual al valor num ingresado por el usuario. Si existe, mostrar por pantalla solamente el nombre del artículo, el tipo del artículo, y su stock. Si no existe, informar con un mensaje. El proceso debe deternerse al encontrar el primer registro que cumpla la condición.

4- Guarde en un archivo los registros del arreglo cuya cantidad en stock no sea cero.

5- Muestre el archivo que creó en el punto 4, a razón de un registro por línea en la pantalla. Muestre al final del listado una línea adicional en la que se indique el precio promedio de todos los registros que se mostraron.
"""

from funciones import *
from registro import *


def test():
    fd = 'tipo_articulo'
    opcion = - 1
    archivo_creado = False
    while opcion != 6:
        print('\nMenú de opciones')
        print('1. Cargar n Articulos')
        print('2. Mostrar Articulos')
        print('3. Buscar por número de identificación')
        print('4. Generar Archivo para registros del arreglo distintos de stock 0 ')
        print('5. Mostrar archivo de punto 4')
        print('6. Finalizar el programa')

        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            n = int(input('Ingrese la cantidad de articulos que desea generar: '))
            articulos = menu1_generar_arreglo(n)
            print('Se generaron los articulos exitosamente.')


        elif opcion == 2:
            if len(articulos) == 0:
                print('Aun no se cargo ningun articulo ')
            else:
                if opcion == 2:
                    mostrar_articulos(articulos)


        elif opcion == 3:
            num = int(input('Ingrese el nro. de identificacion a buscar: '))
            pos = buscar_lectura(articulos, num)
            if pos == -1:
                print('No existe ninguna lectura con el código', c)
            else:
                print('\n¡Encontrado!')
                display(articulos[pos])
        elif opcion == 4:
            crear_archivo(articulos, fd)
            print('El archivo fue creado exitosamente.')
            archivo_creado = True

        elif opcion == 5:
            if archivo_creado:
                print('Contenido del archivo (en caso de estar vacío no se mostrará ninguna lectura)')
                mostrar_archivo(fd)
            else:
                print('El archivo no puede mostrarse porque aún no se creó.')
        elif opcion == 7:
            print('Programa finalizado.')
            break


if __name__ == '__main__':
    test()
