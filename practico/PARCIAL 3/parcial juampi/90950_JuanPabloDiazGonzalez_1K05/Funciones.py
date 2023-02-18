from Plantas import *

import random

# CARGA DE PLANTAS
nombres = ["Aloe", "Vera", "Cardón", "Espinas", "Carnivora", "Lira", "Ficus", "Lapacho", "Java", "Manzano", "Guayaba",
           "Bero"]


def carga_plantas(n):
    v = [None] * n
    for i in range(n):
        num = random.randint(1, 1000)
        nombre = random.choice(nombres)
        tipo = random.randint(0, 18)
        importe = random.uniform(10, 100)
        disponibles = random.randint(0, 10)
        v[i] = Plantas(num, nombre, tipo, importe, disponibles)
    return v


def mostrar_plantas(titulo, v):
    print(titulo)
    print('-' * len(titulo))
    for plantas in v:
        print(to_string(plantas))


# 2) orden

def ordenar(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].nombre > v[j].nombre:
                v[i], v[j] = v[j], v[i]


# Filtrado
def filtrar_tipo_importe(v, x):
    filtrado = []

    for plan in v:
        if plan.precio * plan.disponibles > x:
            filtrado.append(plan)

    return filtrado


# 3)
def acumular_disponibles(v):
    acumulador = [0] * 19
    for plan in v:
        acumulador[plan.tipo] += plan.disponibles
    return acumulador


# 4)

def promedio_disponibles(v):
    suma = 0
    for plan in v:
        suma += plan.disponibles
    return suma / len(v)

# 5)


def buscar(v, x):
    for plan in v:
        if plan.numero == x:
            return plan
    return None
