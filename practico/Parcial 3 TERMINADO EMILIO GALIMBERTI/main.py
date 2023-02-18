__author__ = 'Emilio Galimberti'

'''
Una empresa que vende cruceros, desea un programa para administrar la información de venta de pasajes.
Por cada pasaje se conoce:

pasaporte del pasajero (cadena de caracteres),
nombre completo,
código de destino (100: Bahamas, 101: Bermudas: 102: Puerto Rico, 103: República Dominicana),
código de clase (un número entero entre 1 y 10, por ejemplo: 1: Clase Preferencial, 2: Clase superior, 3: Clase Turista, etc.)
 el monto abonado por el pasaje.

 Se desea almacenar la información referida a los n pasajes en un arreglo de registros de tipo Pasaje (definir el tipo Pasaje y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n pasajes. Valide que el destino y el código de clase se encuentren en el rango correcto.
 Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar los datos de todos los pasajes emitidos ordenados de mayor a menor de acuerdo al monto abonado por el pasaje. Los pasajes deben mostrarse a razón de uno por línea y
mostrando el nombre del destino en lugar de sus códigos.

3- Determine la recaudación acumulada para cada una de las 10 clases posibles (un acumulador por cada clase). Muestre los resultados que sean mayores a cero, y determina y muestre la clase con mayor
recaudación (aquella clase cuyo monto acumulado de ventas es el mayor entre las 10 clases).

4- Mostrar todos los pasajes vendidos que correspondan a la clase 3, cuyo monto sea superior al monto promedio pagado en esa clase.

5- Buscar un pasajero por pasaporte. Si se encuentra, mostrar el mensaje "Pasajero <Nombre>, por favor concurrir a atención al cliente". Si no se encuentra indicar la situación con un mensaje. 
Si existe más de un registro que coincida con el mismo pasaporte, debe mostrar sólo el primero que encuentre.

'''

from registro import *
from funciones import *

def menu():
    print('\nMenú de opciones: ')
    print('1. Cargar arreglo')
    print('2. Datos de pasajes - Mayor a Menor por monto')
    print('3. Recaudacion acumulada para las clases posibles')
    print('4. Pasajes vendidos de clase 3')
    print('5. Buscar pasajero por pasaporte')
    print('6.Salir \t')
    return

def main():
    pasaje = None
    opcion = 0

    while opcion != 6:
        menu()
        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            n = int(input('Ingrese la cantidad de pasajes: '))
            pasaje = carga_pasajes(n)

        elif opcion == 2:
            if pasaje:
                ordenar(pasaje)
                mostrar_pasajes('Pasajes ordenados: ', pasaje)
            else:
                print('Debe cargar los pasajes !')

        elif opcion == 3:
            if pasaje:
                totales = acumular_recaudacion(pasaje)
                for i in range(len(totales)):
                    if totales[i] != 0:
                        print('Clase: ', i, ' recaudacion', totales[i])
                mayor_recaudacion = mayor(totales)
                print("La clase con mayor recaudacion es: ")
                print(round(mayor_recaudacion,2))
            else:
                print('Debe cargar los pasajes !')

        elif opcion == 4:
            if pasaje:
                promedio =promedio_importes(pasaje)
                filtrado = filtrar_tipo_clase(pasaje,promedio)
                mostrar_pasajes('Listado de los pasajes que cumplen con la condicon',filtrado)
            else:
                print('Debe cargar los pasajes !')

        elif opcion == 5:
            if pasaje:
                pasaporte = int(input('Ingrese el pasaporte que desea buscar: '))
                encontrado = buscar(pasaje,pasaporte)
                if encontrado:
                    print('Pasajero', encontrado.nombre, ', por favor concurrir a atención al cliente')
                else:
                    print('No se encontro ')
            else:
                print('Debe cargar los pasajes !')


if __name__ == '__main__':
    main()
