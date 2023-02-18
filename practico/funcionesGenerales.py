
#Menu de opciones
def main():
    print("Menu de opciones.")
    opcion = None
    while opcion != 4:
        print('1. Impares multiplos de 3')
        print('2. Primos en un intervalo')
        print('3. Secuencia ordenada')
        print('4. Salir')
        opcion = int(input('Ingrese el numero de la opcion elegida: '))
        # chequeo de la opcion elegida...
        if opcion == 1:
            print('a')
        elif opcion == 2:
            print('b')
        elif opcion == 3:
            print('c')
        elif opcion == 4:
            print('Programa finalizado.')
            break
        elif opcion > 4 or opcion < 0:
            print('Eligio una opcion fuera del rango disponible, introduzca nuevamente')

if __name__ == '__main__':
    main()
