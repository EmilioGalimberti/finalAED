from Registro import  *
import os
import pickle
import random
import string

'''1. Generar un archivo binario de registros que contenga los datos de todos los planes disponibles. El archivo debe 
generarse directamente sin crear primero un arreglo con los registros pedidos. Puede generarlo cargando los datos 
en forma manual o generando los datos en forma aleatoria. No se requiere que el archivo permanezca ordenado 
durante la carga. Debe considerar que esta opción puede ser invocada varias veces a lo largo del programa, y que 
en cada ejecución pueden agregarse al final del archivo tantos registros que desee el operador, sin eliminar los 
datos que ya estaban cargados.'''
def generarArchivoB(archivoB , n):
    m = open(archivoB, 'ab')
    for i in range(n):
        claveIdent = generarClave()
        nombre = random.choice(['Rehabilitacion' , 'Entrenamiento intensivo' , 'Pretemporada'])
        descripcion = generarDescripcion()
        monto = round(random.uniform(1,1000),2)
        tipoPlan = random.randint(1,10)
        rangoEdad = random.randint(1,40)
        pickle.dump(Plan(claveIdent , nombre, descripcion , monto , tipoPlan, rangoEdad), m)
    m.close()
    print('Archivo generado')

def generarClave():
    clave = str(random.randint(1,10)) + random.choice(string.ascii_lowercase) + str(random.randint(1,10)) + random.choice(string.ascii_lowercase)
    return clave

def generarDescripcion():
    descripcion =  ''.join(random.choices(string.ascii_lowercase,k=4)) + " " +  ''.join(random.choices(string.ascii_lowercase,k=2)) + '.'
    return descripcion

'''2. Mostrar el archivo generado en el punto anterior, a razón de un registro por línea en la consola de salida'''
def mostrarArchivo(archivoB):
    if os.path.exists(archivoB):
        m = open(archivoB, 'rb')
        print('='*100)
        print(titulos())
        print('='*100)
        while m.tell() < os.path.getsize(archivoB):
            print(pickle.load(m))
        m.close()

        m = open(archivoB, 'rb')
        print('Otra forma')
        while m.tell() < os.path.getsize(archivoB):
            obj = pickle.load(m)
            print(to_string(obj))
        m.close()
    else:
        print('No genero el archivo')

'''3. A partir del archivo, generar un arreglo unidimensional de registros que contenga los datos de todos los planes 
cuyo monto a abonar sea mayor a un valor p que se carga por teclado. No se requiere que este arreglo se 
mantenga ordenado mientras se genera.
'''
def generarArray(array, archivoB, p):
    if os.path.exists(archivoB):
        m = open(archivoB, 'rb')
        while m.tell() < os.path.getsize(archivoB):
            objt = pickle.load(m)
            if objt.monto > p:
                add_in_order(array, objt)
        m.close()

def add_in_order(array,objt):
    n = len(array)
    izq = 0
    der = n - 1
    pos = n
    while izq <= der:
        centro = (izq+der)//2
        if array[centro].claveIdent == objt.claveIdent:
            pos = centro
        if array[centro].claveIdent > objt.claveIdent:
            der = centro - 1
        else:
            izq = centro + 1

    if izq > der:
        pos=izq

    array[pos:pos] = [objt]

'''4. Mostrar todos los datos del arreglo que generó en el punto 3, pero de forma que el listado salga ordenado por 
clave de identificación.
'''
def mostrarArray(array):
    for i in range(len(array)):
        print(to_string(array[i]))

'''5. Determine si existe en el arreglo un plan en el que el nombre del plan coincida con el valor nom que se carga por 
teclado. Si existe, retorne la cadena contenida en el campo descripción y detenga la búsqueda. Si no existe, 
retorne una cadena de la forma ‘No existe’. En ambos casos, muestre la cadena retornada.'''
def buscarEnNombre(array, nombre):
    for i in range(len(array)):
        if array[i].nombre == nombre:
            print(to_string(array[i]))
            print(' ')
            print("su descripcion es: ", array[i].descripcion)
            return array[i].descripcion
    print("No se encontro")

'''6. Determine si existe en el arreglo un plan en el que la clave de identificación coincida con el valor k que se carga por 
teclado. Si existe, muestre sus datos completos y detenga la búsqueda. Si no existe, informe con un mensaje.'''
def buscarClaveIdent(array, k):
    for i in range(len(array)):
        if array[i].claveIdent == k:
            print(to_string(array[i]))
            return
    print("No se encontro")

'''7. Determine el cuántos planes existen para cada una de las posibles combinaciones entre tipos de planes y rangos 
de edades (un total de 10 * 5 = 50 contadores). Muestre sólo los resultados que sean diferentes a cero.
'''
def generarMatrizC(array):
    matriz = [[0] * 10 for i in range(5)]
    for i in array:
        matriz[i.tipoPlan][i.rangoEdad] += 1
    return matriz



def mostrarMatriz(matriz):
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[filas])):
            if matriz[filas][columnas] != 0:
                print("para los planes " , filas, ' y rango de edad ',columnas, ' la cantidad de planes ', matriz[filas][columnas] )

'''8. Tome la cadena retornada en el punto 5, y determine cuántas palabras de esa cadena contenían cuatro o más 
caracteres de largo (de cualquier tipo) y al menos una vez la letra “t” y la letra “b” pero de forma que la “t”
aparezca antes que la “b” (no es necesario que ambas letras estén consecutivas). Puede considerar que la cadena 
termina siempre con un punto, y que las palabras se separan entre ellas con un (y solo un) espacio en blanco. La 
cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella.'''

def procesarCaracteres(descripcion):
    descripcion = descripcion.lower()
    contCar = 0

    min4c = False
    hayT = False
    hayB = False

    contP = 0

    for caracter in descripcion:
        if caracter != ' ' and caracter != '.':
            contCar += 1
            if contCar >= 4:
                min4c = True
            if caracter == 't':
                hayT = True
            if hayT and caracter == 'b':
                hayB = True
        else:
            if min4c and hayT and hayB:
                contP += 1
                contCar = 0
                min4c = False
                hayT = False
                hayB = False
    print('la cnatidad de palabras que cumplen con estas condiciones es de: ', contP)