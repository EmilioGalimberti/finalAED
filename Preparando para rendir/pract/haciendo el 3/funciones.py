from Registro import *
import random
import pickle #Seralizacion Archivos
import os #Recorrido archivos
import string #ASCII for strings
'''1. Generar un archivo binario de registros que contenga los datos de todos los programas disponibles en el centro.
Puede generarlo cargando los datos en forma manual o aleatoria. No se requiere que el archivo permanezca
ordenado mientras se carga, ni tampoco que se ordene de ninguna forma al terminar el proceso. Debe considerar
que esta opción puede ser invocada varias veces a lo largo del programa, y que en cada ejecución pueden
agregarse tantos registros como desee el operador, sin eliminar los datos que ya estaban cargados. Observación:

NO CARGUE LOS DATOS EN UN ARREGLO PARA DESPUÉS GRABARLOS EN EL ARCHIVO: DIRECTAMENTE CARGUE
LOS DATOS EN EL ARCHIVO. SERÁ CONSIDERADA INCORRECTA CUALQUIER SOLUCIÓN BASADA EN GENERAR
PRIMERO UN ARREGLO Y LUEGO GRABAR ESE ARREGLO EN EL ARCHIVO.'''
def generarArhvioB(arhivo,cantProgramas):
    m = open(arhivo,'ab')  #modo de sólo append para archivo binario (todas las grabaciones se  hacen al final del archivo, preservando su contenido previo si el archivo ya existía
    for i in range(cantProgramas):
        clave = generarClave()
        nombre = random.choice(["Benjamin", "Isabella", "Martina", "Catalina"]) #fijase si funca bien asi osino hay que resolverlo de la otra forma
        descripcion = generarDescripcion()
        cantDeportistasReg = random.randint(0,100)
        tipoDeporte = random.randint(1,5)
        nivel = random.randint(0,9)
        # Graba los valores de las variables en el archivo
        #Necesitas la Clase, variables a guardar, en el archivo a guardar
        pickle.dump(Programa(clave, nombre, descripcion, cantDeportistasReg, tipoDeporte, nivel), m)
    m.close() #cerramos el archivo
    print('Archivo generado..')

def generarClave():
    clave = 0
    for i in range(3):
        #clave += random.choice(string.ascii_letters) + random.choice(string.digits)    EN VERDAD TENDRIA QUE HACER ASI
        clave += random.randint(1,20) #Puse esto para probar el algoritmo de ordenamiento para el vector
    return clave
def generarDescripcion():
    descripcion = ''
    for i in range(4):
       if i < 3:
        descripcion += "".join(random.choices(string.ascii_letters, k=5)) + " " #preguntas si saben usar el .join
       else:
           descripcion += ''.join(random.choices(string.ascii_letters, k=5))+ "." #necesitamos del if y hacerlo asi porque debe terminar en punto
    return descripcion

'''2. Muestre el archivo generado, a razón de un registro por línea en la consola de salida. Al final del listado, muestre
una línea adicional en la que se informe cuántos registros se mostraron.'''
def mostrarArchivo(archivo):
    contador = 0
    if os.path.exists(archivo):
        m = open(archivo, 'rb') #Binariosolo lectura
        print('-'*110)
        print(titulos())
        print('-' * 110)
        #con tell reotrna el valor del filepointer como valor entero, entonces esto permite un recorrid
        #y mientras este sea menor al tamaño del achivo lo ira recorriendo y mostrando
        while m.tell() < os.path.getsize(archivo): # SON LAS DOS FOMRAS
            print(pickle.load(m)) #el pickle load es para leer el contenido del archivo abierto (m)
            contador += 1
        print("AAAAAAAAAAAAA")
        m.close()
        m = open(archivo, 'rb')
        while m.tell() < os.path.getsize(archivo): #SON LAS DOS FORMAS
            programa = pickle.load(m)
            print(to_string(programa))
        m.close()
    else:
        print("El archivo no existe. ")
    return contador

'''3. A partir del archivo cargado en el punto 1, genere un arreglo de registros con todos los programas del archivo cuya
cantidad de deportistas registrados sea diferente de cero(EN EL OBJETO). El arreglo debe mantenerse ordenado de menor a
mayor en todo momento durante el proceso de creación, de acuerdo al valor del campo clave de identificación.
Cada vez que esta opción se elija, el arreglo debe volver a crearse desde cero, eliminando los datos que pudiese
contener anteriormente. NO GENERE ESTE ARREGLO DIRECTAMENTE EN LA OPCIÓN 1, AL MISMO TIEMPO QUE
GRABA EL ARCHIVO. DEBE RESOLVER ESTE PEDIDO CON UNA OPCIÓN SEPARADA EN EL MENÚ DE OPCIONES.'''
#Es leer el archivo como en el 2 pero en ves de mostrarlo por pantalla, lo cargamos en un array
def genararArray(array ,archivoB):
    if os.path.exists(archivoB):
        m = open(archivoB, 'rb')
        while m.tell() < os.path.getsize(archivoB):
            programa = pickle.load(m)
            if programa.cantDeportistasReg != 0:
                add_in_order(array, programa)
        m.close()
    print('array Cargado...')

#LITERALMENTE MEMORIZAR COMO FUNCA
def add_in_order(array, programa):
    n = len(array)
    izq = 0
    der = n-1
    pos = n
    while izq <= der:
        centro = (izq+der) //2
        if array[centro].clave == programa.clave:
            pos = centro
            break
        if programa.clave < array[centro].clave:
            der = centro - 1
        else:
            izq = centro + 1
    # ATENTO QUE ESTO NO TIENE QUE ESTAR DENTRO DEL WHILE
    if izq > der:
            pos=izq
    #ATENTO QUE ESTO NO TIENE QUE ESTAR DENTRO DEL WHILE
    array[pos:pos] = [programa]  #ESTUDIARLO MEJOR

'''4. Muestre el arreglo generado en el punto anterior, a razón de un registro por línea en la pantalla.'''
def mostrarArray(array):
    print("-" * 160)
    print(titulos())
    print("-" * 160)
    for i in range(len(array)):
        print(array[i])

'''5. Determine si existe en el arreglo un programa en el que el nombre del entrenador coincida con el valor nom que
se carga por teclado. Si existe, detenga la búsqueda al primero que encuentre y muestre todos sus datos. Si no
existe, cargue por teclado (o genere en forma aleatoria) un registro nuevo con los datos del programa, asigne el
nombre nom del entrenador en el campo correspondiente, y agregue en el arreglo el nuevo registro, manteniendo
el orden por clave de identificación.
'''
def busquedaSecuencial(array, nombreB):
    encontrado = False
    pos = -1
    for i in range(len(array)):
        if array[i].nombre == nombreB:
            encontrado = True
            pos = i
            break
    if encontrado == False:
        clave = generarClave()
        nombre = nombreB
        descrpicion = generarDescripcion()
        cantDeportistasReg = random.randint(0, 100)
        tipoDeporte = random.randint(1, 5)
        nivel = random.randint(0, 9)
        obj = Programa(clave,nombre,descrpicion,cantDeportistasReg,tipoDeporte,nivel)
        add_in_order(array, obj)
        print("No existia ese programa pero ya fue cargado con el nombre")
    return pos

'''6. Determine si existe en el arreglo un programa en el que la clave de identificación coincida con el valor k que se
carga por teclado. Si existe, muestre sus datos completos y detenga la búsqueda al primero que encuentre. Si no
existe, informe con un mensaje.'''
def busquedaIdentificacion(array,k):
    for i in range(len(array)):
        if array[i].clave == k:
            print('El programa que conicide con lo solicitado es: ')
            print("-" * 160)
            print(titulos())
            print("-" * 160)
            print(array[i])
            break
    print('No se encontre ningun programa con la clave solicitade')

'''7. Determine la cantidad acumulada de deportistas que están registrados para cada uno de los posibles deportes y
por cada nivel posible de entrenamiento (un total de 50 * 10 = 500 acumuladores). Muestre sólo los resultados
que sean mayores a un valor m que se carga por teclado. REPASAR'''

#7)
def generar_matriz(vec):
    matriz = [[0] * 50 for f in range(10)] # 50 columnas - tipo de deporte y 10 filas - nivel
    for reg in vec:
        filas = reg.nivel
        columnas = reg.tipo_deporte - 1 #porque -1?
        matriz[filas][columnas] += reg.cantidad   #Creo que esto seria de acumulacion pero ni idea ESTO NO ENTIENDO MUCHO

    return matriz
def mostrar_matriz(matriz, m):
    for filas in range(len(matriz)): #Recorre por filas
        for columnas in range(len(matriz[filas])):
            if matriz[filas][columnas] > m:
                print(matriz)
                print("-" * 50)
                ''' muestra los resultados obtenidos, considerando sólo aquellos casilleros que hayan quedado con valor diferente de m:'''
                print("Nivel: ", filas, "Tipo de deporte: ", columnas + 1, "Cantidad de deportistas: ", matriz[filas][columnas])

def validar_mayor_que(inferior, mensaje):
    numero = inferior
    while numero <= inferior:
        numero = int(input(mensaje))
        if numero <= inferior:
            print("Valor incorrecto!")
    return numero
'''8. Cargue por teclado una cadena de caracteres, terminada en punto y con palabras separadas con un blanco según
lo habitual. Determine cuántas palabras de la cadena tienen un número par de caracteres, comienzan con una
vocal y tienen al menos una "t" entre los primeros tres caracteres (un único contador para palabras que cumplan
con los tres criterios al mismo tiempo).'''

def procesamientoTexto(texto):
    comienzaVocal = False
    numCaracter = 0
    contieneT = False
    contPalabras = 0

    if texto[-1] != '.':
        texto = texto+'.' # ES PARA VERIFICAR SI TERMINA EN PUNTO, PERO NO LO PIDE

    for caracter in texto:
        if caracter != ' ' and  caracter != '.':
            numCaracter += 1
            if numCaracter == 1 and caracter in 'AEIOUaeiou':
                comienzaVocal = True
            if numCaracter <= 3 and caracter == 't':
                contieneT = True
        else:
            if (numCaracter%2) == 0 and comienzaVocal and contieneT: #lo primero era para ver si tiene cantidad para de caracteres
                contPalabras += 1

    return contPalabras