import random

from funciones import *

def main():
    option = 0
    array = []
    archivoB = 'archivoProgramas.dat'
    while option != 9:
        print('-'*60)
        print('\nMenu de opciones:')
        print("1. Generar archivo")
        print("2. Mostrar registros y la cantidad de registros")
        print("3. Generar arreglo")
        print("4. Mostrar arreglo")
        print("5. Buscar programa por nombre")
        print("6. Buscar programa por clave")
        print("7. Generar y mostrar matriz")
        print("8. Procesamiento de caracteres")
        print("9. Salir")
        print("-" * 60)

        option = int(input('Ingrese La opcion que desea: '))
        if option == 1:
            print('Eligio La opcion 1: ')
            cantProgramas = int(input('\n Ingrese la cantidad de programas que desaea cargar en el archivo: '))
            if cantProgramas > 0:
                generarArhvioB(archivoB,cantProgramas)
            else:
                print('\nNo se cargara ningun programa.')
        elif option == 2:
            contador = mostrarArchivo(archivoB)
            print('\n La cantidad de registros mostrados es de: ', contador)
        elif option == 3:
            genararArray(array,archivoB)
        elif option == 4:
            mostrarArray(array)
        elif option == 5:
            nombre = input("Ingrese el nombre que desea buscar: ")
            pos = busquedaSecuencial(array, nombre)
            if pos != -1:
                print("-" * 160)
                print(titulos())
                print("-" * 160)
                print(array[pos])
        elif option == 6:
            k = int(input("Ingrese la clave que desea buscar: "))
            busquedaIdentificacion(array, k)
        elif option == 7:
            if len(array) != 0:
                m = validar_mayor_que(0, "Ingrese la cantidad minima: ")
                matriz = generar_matriz(array)
                mostrar_matriz(matriz, m)
            else:
                print("No se han cargado datos...")
        elif option == 8:
            texto = input("Ingres un texto terminado en .")
            contPalabras =procesamientoTexto(texto)
            print("Cantidad de palabras que cumplen las 3 condiciones", contPalabras)
        else:
            print('Opcion invalida')


if __name__ == '__main__':
    main()

