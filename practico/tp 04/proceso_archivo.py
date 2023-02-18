import random
import os.path

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


class Libro:
    def __init__(self, tit, cant, ano, cod, rat, isbn):
        self.titulo = tit
        self.cantidad_revisiones = cant
        self.ano_publicacion = ano
        self.codigo_idioma = cod # (un valor entre 1 y 27)
        self.rating = rat
        self.isbn = isbn

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def procesar_archivo(nom_archivo):

    # Verificar si el archivo existe y si no existe cortar
    if not os.path.exists(nom_archivo):
        print('\n((( Error: el arhivo no existe. )))\n')
        return None

    archivo = open("libros.csv", mode="rt", encoding="utf8")

    vector = []
    contador = 0
    print('Cargando libros...\n')
    # Comienzo a leer línea por línea el archivo de texto
    for linea in archivo:
        contador += 1
        #  para no considerar la línea de encabezados
        if contador > 1:
            # eliminar el '\n' del final.
            if linea[-1] == '\n':
                linea = linea[:-1]

            # obtener vector de cadenas con cada cadena separada
            cadenas = separar_texto(linea, separador=',')

            # crear el registro
            reg = Libro(cadenas[0], cadenas[1], cadenas[2], cadenas[3], cadenas[4], cadenas[5])

            # agregar el registro al vector
            add_in_order(vector, reg)

    archivo.close()
    print('((( Se cargaron', contador - 1, 'libros. )))')
    return vector

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


# Inserccion ordenada por búsqueda binaria.
def add_in_order(p, libro):
    n = len(p)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].isbn == libro.isbn:
            pos = c
            break

        if libro.isbn < p[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    p[pos:pos] = [libro]

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


# Separar las lineas de texto en un vector
def separar_texto(linea, separador):
    # Inicializo
    cadenas = []
    cadena_actual = ''

    for car in linea:
        if car != separador:
            cadena_actual += car
        else:
            cadenas.append(cadena_actual)
            cadena_actual = ''

    if linea[-1] != separador:
        cadenas.append(cadena_actual)

    return cadenas

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def decada(i, num):
    if i == 0:
        print('- La decada del 1900:', num)
        return
    if i == 1:
        print('- La decada del 1910:', num)
        return
    if i == 2:
        print('- La decada del 1920:', num)
        return
    if i == 3:
        print('- La decada del 1930:', num)
        return
    if i == 4:
        print('- La decada del 1940:', num)
        return
    if i == 5:
        print('- La decada del 1950:', num)
        return
    if i == 6:
        print('- La decada del 1960:', num)
        return
    if i == 7:
        print('- La decada del 1970:', num)
        return
    if i == 8:
        print('- La decada del 1980:', num)
        return
    if i == 9:
        print('- La decada del 1990:', num)
        return

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def to_string(p):
    r = ''
    r += '{:<93}'.format('| Título: ' + str(p.titulo))
    r += '{:<32}'.format('| Cantidad de revisiones: ' + p.cantidad_revisiones)
    r += '{:<27}'.format('| Año de publicación: ' + str(p.ano_publicacion))
    r += '{:<22}'.format('| Código de idioma: ' + str(p.codigo_idioma))
    r += '{:<15}'.format('| Rating: ' + str(p.rating))
    r += '{:<14}'.format('| ISBN: ' + str(p.isbn) + ' |')
    return r

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


# funcion para validar entre que años está la fecha del libro.
def intervalo_fecha(valor, inf, sup):
    if valor >= inf and valor <= sup:
        return True
    return False

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


# funcion para enlistar y mostrar los contadores.
def mostrar_cont(cont):
    print('\nLibros publicados en: ')
    n = len(cont)
    may = 0
    pos = -1
    for i in range(n):
        if cont[i] > may:
            may = cont[i]
            pos = i

    for i in range(n):
        if cont[i] != 0:
            decada(i, cont[i])

    if pos != -1:
        if pos == 0:
            print('\n((( La decada del 1900 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 1:
            print('\n((( La decada del 1910 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 2:
            print('\n((( La decada del 1920 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 3:
            print('\n((( La decada del 1930 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 4:
            print('\n((( La decada del 1940 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 5:
            print('\n((( La decada del 1950 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 6:
            print('\n((( La decada del 1960 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 7:
            print('\n((( La decada del 1970 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 8:
            print('\n((( La decada del 1980 tiene la mayor cantidad de publicaciones. )))\n')
        if pos == 9:
            print('\n((( La decada del 1990 tiene la mayor cantidad de publicaciones. )))\n')
    return

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def indice_ano(i):
  j = 2000 + i
  return j

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def chistes():
  chiste = ['\nChiste 1\n- ¿Tienes WiFi? \n- Sí \n- ¿Y cuál es la clave? \n- Tener dinero y pagarlo.\n','\nChiste 2\n-¿Qué pasa si tiras un pato al agua?\n-Nada...\n','\nChiste 3\n- Mamá, ¿qué haces en frente de la computadora con los ojos cerrados? \n- Nada, hijo, es que Windows me dijo que cerrara las pestañas\n']
  print('\nUn chiste hasta procesar la matriz de libros. :)')
  print(random.choice(chiste))

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


# Funcion para calcular el promedio de las revisiones por idioma.
def prom_idioma(libros, idioma):
    n = len(libros)
    sumador = 0
    cont = 0
    for i in range(n):
        if idioma == libros[i].codigo_idioma:
            cont += 1
            sumador += int(libros[i].cantidad_revisiones)
            # print(to_string(libros[i]))
    return sumador / cont

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
