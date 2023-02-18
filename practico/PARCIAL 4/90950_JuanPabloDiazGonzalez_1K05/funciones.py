import random
from registro import *
import pickle
import os.path


def generar_articulos_random():
    nro = random.randint(1, 99)
    desc = "Descripción_" + str(nro)
    prec = random.randint(1, 900)
    pais = random.randint(0, 29)
    tipo = random.randint(0, 49)
    cant = random.randint(0, 3)
    art = Artículo(nro, desc, prec, pais, tipo, cant)
    return art


def add_in_order_articulos(vec, art):  # Búsqueda Binaria
    n = len(vec)
    pos = n
    izq = 0
    der = n-1
    while izq <= der:
        num = (izq + der) // 2
        if vec[num].numero == art.numero:
            pos = num
            break
        if art.numero < vec[num].numero:
            der = num - 1
        else:
            izq = num + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [art]

def menu1_generar_arreglo(n):
    vec = []
    for i in range(n):
        art = generar_articulos_random()
        add_in_order_articulos(vec, art)    # Se agrega al vector de forma ordenada
    return vec

def display(articulo):
    print('Numero de identficacion:', articulo.numero, '\t')
    print(' - descripcion:', articulo.descripcion, '\t')
    print(' - precio:', articulo.precio, '\t')
    print(' - pais', articulo.pais, '\t')
    print(' - tipo', articulo.tipo,'\t')
    print(' - cantidad', articulo.cantidad)



def mostrar_articulos(vec):
    for i in range(len(vec)):
        display(vec[i])


def buscar_lectura(articulos, codigo):
    izq, der = 0, len(articulos) - 1
    while izq <= der:
        num = (izq + der) // 2
        if codigo == articulos[num].numero:
            pos = num
            return pos
        elif codigo < articulos[num].numero:
            der = num - 1
        else:
            izq = num + 1
    return -1



# 4-----------------------------------------------
def crear_archivo(v,fn):
  m = open(fn, 'wb')
  for articulo in v:
    if articulo.cantidad != 0:
      pickle.dump(articulo,m)
  m.close()

# 5------------------------------------------


def mostrar_archivo(fd):
  if not os.path.exists(fd):
    print('El archivo no existe! ')
    return
  m = open(fd,'rb')
  tam = os.path.getsize(fd)
  while m.tell() < tam:
    articulo = pickle.load(m)
    display(articulo)
  m.close

