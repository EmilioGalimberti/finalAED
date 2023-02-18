"""
Un centro de entrenamiento deportivo necesita un programa que le permita operar con los diferentes programas
avanzados que tiene disponibles para los deportistas que entrenan en ese centro. De cada Programa, se tiene una
clave de identificación (una cadena que puede tener dígitos y caracteres), el nombre del entrenador a cargo de ese
programa, la descripción del contenido de ese programa (una cadena con un texto terminado en punto y con palabras
separadas por un blanco. Por ejemplo: “Entrenamiento intensivo en judo para varones de menos de 70 kilos.”, etc.), la
cantidad de deportistas registrados para ese programa (puede valer cero), un número entre 1 y 50 que indica el
deporte para ese programa (por ejemplo: 1: fútbol, 2: basquet, etc.), y otro número pero entre 0 y 9 para indicar el
nivel de entrenamiento ofrecido en ese programa (por ejemplo: 0: de alta competencia, 1: de recuperación, 2: de
competencia inicial, etc.).
En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos:
• En uno de ellos, definir la clase Programa que represente al registro a usar en el programa, y las funciones
básicas para operar con registros de ese tipo.
• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias. Aplique las
validaciones que considere necesarias. El programa debe basarse en un menú de opciones para desarrollar las
siguientes tareas:
1. Generar un archivo binario de registros que contenga los datos de todos los programas disponibles en el centro.
Puede generarlo cargando los datos en forma manual o aleatoria. No se requiere que el archivo permanezca
ordenado mientras se carga, ni tampoco que se ordene de ninguna forma al terminar el proceso. Debe considerar
que esta opción puede ser invocada varias veces a lo largo del programa, y que en cada ejecución pueden
agregarse tantos registros como desee el operador, sin eliminar los datos que ya estaban cargados. Observación:
NO CARGUE LOS DATOS EN UN ARREGLO PARA DESPUÉS GRABARLOS EN EL ARCHIVO: DIRECTAMENTE CARGUE
LOS DATOS EN EL ARCHIVO. SERÁ CONSIDERADA INCORRECTA CUALQUIER SOLUCIÓN BASADA EN GENERAR
PRIMERO UN ARREGLO Y LUEGO GRABAR ESE ARREGLO EN EL ARCHIVO.
2. Muestre el archivo generado, a razón de un registro por línea en la consola de salida. Al final del listado, muestre
una línea adicional en la que se informe cuántos registros se mostraron.
3. A partir del archivo cargado en el punto 1, genere un arreglo de registros con todos los programas del archivo cuya
cantidad de deportistas registrados sea diferente de cero. El arreglo debe mantenerse ordenado de menor a
mayor en tod0 momento durante el proceso de creación, de acuerdo al valor del campo clave de identificación.
Cada vez que esta opción se elija, el arreglo debe volver a crearse desde cero, eliminando los datos que pudiese
contener anteriormente. NO GENERE ESTE ARREGLO DIRECTAMENTE EN LA OPCIÓN 1, AL MISMO TIEMPO QUE
GRABA EL ARCHIVO. DEBE RESOLVER ESTE PEDIDO CON UNA OPCIÓN SEPARADA EN EL MENÚ DE OPCIONES.
4. Muestre el arreglo generado en el punto anterior, a razón de un registro por línea en la pantalla.
5. Determine si existe en el arreglo un programa en el que el nombre del entrenador coincida con el valor nom que
se carga por teclado. Si existe, detenga la búsqueda al primero que encuentre y muestre todos sus datos. Si no
existe, cargue por teclado (o genere en forma aleatoria) un registro nuevo con los datos del programa, asigne el
nombre nom del entrenador en el campo correspondiente, y agregue en el arreglo el nuevo registro, manteniendo
el orden por clave de identificación.
6. Determine si existe en el arreglo un programa en el que la clave de identificación coincida con el valor k que se
carga por teclado. Si existe, muestre sus datos completos y detenga la búsqueda al primero que encuentre. Si no
existe, informe con un mensaje.
7. Determine la cantidad acumulada de deportistas que están registrados para cada uno de los posibles deportes y
por cada nivel posible de entrenamiento (un total de 50 * 10 = 500 acumuladores). Muestre sólo los resultados
que sean mayores a un valor m que se carga por teclado.
8. Cargue por teclado una cadena de caracteres, terminada en punto y con palabras separadas con un blanco según
lo habitual. Determine cuántas palabras de la cadena tienen un número par de caracteres, comienzan con una
vocal y tienen al menos una "t" entre los primeros tres caracteres (un único contador para palabras que cumplan
con los tres criterios al mismo tiempo).
"""
from registro import *
import pickle
import os
import string
import random


def validar_mayor_que(valor, mensaje='Ingrese un numero: '):
    numero = valor
    while numero <= valor:
        numero = int(input(mensaje))
        if numero <= valor:
            print('Error!!! El Numero debe ser mayor que {}'.format(valor))
    return numero


"""
8. Cargue por teclado una cadena de caracteres, terminada en punto y con palabras separadas con un blanco según
lo habitual. Determine cuántas palabras de la cadena tienen un número par de caracteres, comienzan con una
vocal y tienen al menos una "t" entre los primeros tres caracteres (un único contador para palabras que cumplan
con los tres criterios al mismo tiempo).
"""


def add_in_order_bin(v, nuevo):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].clave == nuevo.clave:
            pos = c
        if nuevo.clave < v[c].clave:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [nuevo]


def carga_de_datos(v, n):
    for i in range(n):
        clave = clave_2()
        nombre = ''.join(random.choices(string.ascii_letters, k=25))
        descripcion = generar_descripcion()
        cantidad = random.randint(0, 10)
        deporte = random.randint(1, 50)
        nivel = random.randint(0, 9)
        programa = Programa(clave, nombre, descripcion, cantidad, deporte, nivel)
        v.append(programa)


def crear_archivo(fd):
    m = open(fd, 'wb')
    print('Archivo creado con exito')
    m.close()


def cargar_archivo(fd, v):
    n = len(v)
    m = open(fd, "ab")
    for i in range(n):
        pickle.dump(v[i], m)
    print('Archivo cargado')
    m.close()


def menu():
    cad = 'Menu de Opciones\n' \
          '==============================================\n' \
          '1 ----- Generar archivo binario\n' \
          '2 ----- Mostrar archivo binario\n' \
          '3 ----- Cargar vector\n' \
          '4 ----- Mostrar vector\n' \
          '5 ----- Buscar nombre entrenador\n' \
          '6 ----- Buscar clave de identificacion\n' \
          '7 ----- Cantidad acumulada de deportistas\n' \
          '8 ----- Palabras comienzan con vocal y tienen letra t en tercer digito\n' \
          '0 ----- Salir\n' \
          'Ingrese su opcion: '
    return int(input(cad))


def mostrar_archivo(fd):
    m = open(fd, "rb")
    size = os.path.getsize(fd)
    print("Datos del archivo:\n")
    while m.tell() < size:
        programa = pickle.load(m)
        to_string(programa)
    m.close()


def acumular_por_deportista(v):
    va = [0] * 11
    for reg in v:
        va[reg.deporte] += reg.nivel
    return va


def add_in_order(vector, programa):
    izq, der = 0, len(vector) - 1
    pos = 0

    while izq <= der:
        med = (izq + der) // 2
        if vector[med].clave == programa.clave:
            pos = med
            break

        if programa.clave < vector[med].clave:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [programa]


def cargar_vector(nombre_archivo):
    programas = []
    if not os.path.exists(nombre_archivo):
        print('El archivo', nombre_archivo, 'no existe.')
        return
    m = open(nombre_archivo, 'rb')
    t = os.path.getsize(nombre_archivo)
    while m.tell() < t:
        programa = pickle.load(m)
        if programa.cantidad != 0:
            add_in_order(programas, programa)
    m.close()
    return programas


def mostrar_vector(v):
    n = len(v)
    for i in range(n):
        to_string(v[i])


def buscar_por_nombre(vector, nom):
    for i in range(len(vector)):
        if vector[i].nombre == nom:
            return i
    return -1


def buscar_por_clave(vector, clave):
    for i in range(len(vector)):
        if vector[i].clave == clave:
            return i
    return -1


def generar_matriz(v):
    math = [[0] * 50 for i in range(10)]
    for programa in v:
        f = programa.nivel
        c = programa.deporte
        math[f][c] += 1
    return math


def mostrar_matriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] != 0:
                print("Tipo del progarma:", f, "Deporte:", c, "Nivel:", matriz[f][c])


"""
8. Cargue por teclado una cadena de caracteres, terminada en punto y con palabras separadas con un blanco según
lo habitual. Determine cuántas palabras de la cadena tienen un número par de caracteres, comienzan con una
vocal y tienen al menos una "t" entre los primeros tres caracteres (un único contador para palabras que cumplan
con los tres criterios al mismo tiempo).
"""


def numero_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


def procesar_texto(cadena):
    cl = cont_pal_t_tres_digitos = 0
    tiene_t = False
    cont_pal_numero_par = 0
    for letra in cadena:
        if letra != ' ' and letra != '.':
            cl += 1

            if letra.lower() == 't':
                tiene_t = True
        else:
            if numero_par(cl):
                cont_pal_numero_par += 1
            if ((cl == 1) or (cl == 2) or (cl == 3)) and tiene_t:
                cont_pal_t_tres_digitos += 1

            cl = 0

            tiene_t = False
    print('La cantidad de palabras de las cuales los caracteres de la misma son pares son', cont_pal_numero_par)
    print('La cantidad de palabras que tienen la letra t en los primeros 3 digitos es', cont_pal_t_tres_digitos)


def ordenar_vector(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].clave > v[j].clave:
                v[i], v[j] = v[j], v[i]
    print('Vector ordenado con exito!!')


def principal():
    programas = []
    opcion = -1
    nombre_archivo = 'programa.dat'
    pos = 0
    n = -1
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            crear_archivo(nombre_archivo)
            n = int(input('Ingrese cuantos planes quiere agregar: '))
            carga_de_datos(programas, n)
            cargar_archivo(nombre_archivo, programas)
        if opcion == 2:
            mostrar_archivo(nombre_archivo)
        elif opcion == 3:
            programas = cargar_vector(nombre_archivo)
            print('Vector generado con éxito.')
        elif opcion == 4:
            mostrar_vector(programas)
        elif opcion == 5:
            nom = input('Ingrese el nombre')
            pos = buscar_por_nombre(programas, nom)
            if pos != -1:
                to_string(programas[pos])
            else:
                print('No existe un programa con el nombre {}'.format(nom))
                clave = clave_2()
                nombre = nom
                descripcion = generar_descripcion()
                cantidad = random.randint(0, 10)
                deporte = random.randint(1, 50)
                nivel = random.randint(0, 9)
                nuevo_nom = Programa(clave, nombre, descripcion, cantidad, deporte, nivel)
                programas.append(nuevo_nom)
                print('El nombre ha sido agregado exitosamente')
        elif opcion == 6:
            k = input('Ingrese clave id')
            pos = buscar_por_clave(programas, k)
            if pos != -1:
                to_string(programas[pos])
            else:
                print('No existe un programa con la clave de identificación {}'.format(k))
        elif opcion == 7:
            matriz = generar_matriz(programas)
            mostrar_matriz(matriz)
        elif opcion == 8:
            cadena = input('Ingrese texto a procesar')
            procesar_texto(cadena)
        else:
            print('Gracias por usar el programa del centro deportivo')


if __name__ == '__main__':
    principal()
