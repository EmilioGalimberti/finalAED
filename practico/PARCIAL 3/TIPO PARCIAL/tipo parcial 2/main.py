from alquiler import *
from funciones import *

def menu():
    print('1- Cargar')
    print('2- Mostrar')
    print('3- Contar')
    print('4- Buscar')
    print('5- Filtrar')
    print('6- Salir')
    return

def main():

    alquileres = None
    opcion = 0

    while opcion != 6:
        menu()
        opcion = int(input('Ingrese la opcion: '))

        if opcion == 1:
            n = int(input('Ingrese la cantidad de alquileres '))
            alquileres = carga_alquileres(n)

        elif opcion == 2:
            if alquileres:
                ordenar(alquileres)
                mostrar_alquileres('Todos los alquieres ingresados son', alquileres)
            else:
                print('Debe cargar los alquileres!')
        elif opcion == 3:
            if alquileres:
                contadores = contar_por_tipo(alquileres)        # se le asigna un valor cuando tiene retorno
                mostrar_vector(contadores)
            else:
                print('Debe cargar los alquileres!')
        elif opcion == 4:
            if alquileres:
                c = input('Ingrese la descripcion a buscar: ')
                x = int(input('Ingrese los dias: '))
                encontrado = buscar(alquileres,c,x)
                if encontrado:
                    print(to_string(encontrado))
                else:
                    print('No se encontro ')
            else:
                print('Debe cargar los alquileres!')
        elif opcion == 5:
            if alquileres:
                x = int(input('Ingrese el tipo a buscar: '))
                z = float(input('Ingrese el importe minimo: '))
                filtrado = filtrar_tipo_importe(alquileres,x,z)
                mostrar_alquileres('Listado de alquileres que cumplen con la condicon',filtrado)
                promedio = promedio_importes(filtrado)
                print('Promedio de importes filtrados ', round(promedio))
            else:
                print('Debe cargar los alquileres!')

    pass


if __name__ == '__main__':
    main()
