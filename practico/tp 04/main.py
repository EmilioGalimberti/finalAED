import pickle
import os
import os.path
from proceso_archivo import *


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# OPTION 7


def mostrar_archivo():
  global DAT
  if not os.path.exists(DAT):
    print('((( El archivo no existe. )))')
    return
  m = open(DAT,'rb')
  tam = os.path.getsize(DAT)
  while m.tell() < tam:
    populares = pickle.load(m)
    print(to_string(populares))
  m.close()
  return

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# OPTION 6


def guardar_populares(matriz):
  global DAT
  m = open(DAT,'wb')
  cont = 0
  if not matriz:
    print('\n((( La matriz no fue generada. )))\n')
    return

  filas, columnas = len(matriz), len(matriz[0])

  for f in range(filas):
    for c in range(columnas):
      if matriz[f][c] != 0:
        pickle.dump(matriz[f][c],m)
        cont += 1

  print('→ ¡Se guardaron ', cont,' registros! ←')
  m.close()
  return


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# OPTION 5


def publicaciones_por_decada(libros):
    if len(libros) == 0:
        print('\n((( No hay datos cargados. )))\n')
        return

    n = len(libros)
    cont = [0] * 10

    for i in range(n):
        if intervalo_fecha(int(libros[i].ano_publicacion), 1900, 1909):
            cont[0] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1910, 1919):
            cont[1] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1920, 1929):
            cont[2] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1930, 1939):
            cont[3] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1940, 1949):
            cont[4] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1950, 1959):
            cont[5] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1960, 1969):
            cont[6] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1970, 1979):
            cont[7] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1980, 1989):
            cont[8] += 1
        if intervalo_fecha(int(libros[i].ano_publicacion), 1990, 2000):
            cont[9] += 1

    mostrar_cont(cont)
    return



# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# OPTION 4


def popularidad_2000(libros):
    n = 27
    m = 21
    y = len(libros)

    print('\n> Generando matriz...')
    matriz = [[0] * m for f in range(n)]

    # Agregado para hacer mas amena la espera.
    chistes()

    for i in range(n):
        for c in range(m):
            may = 0
            pos = 0
            encontrado = False
            for u in range(y):
                if int(libros[u].codigo_idioma) == i+1:
                    if int(libros[u].ano_publicacion) == indice_ano(c):
                        if float(libros[u].rating) > float(may):
                            may = float(libros[u].rating)
                            pos = u
                            encontrado = True
            if encontrado:
                matriz[i][c] = libros[pos]
    return matriz





# Funcion para corroborar el funcionamiento de la funcion "popularidad_2000"
''' 
def display_count(matriz):
    filas, columnas = len(matriz), len(matriz[0])

    print('\n Matriz de libros por Idioma y Año de publicación:\n')
    for f in range(filas):
        count = 0
        for c in range(columnas):
            count += 1
            print('[ Idioma:', f+1, ' | Año de publicación:', 2000 + c, ' ]   ->   Rating:', matriz[f][c])
            if count == 21:
                print()
'''

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# OPTION 3

def mayor_revisiones(libros):
    if len(libros) == 0:
        print('\n((( No hay datos cargados. )))\n')
        return

    n = len(libros)
    may = 0
    pos = 0
    for i in range(n):
        if int(libros[i].cantidad_revisiones) > may:
            may = int(libros[i].cantidad_revisiones)
            pos = i

    print('\nLibro de mayor num de revisiones:')
    print(to_string(libros[pos]))
    promedio = prom_idioma(libros, libros[pos].codigo_idioma)

    if int(libros[pos].cantidad_revisiones) > promedio:
        print('\n((( El líbro posee MAYOR num de revisiones que el promedio de su idioma. )))\n')
    if int(libros[pos].cantidad_revisiones) < promedio:
        print('\n((( El líbro posee MANOR num de revisiones que el promedio de su idioma. )))\n')
    if int(libros[pos].cantidad_revisiones) == promedio:
        print('\n((( El líbro posee IGUAL num de revisiones que el promedio de su idioma. )))\n')
    return




# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
# OPTION 2


def buscar(libros, search, method):
    if len(libros) == 0:
        print('\n((( No hay datos cargados. )))\n')
        return
    # 0060920084

    # Busqueda por Titulo mediante Busqueda Directa
    if method == 1:
        n = len(libros)
        encontrado = False
        for i in range(n):
            if search == libros[i].titulo:
                libros[i].cantidad_revisiones = str(int(libros[i].cantidad_revisiones)+1)  # Suma de revision +1
                print(to_string(libros[i]))
                encontrado = True
        if not encontrado:
            print('\n((( Título NO encontrado. )))\n')
        return

    # Busqueda por ISBN mediante Busqueda Binaria
    if method == 2:
        n = len(libros)
        izq, der = 0, n - 1
        while izq <= der:
            c = (izq + der) // 2
            if libros[c].isbn == search:
                print('ISBN encontrado:')
                libros[c].cantidad_revisiones = str(int(libros[c].cantidad_revisiones)+1)  # Suma de revision +1
                print(to_string(libros[c]))
                print()
                return

            if search < libros[c].isbn:
                der = c - 1
            else:
                izq = c + 1

    print('\n((( ISBN NO encontrado... )))\n')
    return

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def menu():
    c = '─'*60
    c += '\n|             TRABAJO PRACTICO   N ° 4    A E D            |\n'
    c += '─'*60
    c += '\n> > > REFERENCIA DE OPCIONES:\n'
    c += '1.) Cargar en Vector Registros de Libros.\n'
    c += '2.) Buscar por Título o ISBN.\n'
    c += '3.) Libro de mayor Revisiones que cumpla condiciones.\n'
    c += '4.) Generar matriz de Popularidad 2000-2020.\n'
    c += '5.) Listar cantidad de Publicaciones por década.\n'
    c += '6.) Guardar matriz de libros populares en nuevo archivo.\n'
    c += '7.) Mostrar archivo.\n'
    c += '8.) Salir.\n'
    c += '─'*60
    return c

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


def principal():
    global FD
    global DAT
    archivo_creado = False
    FD = 'libros.csv'
    DAT = 'populares.dat'
    libros = []
    matriz = []
    search = 0
    opc = -1
    while opc != 8:
        print(menu())
        opc = int(input('> Ingrese N° de Opcion a Ejecutar: '))
        print('─'*60)

        if opc == 1:
            libros = procesar_archivo(FD)

        elif opc == 2:
            print('Opciones de Busqueda:\n\t1 -> Busqueda por TÍTULO. \n\t2 -> Busqueda por ISBN.')
            method = int(input('\n> Seleccione el metodo de busqueda: '))
            if method == 1:
                search = input('\n>> Título a buscar: ')
            elif method == 2:
                search = input('\n>> Número de isbn a buscar: ')
            elif method != 2:
                print('\n((( Ingrese un método de busqueda. )))\n')

            buscar(libros, search, method)

        elif opc == 3:
            mayor_revisiones(libros)

        elif opc == 4:
            matriz = popularidad_2000(libros)
            print('─'*60)
            print(" → ¡Matriz generada exitosamente! ←")


        elif opc == 5:
            publicaciones_por_decada(libros)

        elif opc == 6:
            guardar_populares(matriz)
            if os.path.exists(DAT):
              print('((( El archivo fue creado exitosamente. )))')


        elif opc == 7:
            if os.path.exists(DAT):
              print('Contenido del archivo (en caso de estar vacío no se mostrará ninguna lectura)')
              mostrar_archivo()
            else:
              print('\n((( El archivo', DAT, 'no existe. )))\n')

        elif opc == 8:
            print('¡Finalizo correctamente el programa! :) ¡Que tenga buen dia!')

        elif opc != 8:
            print('\n(( Por favor Ingrese un Número Valido de Opcion. ))\n')

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    principal()
