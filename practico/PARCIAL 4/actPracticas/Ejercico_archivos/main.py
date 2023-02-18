"""
Una empresa cuenta con 3 sucursales numeradas desde la 0 a la 2, y necesita
gestionar sus gastos por mes. De cada gasto se registra lo siguiente:
- Código
- Descripción
- Mes (1-12)
- Sucursal (0-2)
- Importe

Se necesita hacer lo siguiente, trabajando desde un menú de opciones:

1. Cargar / generar los n registros de gastos en un vector.
2. Mostrar el vector de gastos
3. Generar un archivo binario con aquellos gastos cuyo importe supere cierto valor x (x ingresa el usuario por teclado).
4. Mostrar el archivo
5. Generar una matriz de acumulación a partir del archivo generado en el punto 3,
   que represente el gasto total por sucursal y mes.
6. Mostrar los gastos acumulados en la matriz por sucurusal y mes, para cuando los mismos sean superiores a cero.

"""

import pickle             # Siempre que se usan archivos binarios se importa el módulo pickle
import os.path
from Registro import *
from MisFunciones import *


NOMBRE_ARCHIVO = "Gastos.dat"


def mostrar_menu():
    print("\nMenú de opciones:")
    print("1.Cargar arreglo de gastos")
    print("2.Mostrar arreglo de gastos")
    print("3.Generar archivo de gastos")
    print("4.Mostrar archivo de gastos")
    print("5.Generar matriz de acumulación")
    print("6.Mostrar gastos por sucursal y mes")
    print("0.SALIR")


def generar_gasto_rnd():
    cod = random.randint(1, 9999)
    des = "Descripción_" + str(cod)
    me = random.randint(1, 12)
    suc = random.randint(0, 2)
    imp = round(random.random() * 4000 + 1000, 2)  # importe entre 1000 y 5000
    gas = Gasto(cod, des, me, suc, imp)
    return gas


def add_in_order_gasto(vec, gas):  # Búsqueda Binaria
    n = len(vec)
    pos = n
    izq = 0
    der = n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == gas.codigo:
            pos = c
            break
        if gas.codigo < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [gas]


def mostrar_gastos(vec):
    for gas in vec:
        print(to_string(gas))
        # print(gas) # requiere tener función __str__ en el Class



# -------------------------- FUNCIONES DEL MENÚ ------------------------------



def menu1_genera_arreglo(n):
    vec = []
    for i in range(n):
        gas = generar_gasto_rnd()       # Genera un gasto aleatorio
        add_in_order_gasto(vec, gas)    # Se agrega al vector de forma ordenada
    return vec


def menu2_mostrar_arreglo(vec):
    print()
    titulos = get_titulos()
    tam = len(titulos)
    print(titulos)
    print("" * tam)
    mostrar_gastos(vec)
    print("-" * tam)


def menu3_generar_archivo(vg, x):  # "vg" → Vector Gastos
    arch = open(NOMBRE_ARCHIVO, "wb")       # Asociar el archivo físico con la variable que tiene ....
    for i in range(len(vg)):
        if vg[i].importe > x:           # Si el elemento que estoy viendo del importe es mayor a "x", se graba el registro
            pickle.dump(vg[i], arch)     # 1: ¿Qué grabo? Quiero grabar el casillero completo en el archivo  - 2 ¿Donde lo grabo?: en arch, que es tipo file
    arch.close()


def menu4_mostrar_archivo():
    tam = os.path.getsize(NOMBRE_ARCHIVO)    # Necesito el tamaño para poder leer el archivo
    arch = open(NOMBRE_ARCHIVO, "rb")
    while arch.tell() < tam:                 # Me dice en que lugar del archivo estoy parado en ese momento e inmediatamente dsp del open estoy en el byte cero
        gas = pickle.load(arch)              # Mientras haya algo para leer, lee e imprime
        print(gas)
    arch.close()


def menu5_generar_matriz():
    mat = 3 * [None]
    for i in range(len(mat)):
        mat[i] = 12 * [0.0]       # Generamos una matriz de 3 filas y 12 columnas

    tamanio = os.path.getsize(NOMBRE_ARCHIVO)       # Se abre el archivo en modo lectura y se recorre
    arch = open(NOMBRE_ARCHIVO, "rb")
    while arch.tell() < tamanio:
        gas = pickle.load(arch)
        fil = gas.sucursal
        col = gas.mes - 1
        mat[fil][col] += gas.importe
    arch.close()
    return mat


def menu6_mostrar_matriz(mat):           # Se muestran solamente los elementos de la matriz que sean mayores a cero
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] > 0.0:
                print("Sucursal:" + '{:>3}'.format(i) + "  Mes:" + '{:>3}'.format(j+1), end="")
                print("  Monto:" + '{:>10.2f}'.format(mat[i][j]))


# ================================================================================



def principal():
    mat = None
    vec_gas = []
    opc = -1
    while opc != 0:
        mostrar_menu()
        opc = int(input("Ingrese su elección: "))

        if opc == 1:

            n = cargar_mayor_que(0, "Ingrese la cantidad de gastos: ")
            vec_gas = menu1_genera_arreglo(n)
            print("\nDatos generados!")

        elif opc == 2:

            if len(vec_gas) > 0:
                menu2_mostrar_arreglo(vec_gas)
            else:
                print("\nDebe generar los gastos primero (menu 1)!")

        elif opc == 3:
            if len(vec_gas) > 0:
                x = cargar_mayor_que_f(0.0, "Ingrese monto mínimo de gasto: ")
                menu3_generar_archivo(vec_gas, x)
                print("\nArchivo Generado!")
            else:
                print("\nDebe generar los gastos primero! (menu 1)")

        elif opc == 4:

            if not os.path.exists(NOMBRE_ARCHIVO):
                print("Primero debe generar el archivo! (menu 3)")
            elif os.path.getsize(NOMBRE_ARCHIVO) == 0:
                print("\nEl arhivo esta vacío!")
            else:
                menu4_mostrar_archivo()

        elif opc == 5:
            if not os.path.exists(NOMBRE_ARCHIVO):
                print("\nEl archivo " + NOMBRE_ARCHIVO + " no existe!")
            elif os.path.getsize(NOMBRE_ARCHIVO) == 0:
                print("\nEl archivo " + NOMBRE_ARCHIVO + " está vacío!")
            else:
                mat = menu5_generar_matriz()
                print("\nMatriz generada!")

        elif opc == 6:
            if mat is not None:
                menu6_mostrar_matriz(mat)
            else:
                print("Primero debe generar la matriz!")

        elif opc == 0:
            print("--- Programa finalizado ---")
        else:
            print("\nOpción no válida!")


# script principal
if __name__ == '__main__':
    principal()
