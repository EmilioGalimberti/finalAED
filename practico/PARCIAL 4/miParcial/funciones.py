import random
from registro import *
import pickle
import os.path



#1--------------------------------------------------------------

def generar_articulos_random():
    id = random.randint(1, 20)
    descripcion = "Descripción_" + str(id)
    precio = random.randint(1, 900)
    origen = random.randint(0, 20)
    tipo = random.randint(0, 49)
    art = Articulo(id, descripcion, precio, origen, tipo)
    return art

def add_in_order_articulos(vec, art):
    n = len(vec)
    pos = n
    izq = 0
    der = n-1
    while izq <= der:
        num = (izq + der) // 2
        if vec[num].id == art.id:
            pos = num
            break
        if art.id < vec[num].id:
            der = num - 1
        else:
            izq = num + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [art]

def generar_arreglo(n):
    vec = []
    for i in range(n):
        art = generar_articulos_random()
        add_in_order_articulos(vec, art)
    return vec

#2----------------------------------------------------------------


def to_string(a):  # Convierte a string la variable registro
    renglon = ''
    renglon += 'Numero de identifacion:{:>10}'.format(a.id)
    renglon += ' '
    renglon += 'Descripcion: {:<20}'.format(a.descripcion)
    renglon += ' '
    renglon += 'Precio: ${:>10}'.format(a.precio)
    renglon += ' '
    renglon += 'Origen:{:>10}'.format(a.origen)
    renglon += ' '
    renglon += 'Tipo:{:>10}'.format(a.tipo)
    return renglon


def mostrar(articulo):
    print('Numero de identficacion:', articulo.id, '\t')
    print(' >> Descripcion:', articulo.descripcion, '\t')
    print(' >> Precio:', articulo.precio, '\t')
    print(' >> Origen', articulo.origen, '\t')
    print(' >> Tipo', articulo.tipo,'\t')


def mostrar_articulos(v,p):
  for articulo in v:
    if articulo.origen != p:
      print(to_string(articulo))

#3-----------------

def buscar_articulo(articulos, codigo):
    izq, der = 0, len(articulos) - 1
    while izq <= der:
        num = (izq + der) // 2
        if codigo == articulos[num].id:
            pos = num
            return pos
        elif codigo < articulos[num].id:
            der = num - 1
        else:
            izq = num + 1
    return -1




# 4-----------------------------------------------
def crear_archivo(v,fn,tip):
  m = open(fn, 'wb')
  for articulo in v:
    if articulo.tipo != tip:
      pickle.dump(articulo,m)
  m.close()

# 5------------------------------------------

def contador_registro(v):
    total = 0
    for articulo in v:
      total += 1
      return total


def mostrar_archivo(v,fd):
  total = 0
  acum = 0
  if not os.path.exists(fd):
    print('El archivo no existe! ')
    return
  m = open(fd,'rb')
  tam = os.path.getsize(fd)
  while m.tell() < tam:
    articulo = pickle.load(m)
    mostrar(articulo)

  m.close()

