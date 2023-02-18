from funciones import *

def main():
    v = []
    op = -1
    flagCarga = False

    while op != 9:
        print('\nMenu de opciones')
        print('1- Generar registro')
        print('2- Mostrar registro')

        print('9- Finalizar progama')
        op = int(input('Ingrese una opcion: '))
        if op == 1:
            n = validarMayor('\nIngrese la cantidad de registro a cargar')
            cargaRegistro(n, v)
            print('\nRegistro cargado correctamente')
            flagCarga = True

        elif op == 2:
            if flagCarga:
                displayRegistro(v)
            else:
                print('nope')


        elif op == 9:
            print('programa finalizado')
        else:
            print('opcion incocrrecta')

if __name__ == '__main__':
    main()
