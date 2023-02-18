''' Enunciado: Ejercicio de integración: registros-vectores-matrices-archivos
 Un equipo de competición del “Super Byke” (carreras de motos) está probando una
 nueva moto de carrera. Durante esta prueba la motocicleta tiene sensores que emiten
 información cada vez que la misma pasa frente al puesto de control. Usted debe
 desarrollar un programa Python que permita cargar y gestionar esta información.
 Por cada lectura de los sensores se tiene:
  código de lectura (un valor entero),
 estado del motor (un valor entero comprendido entre 1 y 8 ambos inclusive),
 estado de frenos (un valor entero comprendido entre 1 y 20 ambos inclusive),
 consumo de combustible (un valor float)
 y descripción general (un string).
 Se pide definir el tipo Lectura con los campos indicados, y desarrollar un programa en Python
 controlado por un menú de opciones que permita gestionar las siguientes tareas:

 1- Cargar un arreglo de registros con los datos de n lecturas. Valide que el estado
 del motor y el estado de los frenos estén dentro de los valores descriptos. Puede cargar
 los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual,
 TODA la carga debe ser manual, y si la hace automática entonces TODA debe ser automática).
 El arreglo debe crearse de forma que siempre quede ordenado de menor a mayor por código de
 lectura. Para esto debe utilizar el algoritmo  inserción ordenada con búsqueda binaria.
 Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y
 ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

 2- Mostrar el contenido completo del vector a razón de un registro por línea.

 3- Cargar desde teclado una variable c con un código de lectura y buscar y mostrar
 un registro cuyo código de lectura coincida con c. Si no lo encuentra, mostrar un mensaje
 avisando de esta situación. La búsqueda debe detenerse al encontrar el primer registro que
 coincida con el criterio de búsqueda.

 4- A partir del vector de registros, genere una matriz para acumular el consumo de
 combustible por cada estado del motor y por cada estado de los frenos (matriz de
 acumulación de 8 * 20 acumuladores). Puede colocar los estados de motor como fila
 y los estados de freno como columnas. Muestre el contenido de toda la matriz.

 5- A partir del vector, generar un archivo binario que contenga los registros donde
 el estado del motor sea 2, 5 o 7.

 6- Mostar el contenido completo del archivo a razón de un registro por línea.'''

from lectura import *
import pickle
import os.path

# Funciones de validación
def mayor_que(valor, mensaje='Ingrese un número'):
    n = valor - 1
    while n <= valor:
        n = int(input(mensaje))
        if n <= valor:
            print('¡Error! El valor debe ser mayor a', valor)
    return n

def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup)+ ' : '))
        if n < inf or n > sup:
            print('\t\tError... cargue de nuevo...')
    return n

# Implementación de funciones..
'''def add_in_order(v, lectura):# 1 2 3
    n = len(v)
    pos = n
    for i in range(n):
        if lectura.cod < v[i].cod:  cod es lo que quiere ingresar // busqueda secuencial para encontrar la pos
            pos = i                    para hacer de mayor  amenor solo cambio el signo
            break

    v[pos:pos] = [lectura]
'''
'''Repaso de búsqueda binaria
def busqueda_binaria(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            pos = c
            return pos 
        elif x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1
'''
# Opcion 1 ------------------------------------------------------------------------------
def add_in_order(v, lectura):# 1 2 3
    izq, der = 0, len(v) - 1
    pos = len(v)
    while izq <= der:
        c = (izq + der) // 2

        if lectura.cod == v[c].cod:
            pos = c
            break
        elif lectura.cod < v[c].cod:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [lectura]


def carga_manual(v, n):
    print('-'*50)
    for i in range(n):
        print('Lectura n°' + str(i+1))
        codigo = mayor_que(0, 'Ingrese el codigo: ')
        print('Ingrese el estado del motor')
        motor = validar_intervalo(1, 8)
        print('Ingrese el estado de los frenos')
        frenos = validar_intervalo(1, 20)
        consumo = float(input('Ingrese el valor del consumo:'))
        consumo = round(consumo, 2)
        desc = input('Ingrese la descripción: ')

        lectura = Lectura(codigo, motor, frenos, consumo, desc) #registro lectura
        add_in_order(v, lectura)

# Opcion 2 ------------------------------------------------------------------------------
def mostrar_lecturas(v):
    for i in range(len(v)):
        display(v[i])

# Opcion 3 ------------------------------------------------------------------------------
def buscar_lectura(v, codigo):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if codigo == v[c].cod:
            pos = c
            return pos
        elif codigo < v[c].cod:
            der = c - 1
        else:
            izq = c + 1
    return -1

# Opcion 4 ------------------------------------------------------------------------------
def generar_matriz(v):
    m = [[0] * 20 for i in range(8)]
    for i in range(len(v)):
        fila = v[i].est_mot
        col = v[i].est_fr
        # Acceso directo...
        m[fila-1][col-1] += v[i].cons
    return m

def mostrar_matriz(m):
    for f in range(len(m)):
        for c in range(len(m[0])):
            if m[f][c] > 0:
                print('Mat[' + str(f+1) + '-' + str(c+1) + ']:  ', m[f][c])


# Opcion 5 ------------------------------------------------------------------------------
def crear_archivo(v, fn):
    m = open(fn, 'wb')
    for lectura in v:
        if lectura.est_mot in (2, 5, 7):
            pickle.dump(lectura, m)
    m.close()

# Opcion 6 ------------------------------------------------------------------------------
def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print('El archivo no existe!!')
        return
    m = open(fd, 'rb')
    tam = os.path.getsize(fd)
    while m.tell() < tam:
        lectura = pickle.load(m)
        display(lectura)
    m.close()

def test():
    v = []
    fd = 'lecturas.dat'
    arch_creado = False

    opcion = - 1
    while opcion != 7:
        print('Menú de opciones')
        print('1. Cargar n lecturas')
        print('2. Mostrar lecturas')
        print('3. Buscar lectura por código')
        print('4. Consumo de combustible por cada estado del motor y de los frenos')
        print('5. Crear un archivo con estado del motor 2, 5 o 7')
        print('6. Mostrar archivo')
        print('7. Finalizar el programa')

        opcion = int(input('Ingrese una opción: '))
        print()

        if opcion == 1:
            n = mayor_que(0, 'Ingrese la cantidad de lecturas que desee cargar: ')
            carga_manual(v, n)
            print('Se cargaron las lecturas exitosamente.')

        else:
            if len(v) == 0:
                print('Aún no se cargó ninguna lectura.')
            else:
                if opcion == 2:
                    mostrar_lecturas(v)

                elif opcion == 3:
                    c = int(input('Ingrese el código de lectura a buscar: '))
                    pos = buscar_lectura(v, c)
                    if pos == -1:
                        print('No existe ninguna lectura con el código', c)
                    else:
                        print('\n¡Encontrado!')
                        display(v[pos])

                elif opcion == 4:
                    m = generar_matriz(v)
                    mostrar_matriz(m)

                elif opcion == 5:
                    crear_archivo(v, fd)
                    print('El archivo fue creado exitosamente.')
                    arch_creado = True

                elif opcion == 6:
                    if arch_creado:
                        print('Contenido del archivo (en caso de estar vacío no se mostrará ninguna lectura')
                        mostrar_archivo(fd)
                    else:
                        print('El archivo no puede mostrarse porque aún no se creó.')
                elif opcion == 7:
                    print('Programa finalizado.')
                    break

if __name__ == '__main__':
    test()
