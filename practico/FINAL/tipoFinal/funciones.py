from registro import *
import os
import pickle
import random

'''1. Generar un arreglo de registros que contenga los datos de todos los proyectos. Puede generarlo cargando los
datos en forma manual o generando los datos en forma aleatoria. El arreglo debe permanecer ordenado por
número de identificación en todo momento durante la carga (será especialmente considerada la eficiencia de la
estrategia que aplique). Debe tener en cuenta que esta opción debe poder ser invocada varias veces a lo largo del
programa, y que en cada ejecución se debe poder agregar tantos registros como desee el operador, sin eliminar los
datos que ya estaban cargado'''


def validarMayor(mensaje):
    n = -1
    while n <= -1:
        n = int(input(mensaje))
        if n <= -1:
            print('Error, ingrese un numero de registros valido')
        return n


def cargaRegistro(n, reg):
    nombres = 'Proyecto nuevo', 'Proyecto', 'Decidex', 'Vacunacion'
    descripciones = ('Buenas noches.', 'que onda por suerte.', '123456789.', 'aerossol98.')
    for i in range(n):
        numeroIdentificacion = random.randint(1, 50)
        nombre = random.choice(nombres)
        descripcion = random.choice(descripciones)
        monto = random.randint(1, 1000)
        areaAplicacion = random.randint(1, 39)
        tipoProyecto = random.randint(0, 9)
        linea = Proyecto(numeroIdentificacion, nombre, descripcion, monto, areaAplicacion, tipoProyecto)
        addInOrder(reg, linea)
    return reg


# Recordar mejor que los tipos de ordenamientos
def addInOrder(reg, linea):
    izq, der = 0, len(reg) - 1
    pos = len(reg)
    while izq <= der:
        c = (izq + der) // 2
        # Lo unico que cambia es segun en que se ordena
        if reg[c].numeroIdentificacion == linea.numeroIdentificacion:
            pos = c
            break
        if reg[c].numeroIdentificacion > linea.numeroIdentificacion:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    reg[pos:pos] = [linea]


'''2. Mostrar el arreglo generado en el punto anterior, a razón de un registro por línea en 
la consola de salida'''


def displayRegistro(reg):
    for num in reg:
        print(to_string(num))  # Le esta pasando el registro


'''3. A partir del arreglo, generar un archivo binario de registros que contenga los datos de todos los proyectos cuyo 
tipo no sea ni 0 ni 1. Cada vez que esta opción se seleccione, el archivo debe crearse otra vez, eliminando los 
anteriores registros que hubiese contenido.
'''


def generarArchivo(reg, fd):
    archivo = open(fd, 'wb')
    contadorRegistros = 0
    acumuladorMontos = 0
    for num in reg:
        if num.tipoProyecto != 1 and num.tipoProyecto != 0:
            contadorRegistros += 1
            acumuladorMontos += num.monto
            pickle.dump(num, archivo)  # Recordar que hacia el pickle.dump
    promedio = acumuladorMontos / contadorRegistros
    archivo.close()
    return promedio


'''4. Mostrar todos los datos del archivo que generó en el punto 3, a razón de un registro por línea, pero agregue al 
final del listado una línea adicional indicando el monto promedio de todos los registros que se mosgtraron.'''


def mostrarArchivo(fd, promedio):
    tam = os.path.getsize(fd)
    m = open(fd, 'rb')
    while m.tell() < tam:
        registro = pickle.load(m)
        print((to_string(registro)))
    m.close()
    print('\n el monto promedio es: ', promedio)


'''5. Determine si existe en el arreglo creado en el punto 1 un proyecto en el que su número de identificación coincida 
con el valor num que se carga por teclado. Si existe, muestre sus datos completos y detenga la búsqueda. Si no 
existe, informe con un mensaje.'''


# Busqueda Binaria. | solo se puede usar con el vector ordenado de menor a mayor


def busqueda(reg, b):
    for n in reg:
        if n.numeroIdentificacion == b:
            return n
    return  -1

'''
Ver que diferencia hay porque no entindo xd
def busqueda(reg, b):
    izq, der = 0, len(reg) - 1
    # Con un ciclo while colocamos la condición de corte.-
    while izq <= der:
        num = (izq + der) // 2
        # Indice central
        if b == reg[num].numeroIdentificacion:
            pos = num
            return pos  # c: indice del elemento central q coincide con el elem. buscado.
        elif b < reg[num].numeroIdentificacion:
            der = num - 1
        else:
            izq = num + 1
    # Elemento buscado no se encuentra en el arreglo.
    return -1
'''

'''
# Busqueda Secuencial -> Algoritmo se usa cuando el vector no esta ordenado.
def linear_search(reg, b):
    for i in range(len(reg)):
        if b == reg[i]:# Consulto si el valor de "x" es igual al componente almacenado en la posición i.
            return i # Retorna el indice en donde se encontró el elemento x.-
    return -1 # El -1 es un indicador de que el elemento no lo encontré.
'''


def mostrar(reg):
    print('Numero de identficacion:', reg.numeroIdentificacion, '\t')
    print(' >> Nombre:', reg.nombre, '\t')
    print(' >> Descripcion:', reg.descripcion, '\t')
    print(' >> Monto', reg.monto, '\t')
    print(' >> Area', reg.areaAplicacion, '\t')
    print(' >> Tipo', reg.tipoProyecto, '\t')


'''6. Recorra el arreglo y cree una cadena que contenga la concatenación de todos los textos contenidos en el campo
objetivo de todos los registros en los que la longitud de la cadena contenida en ese campo sea mayor a 10. La
cadena creada solo debe contener UN punto al final, y debe cumplirse que las palabras sigan separadas entre ellas
por un y solo un espacio en blanco. Retorne la cadena creada, o retorne una cadena de la forma ‘Imposible.’ si
ningún registro cumplía la condición pedida. En ambos casos, muestre la cadena retornada
'''


# Ver diferencia entre i.descripcion y usar el v[i]
def cadenas(reg):
    cadena = ''
    for i in reg:
        if len(i.descripcion) > 10 and i.descripcion[-1] == '.':
            cadena += i.descripcion[:-1]
            cadena += ' '
    cadena = cadena[:-1] + '.'
    if cadena == '.':
        print('Ningun registro cumple esta condicion')
        cadena = 'Imposible'
        return cadena
    return cadena


'''7. A partir del arreglo, determine cuántos proyectos existen para cada una de las posibles combinaciones entre áreas 
de aplicación y tipos de proyectos (un total de 40 * 10 = 400 contadores). Muestre los resultados que sean 
diferentes a cero, pero solo para los contadores que correspondan a áreas mayores a 10.
'''


def matrizConteo(reg):
    conteo = [[0] * 40 for f in range(10)]
    n = len(reg)
    for i in range(n):
        f = reg[i].tipoProyecto
        c = reg[i].areaAplicacion
        conteo[f][c] += 1
    return conteo


# Ver bien el tema de matrices
def displayCount(conteo):
    filas, columnas = len(conteo), len(conteo[0])
    print('\nConteo de areas de aplicacion y tipos de proyectos')
    for f in range(filas):
        for c in range(columnas):
            if c > 10:
                if conteo[f][c] != 0:
                    print('\nTipo proyecto: ', f, '\t Area de aplicacion: ', c, '\tCantidad: ', conteo[f][c])


'''8. Tome la cadena retornada en el punto 6, y determine cuántas palabras de esa cadena contenían al menos dígito y
al menos una vez la combinación de dos vocales seguidas (por ejemplo: "aerosol98" o "x4solsticio" ). Como se
dijo, la cadena debe terminar con un punto y las palabras deben separarse entre ellas con un (y solo un) espacio en
blanco. La cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre
ella, al estilo usua'''


def es_vocal(caracter):
    return caracter in "aeiouáéíóúAEIOUÁÉÍÓÚ"


def es_digito(caracter):
    return caracter in "0123456789"


def punto8_digitosVocales(x):
    cont_cumpleCondicion = 0
    car_anterior = " "
    hay_digito = False
    hay_2vocales = False
    for caracter in x:
        if caracter != " " and caracter != ".":

            if es_digito(caracter):
                hay_digito = True

            if es_vocal(caracter) and es_vocal(car_anterior):
                hay_2vocales = True

        else:
            if hay_digito and hay_2vocales:
                cont_cumpleCondicion += 1

            # Reiniciamos a False y cero
            hay_digito = False
            hay_2vocales = False

        car_anterior = caracter
    print("Hay", cont_cumpleCondicion, " palabras que cumplen la condición")

# VER DIFERENCIA
# i.nombre
# v[i].nomvre
