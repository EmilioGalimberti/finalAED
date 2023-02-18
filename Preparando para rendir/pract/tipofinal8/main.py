from funciones import  *

def main():
    option = 0
    array = []
    archivoB = "planes.dat"

    while option != 9:
        print("\nMenu de opciones")
        print("1) Generar archivoB")
        print("2) Mostrar archivo")
        print("3) Generar array")
        print("4) Mostrar array")
        print("5) Buscar  nombre en Array")
        print("6) Buscar clave")
        print("7) Matriz")
        print("8) procesamiento de caracteres")
        print("9)Exit")

        option = int(input("Ingrese la opcion que desea ejecutar: "))

        if option == 1:
            print("Eligio la opcion 1")
            n = int(input('Ingrese la cantidad de planes que desea cargar: '))
            if n != 0:
                generarArchivoB(archivoB , n)
        elif option == 2:
            print('Eligio la opcion 2')
            mostrarArchivo(archivoB)
        elif option == 3:
            print('Eligio la opcion 3')
            p = int(input("ingrese el monto menor: "))
            generarArray(array, archivoB, p)
        elif option == 4:
            print('Eligio la opcion 4')
            if len(array) > 0:
                mostrarArray(array)
        elif option == 5:
            print('Eligio la opcion 5')
            nombre = input("Ingre el nombre que desea buscar: ")
            descrpcion = buscarEnNombre(array, nombre)
        elif option == 6:
            print('Eligio la opcion 6')
            clave = input("Ingre el nombre que desea buscar: ")
            buscarClaveIdent(array, clave)
        elif option == 7:
            print('Eligio la opcion 7')

        elif option == 8:
            print('Eligio la opcion 8')
            procesarCaracteres(descrpcion)

        else:
            print("OPCION INCORECTA")

if __name__ == '__main__':
    main()