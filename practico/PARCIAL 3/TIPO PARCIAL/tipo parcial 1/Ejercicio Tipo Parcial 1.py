"""
Una compañia de servicios de limpieza desea un programa para procesar los datos de los trabajos ofrecidos.
Por cada trabajo se tiene los siguientes datos:

- El número de identificación del trabajo,
- La descripcion o nombre del mismo
- El tipo de trabajo (un valor de 0 a 3, 0:interios, 1: exterior, 2: piletas, 3:tapizados)
- El importe a cobrar por ese trabajo
- La cantidad de personal afectado para prestar ese servicio

Se desea almacenar la informacion referida a los n trabajos en un arreglo de registros
de trabajos (definir el Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menu de opciones, que permita gestionar las siguientes tareas:

1) → Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo
     sea positivo y que el importe a cobrar sea mayor a cero.

   → Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores aleatorios)
     o puede disponer de ambas técnicas si lo desea.

   Pero al menos una debe programar.

2) Mostrar todos los datos de todos los trabajos, en un listado ordenado de mayor a menor según los importes a cobrar.

3) Determinar y mostrar los datos del trabajo que tenga la mayor cantidad de personal afectado
   (no importa si hay varios trabajos con la misma cantidad de personal: se permite mostrar uno y solo uno cuya cantidad de personal
   sea la maxima)

4) Determinar si existe un trabajo cuya descripción sea igual a d, siendo d un valor que se carga por teclado.
   Si existe, mostrar sus datos. Si no existe, informar con un mensaje. Si existe más de un registro que coincida
   con esos parámetros de búsqueda, debe mostrar sólo el primero que encuentre.

5) Determinar y mostrar la cantidad de trabajos por tipo.

"""

from MisFunciones import *

T_TIPO = "Interior", "Exterior", "Piletas", "Tapizados"  # Tupla cuya posicion muestra el tipo de trabajo


class Trabajo:
    def __init__(self, num, desc, tip, imp, cper):    # Cada parámetro de la funcion init representa un campo del registro
        self.numero = num
        self.descripcion = desc
        self.tipo = tip
        self.importe = imp
        self.cant_pers = cper

    def __str__(self):     # El format lo que hace es rellenar con espacios, se hace para que al imprimir el registro las lineas salgan alineadas
        renglon = ""       # Transforma todø a string y lo concatena
        renglon += "{:>6}".format(self.numero)
        renglon += "   "
        renglon += "{:<25}".format(self.descripcion)
        renglon += " "
        renglon += "{:<15}".format(T_TIPO[self.tipo])
        renglon += "{:>8.2f}".format(self.importe)
        renglon += " "
        renglon += "{:>4}".format(self.cant_pers)
        return renglon


def mostrar_menu():
    print("\nMenú de opciones: ")
    print("1. Cargar/generar arreglo")
    print("2. Mostrar ordenado por importe")
    print("3. Trabajo con mayor personal")
    print("4. Buscar trabajo por descripcion")
    print("5. Cantidad de trabajos por tipo")
    print("0. Salir")


def generar_rnd_trabajo():         # Función que genera 1 (uno solo) trabajo con datos (campos) aleatorios
    num = random.randint(1, 9999)
    desc = "Descripción trabajo_" + str(num)
    tip = random.randint(0, 3)
    imp = round(random.random() * 4500 + 500, 2)  # Importe entre 500 y 5000
    cper = random.randint(1, 20)                  # Cantidad arbitraria, podria haber puesto otra
    return Trabajo(num, desc, tip, imp, cper)

    # El return al haber llamado a la clase trabajo, hace que se ejecute __init__ , luego se genera la variable registro y se la puede asignar a otra variable



# --------- Funciones para resolver puntos del ejercicio ---------



def punto1(vec_tra, tam):  # Genera los valores que van a los casilleros del vector - Generar un vector de registro
    for i in range(tam):  # Por cada elemento del tamaño del vector...
        vec_tra[i] = generar_rnd_trabajo()


def punto2_ordenamiento(v, n):    # Parámetros: el vector (v) y el tamaño del vector (n)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].importe < v[j].importe:   # Ordenamos solo el campo de importe (.importe)
                v[i], v[j] = v[j], v[i]


def punto2_mostrar_datos(vec_tra):
    print("")
    print("-" * 64)
    for tra in vec_tra:
        print(tra)
    print("-" * 64)

    # Forma alternativa para el FOR:
    # for i in range(len(vec_tra)):
    #   print(vec_tra[i])


def punto3(vec_tra):
    may_tra = None
    for tra in vec_tra:
        if may_tra is None:
            may_tra = tra
        elif tra.cant_pers > may_tra.cant_pers:
            may_tra = tra
    return may_tra


def punto4(vec_tra, d):
    for tra in vec_tra:
        if tra.descripcion == d:
            return tra      # Si devuelve un trabajo es porque lo encontró
    return None             # Si devuelve None es porque no lo encontró


def punto5(vec_tra):
    vc = 4 * [0]            # Se usa 4 por la cantidad de tipos de trabajo (0 a 3)
    for tra in vec_tra:
        tip = tra.tipo      # Me fijo de que tipo es
        vc[tip] += 1
    #   vc[tra.tipo] += 1
    return vc

# ----------------------------------- Script Principal -------------------------------------------



def principal():
    n = None  # Se pone None para evitar un "warning" al invocar algunas funciones
    vt = []    # Vector de trabajos
    flag_menu_1 = False

    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese su selección: "))

        if opcion == 1:
            n = cargar_mayor_que(0, "\nIngrese la cantidad de trabajos a generar: ")  # Pedimos la cantidad de trabajos a cargar
            vt = n * [None]    # Le damos tamaño al arreglo el cual luego tendra los valores de Trabajo
            punto1(vt, n)
            print("Se han generado los trabajos correctamente...")
            flag_menu_1 = True


        elif opcion == 2:
            if flag_menu_1:
                punto2_ordenamiento(vt, n)
                punto2_mostrar_datos(vt)
            else:
                print("Primero debe generar/cargar los datos de los trabajos!")



        elif opcion == 3:
            if flag_menu_1:
                may_t = punto3(vt)  # may_t Recibe el valor del return de la funcion punto3
                print("\nEl trabajo con mayor cantidad de personal es:")
                print(may_t)
            else:
                print("Primero debe generar/cargar los datos de los trabajos!")


        elif opcion == 4:
            if flag_menu_1:
                d = cargar_nombre("Ingrese la descripción a buscar: ")
                trabajo = punto4(vt, d)
                if trabajo is not None:
                    print(trabajo)
                else:
                    print("No se encontró el trabajo")


        elif opcion == 5:
            if flag_menu_1:
                vconteo = punto5(vt)   # Devuelve un vector int con 4 casilleros y cada uno dice cuantos trabajos hay de cada tipo
                print("\nCantidad de trabajos por tipo: ")
                for i in range(len(vconteo)):
                    print("Tipo: ", T_TIPO[i], " - Cantidad: ", vconteo[i])     # Se utiliza i para mostrar el índice que corresponde a cada tipo
            else:
                print("Primero debe generar/cargar los datos de los trabajos!")

        elif opcion == 0:
            pass
        else:
            print("Opcion Inválida!")


principal()















