'''

TRABAJO PRACTICO 03
ALGORITMOS Y ESTRUCTURA DE DATOS

INTEGRANTES
 ►  Díaz González, Juan Pablo           Curso: 1K05  (90950)
 ►  Galimberti, Emilio                  Curso: 1K07  (90747)
 ►  Ontivero Capello, Gabriel Nicolás   Curso: 1K06  (91297)

'''

import random

titulo = ("Un secreto en la Ventana", "Padre Rico, Padre Pobre", "The 5 AM Club: Controla tus mañanas", "Can't Hurt me", "El Señor de los Anillos", "Harry Potter", "El Código da Vinci", "Los Cuatro Acuerdos", "Deep Work", "Atomic Habits")
genero = ("Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía", "Infantil", "Otros")
idioma = ("Español", "Inglés", "Francés", "Italiano", "Otros")

class Libro:
    def __init__(self, isbn='', tit='', gen=0, idi=0, pre=0):
        self.codigo = isbn
        self.titulo = tit
        self.genero = gen
        self.idioma = idi
        self.precio = pre

# ──────────────────────────────────────────── MENU DE OPCIONES ──────────────────────────────────────────────────
# opc == 1:
def generacion_y_carga(v):
    cant_libros = int(input("1). Ingrese la cantidad de libros a CARGAR: "))
    for i in range(cant_libros):
        v.append(None)

    print("\nTipos de carga:\n- 1.Manual\n- 2.Automática\n")
    carga = int(input("> Seleccione un numero de tipo de CARGA: "))

    # CARGA MANUAL
    if carga == 1:
        read(v)

    # CARGA AUTOMATICA
    if carga == 2:
        generate(v)


# opc == 2:
def mostrar(v):
    print("Funcion de muestra de todos los LIBROS DISPONIBLES.")
    print("\n> Libros Disponibles:")
    print(datos(v))


# opc == 3:
def conteo_y_genero_popular(v):
    print("Funcion de muestra de cantidad de libros ofrecidos por género y genero mas popular.")

    may_g, cont_g = mayor_genero(v, genero)

    print("\n> Cantidad de libros de:")
    for g in range(10):
        print("\t-", genero[g], ":", cont_g[g])
    print("\n>> El genero con mas libros disponibles es:", genero[cont_g.index(may_g)])


# opc == 4:[[]
def busqueda_del_mayor(v):
    print("Funcion de busqueda del libro de mayor precio según su idioma.")
    print("\nRerencia de Idiomas:\n0. Español.\n1. Inglés.\n2. Francés.\n3. Italiano.\n4. Otros.")

    i_lenguaje = int(input("\n>> Ingrese el numero del lenguaje que desea buscar: "))
    lenguaje = str(idioma[i_lenguaje])
    i_may = may_precio(v, lenguaje)

    print("\n> Libro mas costoso en el idioma", v[i_may].idioma, ":")
    print(to_string(v[i_may]))


# opc == 5:
def busqueda_por_ISBN(v):
    flag_encontrado = False
    print("Funcion de busqueda de un libro mediante codigo ISBN.")
    busqueda = str(input("\n>> Ingrese el CODIGO ISBN del libro que desea buscar: "))
    for i in range(len(v)):
        if v[i].codigo == busqueda:
            res = '\t| Codigo: '+ str(v[i].codigo)
            res += ' | Titulo: '+ str(v[i].titulo)
            res += ' | Genero: '+ str(v[i].genero)
            res += ' | Idioma: '+ str(v[i].idioma)
            res += ' | Precio actualizado (+%10): $'+ str("{:.2f}".format(v[i].precio * 1.1)) + '|\n'
            print(res)
            flag_encontrado = True
    if not flag_encontrado:
        print("(( Libro no encontrado ))")


# opc == 6:
def consulta_por_genero(v):
    print("Funcion de muestra listado descendente en precio de libros del genero mas popular:")
    may_g, cont_g = mayor_genero(v, genero)
    print("\n> El genero con mas cantidad de Libros disponibles es:", genero[cont_g.index(may_g)])
    print("\n> Listado de Libros disponibles de", genero[cont_g.index(may_g)], "(Ordenados de Mayor a Menor):")
    insertion_sort(v)
    print(datos(v))


# opc == 7:
def consulta_precio_por_grupo(v):
    si = []
    no = []
    print("Funcion de busqueda de libros en grupo.")
    cant = int(input(">> Ingresar la cantidad de Libros a consultar: "))
    for c in range(cant):
        busqueda = str(input("\n>> Ingrese el CODIGO ISBN del libro que desea buscar: "))
        for i in range(len(v)):
            if v[i].codigo == busqueda:
                si.append(i)
            else:
                no.append(v[i].codigo)

    # CORREGIR ESTO ULTIMO
    res = ' '
    for i in range(len(si)):
        res += to_string(v[si]) + ' '

    for i in range(len(no)):
        print(no[i])


# ──────────────────────────────────────────── FUNCIONES  ──────────────────────────────────────────────────

def insertion_sort(v):
    for j in range(len(v)):
        y = v[j].precio
        k = j - 1
        while k >= 0 and y > v[k].precio:
            v[k+1].precio = v[k].precio
            k -= 1
        v[k+1].precio = y

# ───────────────────────────────────────────────────────────────────────────

def mayor_genero(v, genero):
    cont_g = 11 * [0]
    for i in range(len(v)):
        for g in range(10):
            if v[i].genero == genero[g]:
                cont_g[g] += 1
    may_g = max(cont_g)
    return may_g, cont_g

# ───────────────────────────────────────────────────────────────────────────

def may_precio(v, lenguaje):
    may = 0
    i_may = 0
    for i in range(len(v)):
        if v[i].idioma == lenguaje:
            if v[i].precio > may:
                may = v[i].precio
                i_may = i
    return i_may

# ───────────────────────────────────────────────────────────────────────────

def generate(v):
    for i in range(len(v)):
        flag_valido = False
        while not flag_valido:
            isbn = str(random.randrange(100,1000))
            isbn += '-' + str(random.randrange(100,1000))
            isbn += '-' + str(random.randrange(10,100))
            isbn += '-' + str(random.randrange(1,10))
            flag_valido = comprobar_ISBN(isbn)
            isbn_entero = cadena_a_vector(isbn)

            cont = 10
            n = 0   # Acumulador
            for car in isbn_entero:
                n = n + cont * car
                cont = cont - 1
            res = n % 11
            isbn += str(res)

        tit = random.choice(titulo)
        gen = random.choice(genero)
        idi = random.choice(idioma)
        pre = random.randrange(1000,5000)
        v[i] = Libro(isbn, tit, gen, idi, pre)

# ───────────────────────────────────────────────────────────────────────────

def read(v):
    for i in range(len(v)):
        print("─"*60)
        print("Carga Libro[",i+1,"]:")
        flag_valido = False
        while not flag_valido:
            isbn = input('> Codigo ISBN: ')
            flag_valido = comprobar_ISBN(isbn)
            if flag_valido:
                print("(( ISBN VALIDO ))")
            else:
                print("(( ISBN NO VALIDO, porfavor intente de nuevo... ))")
        tit = input('> Titulo: ')
        print("Generos: 0.Autoayuda  1.Arte  2.Ficción  3.Computación  4.Economía  5.Escolar  6.Sociedad  7.Gastronomía  8.Infantil  9.Otros")
        gen = int(input('> Genero: '))
        print("Idioma: 0.Español  1.Inglés  2.Francés  3.Italiano  4.Otros")
        idi = int(input('> Idioma: '))
        pre = int(input('> Precio: $'))
        v[i] = Libro(isbn, tit, gen, idi, pre)

# ───────────────────────────────────────────────────────────────────────────

def to_string(libro):
    res = '\t| Codigo: '+ str(libro.codigo)
    res += ' | Titulo: '+ str(libro.titulo)
    res += ' | Genero: '+ str(libro.genero)
    res += ' | Idioma: '+ str(libro.idioma)
    res += ' | Precio: $'+ str(libro.precio) + '|\n'
    return res

# ───────────────────────────────────────────────────────────────────────────

def datos(v):
    res = ' '
    for i in range(len(v)):
        res += to_string(v[i]) + ' '
    return res

# ───────────────────────────────────────────────────────────────────────────

def cadena_a_vector(isbn):
    isbn_entero = []
    for i in isbn:
        if i != "-":
            isbn_entero.append(int(i))
    return isbn_entero

# ───────────────────────────────────────────────────────────────────────────

def comprobar_ISBN(isbn):
    caran = " "
    conta_guion = 0
    cont = 10
    n = 0   # Acumulador
    sintaxis_bien = False
    flag_valido = False

    # Verificación Guiones
    for car in isbn:
        if car == "-":
            conta_guion = conta_guion + 1
        if car == "-" and caran != "-":
            if conta_guion == 3:
                sintaxis_bien = True
        caran = car

    isbn_entero = cadena_a_vector(isbn)

    # Verificación de divisibilidad
    for car in isbn_entero:
        n = n + cont * car
        cont = cont - 1

    if n % 11 == 0 and sintaxis_bien:
        flag_valido = True

    return flag_valido

# ───────────────────────────────── PRINCIPAL ──────────────────────────────────────────

def principal():
    opc = None
    v = []
    while opc != 8:
        print("─"*60)
        print("                   TRABAJO PRACTICO N°3")
        print("─"*60)

        print("> > > REFERENCIA DE OPCIONES:")
        print("1.) Generación y Carga de libros.")
        print("2.) Mostrar detalles de libros disponibles.")
        print("3.) Conteo y género más popular.")
        print("4.) Búsqueda del libro mas caro por idioma.")
        print("5.) Búsqueda por ISBN.")
        print("6.) Consulta de un género.")
        print("7.) Consulta de precio por grupo.")
        print("8.) Exit.")
        print("─"*60)
        opc = int(input(">> Ingrese el numero de la opción a ejecutar: "))
        print("─"*60)

        if opc == 1:
            generacion_y_carga(v)
        if opc == 2:
            mostrar(v)
        if opc == 3:
            conteo_y_genero_popular(v)
        if opc == 4:
            busqueda_del_mayor(v)
        if opc == 5:
            busqueda_por_ISBN(v)
        if opc == 6:
            consulta_por_genero(v)
        if opc == 7:
            consulta_precio_por_grupo(v)

        print("─"*60)
        input("Precione Enter para Continuar...")

# ─────────────────────────────────── SCRIPT ────────────────────────────────────────

if __name__ == '__main__':
    principal()



