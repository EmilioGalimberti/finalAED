from reg_final7 import *
import pickle
import os.path


# [1]. Generar un arreglo de n registros de tipo Deportista que contenga los datos de todos los deportistas (cargue el
# valor de n por teclado validando que sea correcto). Puede generar el arreglo cargando los datos en forma manual o
# generando los datos en forma aleatoria. El arreglo debe permanecer ordenado por el nombre de los depostistas en
##todo momento durante la carga. Debe considerar que esta opción puede ser invocada varias veces a lo largo del
###programa, y que en cada ejecución pueden agregarse tantos registros como desee el operador, sin eliminar los
####datos que ya estaban cargados. Será considerada la eficiencia de la estrategia de carga y los algoritmos que
#####aplique. [Máximo 4 puntos entre los ítems 1 y 2 juntos].

######[2]. Mostrar todos los datos del arreglo generado en el punto a, de manera que en la pantalla se visualice un registro
######por renglón. [Máximo 4 puntos entre los ítems 1 y 2 juntos].

######[3]. En base al arreglo generado en el punto 1, determinar el monto acumulado en concepto de pago por beca a los
######deportistas, para cada uno de los 10 tipos de beca posibles (es decir, un vector de conteo con un acumulador de
######montos para las becas tipo 0, otro para las becas tipo 1, y así sucesivamente). Muestre los resultados que sean
######diferentes de cero [Máximo 4 puntos].

######[4]. En base al arreglo generado en el punto 1, determinar cuántos deportistas hay de cada posible deporte, por cada
######posible tipo de beca (un total de 50 * 10 = 500 contadores en una matriz de conteo: uno para la cantidad de
######depoertistas con deporte 0 y tipo de beca 0, otro para deporte 0 y beca 1, y así sucesivamente). Mostrar sólo los
######contadores diferentes de cero. [Máximo 4 puntos].

######[5]. Cargando por teclado el nombre de un deportista, determinar si en el arreglo generado en el punto 1 existe uno
######con ese nombre. Si existe, mostrar sus datos. Si no existe, informe con un mensaje. LA BÚSQUEDA DEBE
######DETENERSE AL ENCONTRAR EL PRIMER REGISTRO CUYO NOMBRE COINCIDA CON EL QUE SE ESTÁ BUSCANDO.
######[Máximo 4 puntos].

#####[6]. Grabar en un archivo binario los datos de los registros del arreglo generado en el punto 1 que correspondan a
####deportistas con tipo de beca diferente de 0. [Máximo 4 puntos].

###[7]. Mostrar el archivo generado en el punto 6. Muestre al final una línea extra indicando el monto acumulado pagado
##por todos los deportistas que se están mostrando. [Máximo 4 puntos].

#


def addinorder(vec, deportista):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if vec[c].nom == deportista.nom:
            pos = c

        if deportista.nom < vec[c].nom:
            der -= 1

        else:
            izq += 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [deportista]


def vector_conteo(vec):
    vec_conteo = [0] * 10
    for i in range(len(vec)):
        x = vec[i].cod
        vec_conteo[x] += vec[i].monto
    return vec_conteo


def cargarDeportistas(vec, deportistas):
    for i in range(deportistas):
        deportista = crear_aleatorio()
        addinorder(vec, deportista)
    return vec


def mostrarDeportistas(vec):
    for i in range(len(vec)):
        print(to_string(vec[i]))


def asignar_matriz_conteo(vec):
    m = [[0] * 50 for i in range(10)]

    for i in vec:
        m[i.cod][i.dep] += 1
    return m


def mostrar_mc(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] != 0:
                print('Para el tipo de beca', i, 'y el deporte', j, 'la cantidad es: ', m[i][j])


def estaOrdenadorPorNombre(vec, nombre):
    for i in range(len(vec) - 1):
        if vec[i].nom > vec[i + 1].nom:
            return False
    return True


def busquedaBinariaPorNombre(vec, nombre):
    n = len(vec)
    pos = -1
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2

        if nombre == vec[c].nom:
            print(to_string(vec[c]))
            break

        if nombre < vec[c].nom:
            der = c - 1

        else:
            return c

    return -1


def busquedaSecuencialPorNombre(vec, nombre):
    for i in range(len(vec)):
        if vec[i].nom == nombre:
            return i
    return -1


def buscarPorNombre(vec, nombre):
    if estaOrdenadorPorNombre(vec, nombre):
        return busquedaBinariaPorNombre(vec, nombre)
    return busquedaSecuencialPorNombre(vec)


def crear_archivo(vec):
    fd = "deportistas"
    archivo = open(fd,"wb")
    contador = 0
    monto = 0

    archivo = open(fd, 'wb')
    for i in range(len(vec)):
        if vec[i].cod != 0:
            monto += vec[i].monto
            contador += 1
            pickle.dump(vec[i], archivo)
    archivo.close()
    print('Se creo un archivo', fd, ' con un total de ', contador, 'becas diferentes a cero')


def mostrar_archivo(archivo):
    if not os.path.exists(archivo):
        print("No se encuentra el archivo")
    else:
        fd = open(archivo , "rb")
        tam = os.path.getsize(archivo)
        while fd.tell() < tam:
            reg = pickle.load(fd)
            print(to_string(reg))

        fd.close()


def menu():
    opc = None
    vec = []
    pasoPor1 = False
    print("*"*100)
    print("1) Cargar Arreglo")
    print("2) Mostrar Arreglo")
    print("3 Vector de conteo")
    print("4) Vector de conteo")
    print("5) Buscar por nombre")
    print("6) Generar archivo")
    print("7) Mostrar archivo")
    print("8) Salir del menu de opciones")
    print("*"*100)
    opc = int(input("Ingrese una opcion de menu :"))

    while opc != 8:

        if opc == 1:
            print("*"*100)
            deportistas = int(input("Ingrese una cantidad de deportistas a cargar:"))
            cargarDeportistas(vec, deportistas)
            print("El arreglo fue creado con exito")
            # addinorder(vec)
            pasoPor1 = True

        opc = int(input("Ingrese una opcion de menu :"))
        if opc == 2 and pasoPor1:
            print("*"*100)
            mostrarDeportistas(vec)
            pass

        if opc == 3:
            print("*"*100)
            vc = vector_conteo(vec)
            for i in range(len(vc)):
                if vc[i] != 0:
                    print('Para el tipo de beca ', i, 'el monto total es: ', round(vc[i], 2))

        if opc == 4:
            print("*"*100)
            matriz = asignar_matriz_conteo(vec)
            mostrar_mc(matriz)

        if opc == 5:
            print("*"*100)
            nombre = input("Ingrese un nombre de un deportista a buscar")
            pos = buscarPorNombre(vec, nombre)
            if pos == -1:
                print("No existe un deportista con dicho nombre")
            else:
                print(to_string(vec[pos]))

        if opc == 6:
            print("*"*100)
            crear_archivo(vec)

        if opc == 7:
            print("*"*100)
            archivo = input("Ingrese el nombre del archivo")
            mostrar_archivo(archivo)
        if opc == 8:
            print("*"*100)
            print("Gracias la puta que te pario,chau")


menu()
