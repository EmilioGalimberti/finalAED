from funciones import *

def main():
    opcion = 0
    array = []
    archivoB = 'Pacientes.dat'
    array2 = []

    while opcion != 8:
        print('\nMenu de opciones: ')
        print('1) Generar array ')
        print('2) Mostrar array')
        print('3) Generar array2 monto != 0 && beca != 1 ')
        print('4) Matriz')
        print('5) Buscar pon nombre en el array2')
        print('6) ')
        print('7) ')
        print('8) EXIT')

        opcion = int(input('Ingrese la opcion que desea ejecutar: '))

        if opcion == 1:
            print('Eligio la opcion 1: ')
            n = int(input('Ingrese la canitdad de pacientes que desea cargar: '))
            if n > 0:
                generarArray(array, n)
            else:
                print('Ingrese una opcion valida')
        elif opcion == 2:
            print('Eligio la opcion2: ')
            if len(array) > 0:
                mostraArray(array)
            else:
                print("primero debe cargar un paciente")
        elif opcion == 3:
            print('Eligio la opcion3: ')
            if len(array) > 0:
                array2 = generarArray2(array)
            else:
                print("primero debe cargar un paciente")
        elif opcion == 4:
            print('Eligio la opcion4: ')
        elif opcion == 5:
            print('Eligio la opcion5: ')
            nombre = input('Ingrese el nombre que desea buscar: ')
            if len(array2) > 0 :
                buscarPorNombre(array2, nombre)
            else:
                print("primero debe generar el segundo array")
        elif opcion == 6:
            print('Eligio la opcion6: ')
            genararArchivoB(archivoB, array2)
        elif opcion == 7:
            print('Eligio la opcion7: ')
            mostrarArchivob(archivoB)
        else:
            print("Eligio una opcion incorrecta")


if __name__ == '__main__':
    main()