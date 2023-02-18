import random
import os
import pickle
import string
from Registro import *

'''[1]. Generar un arreglo de n registros de tipo Paciente que contenga los datos de todos los pacientes (cargue el valor
de n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o
generando los datos en forma aleatoria. El arreglo debe permanecer ordenado por el número de historia clínica en
todo momento durante la carga. Debe considerar que esta opción puede ser invocada varias veces a lo largo del
programa, y que en cada ejecución pueden agregarse tantos registros como desee el operador, sin eliminar los
datos que ya estaban cargados. Será considerada la eficiencia de la estrategia de carga y los algoritmos que
aplique. [Máximo 4 puntos entre los ítems 1 y 2 juntos].'''

def generarArray(array,n):
    for i in range(n):
        numeroHistoria = random.randint(1,99)
        nombrePaciente = random.choice(['Emilio','Santina','Juan','Paola'])
        numeroEspecialidad = random.randint(0,29)
        numeroCobertura = random.randint(0,9)
        monto = round(random.uniform(0,1000),2)
        objtPaciente = Paciente(numeroHistoria, nombrePaciente, numeroEspecialidad, numeroCobertura , monto)
        add_in_order(array, objtPaciente)
    print('Array generado correctamente')

def add_in_order(array, objtPaciente):
    n = len(array)
    izq = 0
    der = n - 1
    pos = n

    while izq <= der:
        centro = (izq+der)//2
        if array[centro].numeroHistoria == objtPaciente.numeroHistoria:
            pos = centro
        if objtPaciente.numeroHistoria < array[centro].numeroHistoria:
            der = centro -1
        else:
            izq = centro +1
    if izq>der:
        pos = izq

    array[pos:pos] = [objtPaciente]

'''[2]. Mostrar todos los datos del arreglo generado en el punto a, de manera que en la pantalla se visualice un registro
por renglón. [Máximo 4 puntos entre los ítems 1 y 2 juntos].'''

def mostraArray(array):
    print('=' * 90)
    print(titulos())
    print('=' * 90)
    for i in range(len(array)):
        print(array[i])

    print("OTRA FORMA")
    for i in range(len(array)):
        print(to_string(array[i]))

'''[3]. En base al arreglo generado en el punto b, crear otro arreglo unidimensional que contenga sólo los registros de los
pacientes que tienen un monto a pagar diferente de cero y tengan tipo de cobertura diferente de 1. Muestre este
nuevo arreglo al terminar de crearlo. [Máximo 4 puntos].'''
def generarArray2(array):
    array2 = []
    for i in range(len(array)):
        if array[i].monto != 0:
            if array[i].numeroCobertura != 1:
                array2.append(array[i])

    if len(array2) >0:
        print("=" * 100)
        print(titulos())
        print('=' * 100)
        for i in range(len(array2)):
            print(array2[i])

    return array2

'''[4]. En base al arreglo generado en el punto c, determinar cuántos pacientes hay de cada posible especialidad, por
cada posible tipo de cobertura (un total de 30 * 10 = 300 contadores en una matriz de conteo: uno para la
cantidad de pacientes con especialidad 0 y tipo de cobertura 0, otro para especialidad 0 y cobertura 1, y así
sucesivamente). Mostrar sólo los contadores diferentes de cero. [Máximo 4 puntos].
'''
def generarMatrizConteo(array2):
    matriz = [[0]* 30 for i in range(10)]
    for i in array2:
        matriz[i.numeroEspecialidad][i.numeroCobertura] += 1
    return matriz

def mostrarMatriz(matriz):
    for filas in range(len(matriz)):
        for columnas in range(len(matriz[filas])):
            if matriz[filas][columnas] != 0:
                print('Para la especialidad ' ,filas, 'y el deporte ', columnas, ' la cantidad de paciente es ', matriz[filas][columnas])

'''[5]. Cargando por teclado el nombre de un paciente, determinar si en el arreglo generado en el punto c existe uno con
ese nombre. Si existe, mostrar sus datos. Si no existe, informe con un mensaje. LA BÚSQUEDA DEBE DETENERSE AL
ENCONTRAR EL PRIMER REGISTRO CUYO NOMBRE COINCIDA CON EL QUE SE ESTÁ BUSCANDO. [Máximo 4
puntos].
'''
def buscarPorNombre(array2, nombre):
    for i in range(len(array2)):
        if array2[i].nombre == nombre:
            print(to_string(array2[i]))
            return
    print("No se encontra ningun paciente con el nombre: ",nombre)

'''[6]. Grabar en un archivo binrario el contenido completo del arreglo generado en el punto c. [Máximo 4 puntos].'''
def genararArchivoB(archivoB,array2):
    m = open(archivoB, 'wb')
    for i in range(len(array2)):
        pickle.dump(array2[i], m)
    m.close()
    print("Archivo generado con Exito!")

'''[7]. Mostrar el archivo generado en el punto f. Muestre al final una línea extra indicando el monto acumulado pagado
por todos los pacientes que se están mostrando. [Máximo 4 puntos].'''
def mostrarArchivob(archivoB):
    if os.path.exists(archivoB):
        m = open(archivoB, 'rb')
        print(titulos())
        while m.tell() < os.path.getsize(archivoB):
            print(pickle.load(m))
    m.close()