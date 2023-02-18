from Registro import *
import random
import pickle
import os
import string
""" Un centro de entrenamiento deportivo necesita un programa que le permita operar con los diferentes programas
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
mayor en todo momento durante el proceso de creación, de acuerdo al valor del campo clave de identificación.
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

# 1)
def validar_mayor_que(inferior, mensaje):
    numero = inferior
    while numero <= inferior:
        numero = int(input(mensaje))
        if numero <= inferior:
            print("Valor incorrecto!")
    return numero
def generar_clave():
    palabra = ""
    for i in range(5):
        palabra += random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + str(random.randint(100, 999))
    return palabra
def generar_nombre():
    nombres = ("Benjamin", "Isabella", "Martina", "Catalina", "Bautista", "Sofia", "Olivia", "Felipe",  "Octavio", "Jonás", "Geronimo", "Teo", "Abril", "Tobias", "Gino")
    res = random.choice(nombres)
    return res
def generar_descripcion():
    descripcion = ""
    for i in range(4):
        if i < 3:
            descripcion += "".join(random.choices(string.ascii_letters, k=10)) + " "
        else:
            descripcion += "".join(random.choices(string.ascii_letters, k=10)) + "."
    return descripcion

def generar_archivo_en_binario(fd, n):
    m = open(fd, "ab")
    for i in range(n):
        clave = generar_clave()
        nombre = generar_nombre()
        descripcion = generar_descripcion()
        cantidad = random.randint(0, 1500)
        tipo_deporte = random.randint(1, 50)
        nivel = random.randint(0, 9)
        pickle.dump(Programa(clave, nombre, descripcion, cantidad, tipo_deporte, nivel), m)
    m.close()
    print("Archivo generado...")

# 2)
def mostrar_archivo(fd):
    hay_datos = False
    contador = 0
    if os.path.exists(fd):
        m = open(fd, "rb")
        size = os.path.getsize(fd)
        print("-" * 160)
        print(titulos())
        print("-" * 160)
        while m.tell() < size:
            hay_datos = True
            programa = pickle.load(m)
            contador += 1
            print(programa)
        m.close()
    if hay_datos is False:
        print("El archivo ", fd, "esta vacio")
    return contador

# 3)
def add_in_order(vec, programa):
    n = len(vec)
    izq = 0
    der = n - 1
    pos = n
    while izq <= der:
        centro = (izq + der) // 2
        if vec[centro].clave == programa.clave:
            pos = centro
            break

        if programa.clave < vec[centro].clave:
            der = centro - 1
        else:
            izq = centro + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [programa]
def Pasar_archivo_al_vector(vec, fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        size = os.path.getsize(fd)
        while m.tell() < size:
            programa = pickle.load(m)
            if programa.cantidad != 0:
                add_in_order(vec, programa)
        m.close()
    print("Arreglo generado...")
# 4)
def mostrar_vector(vec):
    print("-" * 160)
    print(titulos())
    print("-" * 160)
    for i in range(len(vec)):
        print(vec[i])


# 5)
def busqueda_secuencial(vec, nom):
    encontrado = False
    pos = -1
    for i in range(len(vec)):
        if vec[i].nombre == nom:
            pos = i
            encontrado = True
            break
    if encontrado is False:
        clave = generar_clave()
        nombre = nom
        descripcion = generar_descripcion()
        cantidad = random.randint(0, 1500)
        tipo_deporte = random.randint(1, 50)
        nivel = random.randint(0, 9)
        reg = Programa(clave, nombre, descripcion, cantidad, tipo_deporte, nivel)
        add_in_order(vec, reg)
        print("No existia ese programa pero ya fue cargado con el nombre")
    return pos


# 6)
def buscarBinariaDeX(vec, x):
    izq = 0
    der = len(vec) - 1
    ban = False
    while izq <= der:
        centro = (izq + der) // 2
        if vec[centro].clave == x:
            print("-" * 160)
            print(titulos())
            print("-" * 160)
            print(vec[centro])
            ban = True
            break
        elif x < vec[centro].clave:
            der = centro - 1
        else:
            izq = centro + 1
    if ban is False:
        print("Programa inexistente...")


# 7)
def generar_matriz(vec):
    matriz = [[0] * 50 for f in range(10)] # 50 columnas - tipo de deporte y 10 filas - nivel
    for reg in vec:
        filas = reg.nivel
        columnas = reg.tipo_deporte - 1
        matriz[filas][columnas] += reg.cantidad
    return matriz
def mostrar_matriz(matriz, m):
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[filas])):
            if matriz[filas][columnas] > m:
                print("-" * 50)
                print("Nivel: ", filas, "Tipo de deporte: ", columnas + 1, "Cantidad de deportistas: ", matriz[filas][columnas])

# 8)
def procesamiento(texto):
    texto = texto.lower()
    clet = 0
    cont_palabras = 0
    contador_numeros = 0
    comienza_vocal = False
    contiene_t = False

    if texto[-1] != ".":
        texto = texto + "."

    for car in texto:

        if car != " " and car != ".":
            clet += 1
            if car in "0123456789":
                contador_numeros += 1
            if clet == 1 and car in "aeiouáéíóúü":
                comienza_vocal = True
            if clet < 4 and car == "t":
                contiene_t = True

        else:
            if (clet % 2) == 0 and comienza_vocal and contiene_t:
                cont_palabras += 1
            clet = 0
            contador_numeros = 0
            comienza_vocal = False
            contiene_t = False

    return cont_palabras



def principal():
    fd = "Programas.dat"
    vec = []
    opcion = 0
    while opcion != 9:
        print("-" * 60)
        print('\nMenú de opciones:')
        print("1. Generar archivo")
        print("2. Mostrar registros y la cantidad de registros")
        print("3. Generar arreglo")
        print("4. Mostrar arreglo")
        print("5. Buscar programa por nombre")
        print("6. Buscar programa por clave")
        print("7. Generar y mostrar matriz")
        print("8. Procesamiento de caracteres")
        print("9. Salir")
        print("-" * 60)

        opcion = int(input("Ingrese su eleccion: "))

        if opcion == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de programas a cargar en forma automatica (mayor a 0): ")
            generar_archivo_en_binario(fd, n)
        elif opcion == 2:
            contador = mostrar_archivo(fd)
            print("La cantidad de registros mostrados es de: ", contador)

        elif opcion == 3:
            Pasar_archivo_al_vector(vec, fd)

        elif opcion == 4:
            if len(vec) != 0:
                mostrar_vector(vec)
            else:
                print("No se han cargado datos...")
        elif opcion == 5:
            if len(vec) != 0:
                nom = input("Ingrese el nombre a buscar: ")
                pos = busqueda_secuencial(vec, nom)
                if pos != -1:
                    print("-" * 160)
                    print(titulos())
                    print("-" * 160)
                    print(vec[pos])
            else:
                print("No se han cargado datos...")
        elif opcion == 6:
            if len(vec) != 0:
                k = input("Ingrese la clave a buscar: ")
                buscarBinariaDeX(vec, k)
            else:
                print("No se han cargado datos...")
        elif opcion == 7:
            if len(vec) != 0:
                m = validar_mayor_que(0, "Ingrese la cantidad minima: ")
                matriz = generar_matriz(vec)
                mostrar_matriz(matriz, m)
            else:
                print("No se han cargado datos...")
        elif opcion == 8:
            texto = input("Ingrese un texto a analizar: ")
            cantidad_palabras = procesamiento(texto)
            if cantidad_palabras != 0:
                print("La cantidad de palabras que cumplen con la condiccion es de: ", cantidad_palabras)
            else:
                print("No hay ninguna palabra que cumpla con la condiccion...")
        else:
            print("Opción inválida!")


if __name__ == "__main__":
    principal()
