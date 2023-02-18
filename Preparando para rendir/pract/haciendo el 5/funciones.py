from Registro import *
import random
import string
import os
import pickle

'''[1]. Generar un arreglo de n registros de tipo Deportista que contenga los datos de todos los deportistas (cargue el
valor de n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o
generando los datos en forma aleatoria. El arreglo debe permanecer ordenado por el nombre de los depostistas en
todo momento durante la carga. Debe considerar que esta opción puede ser invocada varias veces a lo largo del
programa, y que en cada ejecución pueden agregarse tantos registros como desee el operador, sin eliminar los
datos que ya estaban cargados. Será considerada la eficiencia de la estrategia de carga y los algoritmos que
aplique. [Máximo 4 puntos entre los ítems 1 y 2 juntos].'''
def generarArray(array, n):
    for i in range(n):
        deportista = generarDeportista()
        add_in_order(array,deportista)
    return array

def generarDeportista():
    numIdent = random.randint(1,100)
    nombre = random.choice(["EDUARDO","JOSE","MATIAS","DANIEL","JERE","RAFA"])
    deporte = random.randint(0,49)
    codigoBeca = random.randint(0,9)
    monto = round(random.uniform(0,1000),2)
    return Deportista(numIdent,nombre,deporte,codigoBeca,monto)

def add_in_order(array,deportista):
    n = len(array)
    izq = 0
    der = n - 1
    pos = n
    while izq <=der:
        centro = (izq+der)//2
        if array[centro].nombre == deportista.nombre:
            pos = centro
        if deportista.nombre < array[centro].nombre:
            der =  centro -1
        else:
            izq = centro + 1

    if izq>der:
        pos = izq

    array[pos:pos] = [deportista]


'''[2]. Mostrar todos los datos del arreglo generado en el punto a, de manera que en la pantalla se visualice un registro 
por renglón. [Máximo 4 puntos entre los ítems 1 y 2 juntos].'''
def mostrarArray(array):
    for i in range(len(array)):
        print(to_string(array[i]))

    print("")
    print("\nOTRA FORMA")
    print("="*50)
    print(titulos())
    print("="*50)
    for i in range(len(array)):
        print(array[i])

'''[3]. En base al arreglo generado en el punto 1, determinar el monto acumulado en concepto de pago por beca a los 
deportistas, para cada uno de los 10 tipos de beca posibles (es decir, un vector de conteo con un acumulador de 
montos para las becas tipo 0, otro para las becas tipo 1, y así sucesivamente). Muestre los resultados que sean 
diferentes de cero [Máximo 4 puntos].'''
def array_acumlacion(array):
    array_acumlacion = [0] *10 #Basicamente voy a tener diez de estos que son las cantidad de becas posibles
    for i in range(len(array)):
        x = array[i].codigoBeca
        array_acumlacion[x] += array[i].monto
    return array_acumlacion

'''[4]. En base al arreglo generado en el punto 1, determinar cuántos deportistas hay de cada posible deporte, por cada 
posible tipo de beca (un total de 50 * 10 = 500 contadores en una matriz de conteo: uno para la cantidad de 
depoertistas con deporte 0 y tipo de beca 0, otro para deporte 0 y beca 1, y así sucesivamente). Mostrar sólo los 
contadores diferentes de cero. [Máximo 4 puntos].'''
def matriz_conteo(array):
    m = [[0]* 50 for i in range(10)]
    for i in array:
        m[i.codigoBeca][i.deporte] += 1
    return m

def mostrar_matriz(m):
    for filas in range(len(m)):
        for columnas in range(len(m[filas])):
            if m[filas][columnas] != 0:
                print('Para el tipo de beca', filas, 'y el deporte', columnas, 'la cantidad de deportistas es: ', m[filas][columnas])

'''[5]. Cargando por teclado el nombre de un deportista, determinar si en el arreglo generado en el punto 1 existe uno
con ese nombre. Si existe, mostrar sus datos. Si no existe, informe con un mensaje. LA BÚSQUEDA DEBE
DETENERSE AL ENCONTRAR EL PRIMER REGISTRO CUYO NOMBRE COINCIDA CON EL QUE SE ESTÁ BUSCANDO. 
[Máximo 4 puntos].'''
def busquedaSecuencial(array,nombre):
    encontrado = False
    for i in range(len(array)):
        if array[i].nombre == nombre:
            print(to_string(array[i]))
            print("otra forma")
            print("="*50)
            print(titulos())
            print('='*60)
            print(array[i])  # solo porque tengo el objt con el __str__
            encontrado = True
            break
    if encontrado == False:
        print("No se encontro el nombre que busca")

'''[6]. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a 
deportistas con tipo de beca diferente de 0. [Máximo 4 puntos].''' #CONSULTAR SI TENDRIA QUE SER EN APPEND O SOLO GRABAR Y PISAR

def generarArchivoB(array,archivoB):
    m = open(archivoB , 'wb') #solo escritura
    monto = 0
    for i in range(len(array)):
        if array[i].codigoBeca != 0:
            pickle.dump(array[i], m)
            monto += array[i].monto

    m.close()
    print("Se genero el archivo...")

'''[7]. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando el monto acumulado pagado 
por todos los deportistas que se están mostrando. [Máximo 4 puntos].'''
def mostrarArchivo(archivoB):
    contador = 0
    monto = 0
    if os.path.exists(archivoB):
        m = open(archivoB, 'rb') #solo lectura
        print('='*50)
        print(titulos())
        print('=' * 50)
        while m.tell() < os.path.getsize(archivoB):
            print(pickle.load(m)) #CALCULO QUE ESTO ME DEJA POR EL __STR__
        m.close()


        print('\n OTRA FORMA')
        m = open(archivoB,'rb')
        while m.tell() < os.path.getsize(archivoB):
            reg = pickle.load(m)
            monto += reg.monto
            print(to_string(reg))
            contador +=1
        m.close()
        print('total de ', contador, 'becas diferentes a cero y el monto total acumlado es de ', monto)
    else:
        print('el archivo no existe')