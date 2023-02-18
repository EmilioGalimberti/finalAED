from alquiler import *
import random


def mostrar_alquileres(titulo, v):
    print(titulo)
    print("-" * len(titulo))
    for alquiler in v:
        print(to_string(alquiler))


def ordenar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].importe > v[j].importe:
                v[i], v[j] = v[j], v[i]


descripciones = ["A", "B", "C", "D", "E", "F", "G"]


def cargar_alquileres(n):
    v = [None] * n

    for i in range(n):
        num = random.randint(1, 1000)
        descripcion = random.choice(descripciones)
        tipo = random.randint(0, 9)
        importe = random.uniform(1000, 10000)
        dias = random.randint(0, 30)
        v[i] = Alquiler(num, descripcion, tipo, importe, dias)

    return v


def contar_por_tipo(v):

    c = [0] * 10

    for alq in v:
        c[alq.tipo] += 1

    return c


# podria ir a un modulo de funciones generales
def mostrar_vector(v):
    for x in v:
        print(x)


def buscar(v, c, x):
    for alq in v:
        if alq.descripcion == c and alq.dias > x:
            return alq

    # Tecnicamente esto no hace falta
    return None


def filtrar_tipo_importe(v, x, z):
    filtrados = []

    for alq in v:
        if alq.tipo == x and alq.importe >= z:
            filtrados.append(alq)

    return filtrados


def promedio_importes(v):

    suma = 0

    # por cada alq del vector v:
    for alq in v:
        suma += alq.importe

    return suma / len(v)

