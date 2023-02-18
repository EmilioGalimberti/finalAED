__author__ = 'Emilio Galimberti'

from registro import *
import random


# 1) CARGA----------------------------------


t_codigos = "Bahamas", "Bermudas", "Puerto Rico", "República Dominicana"

def carga_pasajes(n):
    v = [None] * n
    nombres = ['Agustin', 'Bruno', 'Joaquin', 'Daniel']
    for i in range(n):
        pasaporte = random.randint(500,1000)
        nombre = random.choice(nombres)
        codigo_destino = random.choice(t_codigos)
        codigo_clase = random.randint(1,10)
        monto = round(random.random()*4500+500,2)
        v[i] = pasaje(pasaporte, nombre, codigo_destino, codigo_clase, monto )
    return v

#2)-----------------------------
def ordenar(v): #para ordenar va a ser siempre igual de forma directa de menor  a mayor
    n = len(v) # n = 4
    # 1er ciclo se utiliza para considerar el elemento pivot en la pasada.
    for i in range(n-1):# Rango: 0 1 2
        # 2do ciclo se utiliza para comparar con los demás elementos del arreglo.
        for j in range(i+1, n): # Rango: 1 2 3 \ es i+1 porque no toma en cuneta el pivot
            if v[i].monto < v[j].monto: # v[i]=pivot v[j]:elem. actual con el cual estoy comparando. en este caso comporamos los importes para el punto 2)
               v[i] , v[j] = v[j] , v[i] # Intercambio.-

def mostrar_pasajes(titulo, v):
    print(titulo)
    print('=' * len(titulo * 2))
    for pasaje in v:
        print(to_string(pasaje))



#3------------------- Acum------------
def acumular_recaudacion(v):
    acumulador = [0] * 11
    for pasj in v:
        acumulador[pasj.codigo_clase] += pasj.monto
    return acumulador


def mayor(v):
    may_rec = None
    for clase in v:
        if may_rec is None:
            may_rec = clase
        elif clase > may_rec:
            may_rec = clase
    return may_rec

#4)))
def promedio_importes(v): #promedio general de un vector
    acum = 0
    suma = 0
    promedio = 0
    # por cada alq del vector v hago tal cosa, alq se puede cambiar por cualquier otra variable
    for pasj in v:                                                                               #este for es para un recorrido comun de 0 a
        if pasj.codigo_clase == 3:
            suma = suma + 1
            acum = acum + pasj.monto
            promedio = acum / suma
    return promedio

def filtrar_tipo_clase(v,promedio):
    filtrado = []

    for pasj in v:
        if pasj.codigo_clase == 3 and pasj.monto >= promedio:
            filtrado.append(pasj)
    return filtrado
#5))
def buscar(v,pasaporte):
    for pasj in v:
        if pasj.pasaporte == pasaporte :
            return pasj
    return None


