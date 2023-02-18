'''Se pide desearrolar un programa en python controlado por menu de opciones. Ese menu debe permitir
gestionar las siguientes tarias, siempre usando funciones que acepten parametros y/o retornen valores en cada
situacion en que se considere apropiad:
1. Cargar el arreglo pedido. Validar que el codigo numerico para el tipo de proyecto este efectivamente entre 0 y
14.
2. Mostrar todos los datoas, a razon de un registro por linea en la pantalla.
3. Determinar el monto de honorarios acumulado en cada uno de los 15 tipos posibles de contruccion (un
acumulador de menor a mayor, de acuerdo al monto de honorarios
4. Muestre todos los proyectos cuyo codigo de tipo de proyecto sea diferente de 4. Este listado debe salir
ordenado de menor a mayor, de acuerdo al monto de honorarios
5. Determinar si existe algun dise;o para el cliente cuyo nombre sea igual a x, siendo x una cadena que se carga
por teclado, Si existe, mostrar todos los datos de ese dise;o por pantalla. Si no existem informar'''

from registro import *


def main():
    opcion = 0
    proyectos = []
    pasa_opcion_1 = False

    while opcion != 6:
        opcion = menu()
        if opcion == 1:
            n = mayor_que(0,'Ingrese cantidad de proyectos')
            proyecto = carga_proyectos(n)
            pasa_opcion_1 = True
        elif opcion == 2:
            if pasa_opcion_1:
                listar_proyectos(proyectos)
            else:
                print('Primeor debe cargar los proyectons con la opcion 1 ')
        elif opcion == 3:
            if pasa_opcion_1:
                totales = acumular_honorarios(proyectos)
                for i in  range(len(totales)):
                    if totales[i] != 0 : #evita que se muestren valores con 0
                        print('Honorarios acumulados para el tipo', i , ':$', totales[i])
            else:
                print('Primeor debe cargar los proyectons con la opcion 1 ')
        elif opcion == 4:
            if pasa_opcion_1:
                pass
            else:
                print('Primeor debe cargar los proyectons con la opcion 1 ')
        elif opcion == 5:
            if pasa_opcion_1:
                pass
            else:
                print('Primeor debe cargar los proyectons con la opcion 1 ')


main()
