"""
Turno 2 - Enunciado 1 (T2E1)

Un vivero desea un programa para procesar los datos de las plantas que tiene a la venta. Por cada Planta se tienen los siguientes datos: el número de identificación de la planta, el nombre de la planta, el precio unitario de la planta, cantidad de unidades disponibles en stock y el tipo de especie de la planta (un número entero entre 0 y 18, por ejemplo: 0: Arbusto, 1: Cactus, etc.). Se desea almacenar la información referida a las n plantas que recepta el gimnasio en un arreglo de registros de tipo Planta (definir el tipo Planta y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de las n plantas. Valide que el número identificador de la planta sea positivo y no mayor a 100, y que el tipo de especie sea un valor entre 0 y 18 (ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar en un listado ordenado de menor a mayor por los nombres de las plantas, todos los datos de las plantas cuyo importe de stock (precio unitario multiplicado por la cantidad disponible de dicha planta) sea superior a un valor x, siendo x un valor que se carga por teclado,

3- Determinar y mostrar la cantidad total de plantas disponibles en stock por cada tipo de especie. En total, 19 acumuladores usando un vector de acumulación. Mostrar solo los valores del vector que sean mayores a cero.

4- Determinar y mostrar la cantidad promedio de plantas disponibles que tiene el vivero. Si ese promedio es menor a un valor x (siendo x un valor que se carga por teclado), informe con un mensaje que debe realizarse un control de stock de las plantas.

5- Determinar si existe una planta cuyo número de identificación sea igual a x, siendo x un valor que se carga por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.
"""

from Funciones import *
from Plantas import *


def menu():
    print("\nMenú de opciones: ")
    print("1. Cargar arreglo de plantas")
    print("2. Mostrar datos ordenados de menor a mayor (nombre)")
    print("3. Cantidad de plantas disponibles")
    print("4. Cantidad promedio de plantas")
    print("5. Identificacion de planta")
    print("6. Salir")
    return


def main():
    plantas = None
    opcion = 0

    while opcion != 6:
        menu()
        opcion = int(input('Ingrese la opcion: '))

        if opcion == 1:

            n = int(input('Ingrese la cantidad de plantas: '))
            plantas = carga_plantas(n)


        elif opcion == 2:
            if plantas:
                ordenar(plantas)
                mostrar_plantas('Todos las plantas disponibles son: ', plantas)
                x = int(input('Ingrese el valor de importe de stock que desea filtrar: '))
                filtrado = filtrar_tipo_importe(plantas, x)
                mostrar_plantas('Plantas que cumplen con la condición: ', filtrado)
            else:
                print('Debe cargar las plantas primero!')


        elif opcion == 3:
            if plantas:
                totales = acumular_disponibles(plantas)
                for i in range(len(totales)):
                    if totales[i] != 0:
                        print('Tipo de Planta: ', i, ' Cantidad disponible', totales[i])
            else:
                print('Debe cargar las plantas primero!')


        elif opcion == 4:
            if plantas:
                promedio = promedio_disponibles(plantas)
                print("Promedio: ", round(promedio, 2))
                x = int(input('Ingrese  un valor para saber si  debe realizarse un control de stock de las plantas: '))

                if promedio < x:
                    print('Debe realizarse un control de stock de las plantas porque su promedio es: ', round(promedio, 2))
                else:
                    print('NO Debe realizarse un control de stock de las plantas porque su promedio es: ', round(promedio, 2))

        elif opcion == 5:
            x = int(input('Ingrese el numero de identifiacion que desea busacar: '))
            encontrado = buscar(plantas, x)
            if encontrado:
                print(to_string(encontrado))
            else:
                print('No se encontro ')


if __name__ == '__main__':
    main()
