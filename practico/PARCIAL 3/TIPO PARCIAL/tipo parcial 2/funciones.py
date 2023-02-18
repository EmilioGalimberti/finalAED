from alquiler import *

import random #para carga automatica

#1) Carga entra N (cant compontes, cant de alquileres) y  retorna un vector

descripciones = ['A', 'B', 'C', 'D', 'E', 'F', 'G'] #vector con descripciones para que puede elegir una descripcion alateoria el programa

def carga_alquileres(n):  #carga automatica
    v = [None] * n
    for i in range(n):
        num = random.randint(1,1000)
        descripcion = random.choice(descripciones)
        tipo = random.randint(0,9)
        importe = random.uniform(1000,10000)
        dias = random.randint(0,30)
        v[i] = Alquiler(num, descripcion, tipo, importe, dias)
    return v


#2) muestra del vector y ordenamiento de importes
#se usa to stirng de modulos

def ordenar(v): #para ordenar va a ser siempre igual de forma directa de menor  a mayor
    n = len(v) # n = 4
    # 1er ciclo se utiliza para considerar el elemento pivot en la pasada.
    for i in range(n-1):# Rango: 0 1 2
        # 2do ciclo se utiliza para comparar con los demás elementos del arreglo.
        for j in range(i+1, n): # Rango: 1 2 3 \ es i+1 porque no toma en cuneta el pivot
            if v[i].importe > v[j].importe: # v[i]=pivot v[j]:elem. actual con el cual estoy comparando. en este caso comporamos los importes para el punto 2)
               v[i] , v[j] = v[j] , v[i] # Intercambio.-

def mostrar_alquileres (titulo, v):     #siempre va a ser igual para mostrar un vector completo
    print(titulo)
    print('-'* len(titulo))
    for alquileres in v:
        print(to_string(alquileres))


# 3)
def contar_por_tipo(v):
    c = [0] * 10  #vector de conteo, se pone 10 , porque puede ver 9 de tipos de autos
    for alq in v:
        c[alq.tipo] += 1
    return c
#Funcion general para mostrar cualquier vecotr
def mostrar_vector(v):
    for x in v:
        print(x)


#4)
def buscar(v,c,x):
    for alq in v:
        if alq.descripcion == c and alq.dias >= x:
            return alq
    return None #tecnicamente no hace falta

#5) Filtrado
def filtrar_tipo_importe(v,x,z):
    filtrado = []

    for alq in v:
        if alq.tipo == x and alq.importe >= z:
            filtrado.append(alq)

    return filtrado

def promedio_importes(v): #promedio general de un vector
    suma = 0
    # por cada alq del vector v hago tal cosa, alq se puede cambiar por cualquier otra variable
    for alq in v:                                                                               #este for es para un recorrido comun de 0 a
        suma += alq.importe
    return suma / len(v)


#usamos los for con range cuando tengo que modificar el vector, por ejemplo en la carga, necesito el indice
#
