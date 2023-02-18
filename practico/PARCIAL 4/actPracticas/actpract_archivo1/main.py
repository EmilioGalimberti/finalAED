'''
Salon de fiestas
Un salon dedicado a la organizacion de fiestas infantiles nos solicita un sistema para gestionar las reservas de un mes
determinado. De cada reserva de festejo se conoce:

* Numero de reserva(es un dato tipo String)
*Nombre del cumpleañero (String)
* Edad del cumpleañero (0 a 13 años)(es un dato tipo Integer)
* Tipo de servicio solicitado (0:salon - 1. salon y animacion - 2 salon,animacion y comida niños - 3: salon,animacion, comida niños y sorpresitas) (es un dato tipo Integer)
* Cantidad Invitados (Integer)
* Monto (float)

Al iniciar el programa todas las reservas se encuntran almacenadas, en un archivo de texto llamado reservas.csv (el cual es
provisto). Se debe cargar dicho archivo en un arreglo de registros de tipo Reserva. Una vez cargado, programe los siguientes
puntos en un menu de opciones

1. Mostrar el contendio del vector, incluyendo descripcion del tipo de servicios
2. Agregar una nueva reserva al arreglo de registro, con un numero que se ingrese por teclado. Validar que dicho numero
de reserva sea unico y solicitar el resto de los datos.
3. Determinar el monto total que el salon ha obtenido por tipo de servicio (vector de acumulacion). Mostrar los resultados e informar que servicion presenta el mayor monto.
4. Crear un nuevo vectro con todas las reservas donde la edad del cumpleañero sea mayor a un valor x pasado por
    parametro y la cantidad de asistentes mayor  aun valor y tambien pasado por parametro. Mostra el contenido
5. Salir del programa, pero antes de terminar, grabar nuevamente todas las reservas en el archivo reservas.csv (sobrescribr el archivo)
'''
from registro import *

def leer_archivo(nombre):
    archivo = open(nombre, 'r' ) #es lo mismo que rt, solo leer un archivo de texto
    v = []
    for linea in archivo:
        # print(linea, end='') #end es que va hacer despues de la impresion print(line[:-1])
        r = convertir_a_reserva(linea)
        # print(r) en este caso la muestra pero muestra la direccion de memoria
        #print(to_string(r))
        v.append(r) # agregar cada cosa que lea al registro
    archivo.close()
    return v


def mostrar_reservas(reservas):
    for r in reservas:
        print(to_string(r))
    pass





def actualizar_archivo(reservas, nombre):
    archivo = open(nombre, 'w' ) #es lo mismo que rt, solo leer un archivo de texto
    lineas = ''
    for r in reservas:
        lineas += convertir_a_texto(r)
    archivo.write(lineas)
    archivo.close()

def main():
    reservas = leer_archivo('reservas.csv')

    op = 0
    while op != 5:
        print('1- Mostrar reservas')

        op = int(input('Ingrese una opcion: '))

        if op == 1:
            mostrar_reservas(reservas)
        elif op == 5:
            actualizar_archivo(reservas, 'reservas.csv')
            print("fin del programa")
        else:
            print("opcion incorrecta")


if __name__ == '__main__':
    main()
