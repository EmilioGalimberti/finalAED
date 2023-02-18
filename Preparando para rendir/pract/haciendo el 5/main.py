from funciones import *


def main():
    option = 0
    array = []
    archivoB = "deportistas.dat"
    while option != 9:
        print('\nMenu de opciones:')
        print('1) Generar Array')
        print('2) Mostrar Array ')
        print('3) Monto acumulado por Becas ')
        print('4)  ')
        print('5) Busqueda por nombre en array ')
        print('6) Generar archivo binario  ')
        print('7) Mostrar archivo binario ')
        print('8) Exit  ')
        option = int(input("Ingrese la opcion que desea utilizar: "))

        if option == 1:
            print('\nEligio la opcion 1:')
            n = int(input("Ingrese la cantidad de deportista que desea cargar: "))
            if n>0:
                generarArray(array, n)
                print("array generado")
            else:
                print("ingrese un calor valido de deporitstas")
        elif option == 2:
            print('\nEligio la opcion 2:')
            if len(array) > 0:
                mostrarArray(array)
            else:
                print("Primero debe cargar deportista al array")
        elif option == 3:
            print('\nEligio la opcion 3:')
            if len(array) > 0:
                array_acumulacion  = array_acumlacion(array)
                for i in range(len(array_acumulacion)):
                    if array_acumulacion[i] != 0:
                        print("para el tipo beca ",i ,"el monto total es: ", array_acumulacion[i])
            else:
                print("Primero debe cargar deportista al array")
        elif option == 4:
            print('\nEligio la opcion 4:')
            m = matriz_conteo(array)
            mostrar_matriz(m)
        elif option == 5:
            print('\nEligio la opcion 5:')
            if len(array) > 0:
                nombre = input("Ingrese le nombre que desea busca: ")
                busquedaSecuencial(array, nombre)
            else:
                print("Primero debe cargar deportista al array")
        elif option == 6:
            print('\nEligio la opcion 6:')
            if len(array) > 0:
                generarArchivoB(array,archivoB)
            else:
                print("Primero debe cargar deportista al array")
        elif option == 7:
            print('\nEligio la opcion 7:')
            mostrarArchivo(archivoB)
        elif option == 8:
            print("\nEXIT")
        else:
            print('\nIngreso una opcion incorrecta')


if __name__ == '__main__':
    main()


