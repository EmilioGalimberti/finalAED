from funciones import *


def main():
    fd = 'proyectos.dat'
    reg = []  # Definido de manera global, por eso no hace falta un return en la carga
    op = -1
    flagCarga = False
    flagArchivo = False
    flagCadena = False

    while op != 9:
        print('\nMenu de opciones')
        print('1- Generar registro')
        print('2- Mostrar registro')
        print('3- Generar arhivo con tipos de proyectos != 1 and !=0')
        print('4- Muestra archivo')
        print('5- Buscar proyecto por numero de identifcacion')
        print('6-Concatenacion de los objetivos')
        print('7- Generar y mostrar matriz de conteo')
        print('8- Analisis cadena')
        print('9- Finalizar progama')
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            n = validarMayor('\nIngrese la cantidad de registros a cargar:')
            cargaRegistro(n, reg)
            print('\nRegistro cargado correctamente\n')
            flagCarga = True


        elif op == 2:
            if flagCarga:
                displayRegistro(reg)
            else:
                print('\nPrimero debe cargar el registro')


        elif op == 3:
            if flagCarga:
                promedio = generarArchivo(reg, fd)
                print('\nArchivo generado correctamente')
                flagArchivo = True
            else:
                print('\nPrimero debe cargar el registro')


        elif op == 4:
            if flagArchivo:
                mostrarArchivo(fd, promedio)
            else:
                print('\nPrimero debe generar un archivo')


        elif op == 5:
            if flagCarga:
                b = int(input('\nIngrese el numero de identficacion que desea buscar '))
                pos = busqueda(reg, b)
                if pos == -1:
                    print('\nEl numero de identficacion ', b, 'No se encuentra')
                else:
                    print('\nEl registro que coincide con el numero de identifcacion buscado es:')
                    mostrar(pos)  # Difrencias mostrar(reg[pos])

            else:
                print('\nPrimero debe generar un archivo')


        elif op == 6:
            if flagCarga:
                cadena = cadenas(reg)
                print('El resultado de la cadena seria: ', cadena)
                flagCadena = True
            else:
                print('\nPrimero debe cargar el registro')


        elif op == 7:
            if flagCarga:
                conteo = matrizConteo(reg)
                displayCount(conteo)

        elif op == 8:
            if flagCadena:
                punto8_digitosVocales(cadena)
            else:
                print('\nPrimero debe generar la cadena en el punto 6')
        elif op == 9:
            print('\nPrograma finalizado')
        else:
            print('\nOpcion incorrecta')


# Recordar porque era esto
if __name__ == '__main__':
    main()
