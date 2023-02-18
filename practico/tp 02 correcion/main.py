'''

TRABAJO PRACTICO 02
ALGORITMOS Y ESTRUCTURA DE DATOS

INTEGRANTES
 ►  Díaz González, Juan Pablo           Curso: 1K05  (90950)
 ►  Galimberti, Emilio                  Curso: 1K07  (90747)
 ►  Ontivero Capello, Gabriel Nicolás   Curso: 1K06  (91297)

'''

import random

puntaje_J1 = 0  # Puntaje Jugador 1.
puntaje_J2 = 0  # Puntaje Jugador 2.

suma_puntaje_J1 = 0  # Suma de los puntajes  de todas las rondas del Jugador 1.
suma_puntaje_J2 = 0  # Suma de los puntajes  de todas las rondas del Jugador 2.

wins_consecutivas_J1 = 0  # Contador de partidas ganadas consecutivamente por el Jugador 1.
wins_consecutivas_J2 = 0  # Contador de partidas ganadas consecutivamente por el Jugador 2.

aciertos_J1 = 0  # Aciertos de paridad de suma de los dados del Jugador 1.
aciertos_J2 = 0  # Aciertos de paridad de suma de los dados del Jugador 2.

hubo_empate = False  # Determinar si hubo al menos un empate.

racha_J1 = False  # Bandera de racha de victorias del Jugador 1.
racha_J2 = False  # Bandera de racha de victorias del Jugador 1.

cont_partidas = valor = 0

# ───────────────────────────────────────────── FUNCIONES  ────────────────────────────────────────────────────


def dado_random():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        d3 = random.randint(1, 6)
        return  d1,d2,d3


def paridad(choice):
    while choice != "par" and choice != "impar":
        choice = input("\nEscriba su apuesta (PAR O IMPAR): ")
        choice = choice.lower()
        if choice != "par" and choice != "impar":
            print("(((   Por favor ingrese una opcion sugerida.   )))")
    return choice


def fun_calculos(aciertos, puntaje, partidas):
    porcent = (aciertos * 100) / partidas       # Calculo de porcentaje de aciertos
    prom = puntaje / partidas       # Cálculo del promedio de puntajes en las rondas
    return porcent, prom

# ───────────────────────────────────────── SCRIPT PRINCIPAL ──────────────────────────────────────────────────


print("=" * 60)
print("             J U E G O   D E   D A D O S   2.0              ")
print("=" * 60)

# Ingreso de nombres por Jugador.
jugador1 = input("\n» Ingrese el nombre del Jugador 1: ")
jugador2 = input("\n» Ingrese el nombre del Jugador 2: ")
jugador1 = jugador1.upper()
jugador2 = jugador2.upper()

while valor <= 4:
    valor = int(input("\n» ¿A cuantos puntos se desea el juego? (mayor a 10 pts): "))
    if valor <= 4:
        print("(((   Error. Por favor ingrese un valor mayor a 10.   )))")

while puntaje_J1 < valor and puntaje_J2 < valor:
    print("")
    print("=" * 60)
    print("                    INICIO DE RONDA", cont_partidas + 1)
    print("=" * 60)

# ────────────────────────────────────────── JUGADOR UNO (1) ──────────────────────────────────────────────────

    # Asignación de valores al zar por dado.
    dado1, dado2 , dado3 = dado_random()

    print("»»» TURNO DE", jugador1)
    print("=" * 60)

    choice = 0
    choice = paridad(choice)
    print("-" * 60)

    # Suma de los dados tirados.
    res_suma = dado1 + dado2 + dado3

    # Verificación de paridad de la suma de los dados.
    if (res_suma % 2) == 0:
        res = "par"
    else:
        res = "impar"

    # Asignación del valor menor y mayor lanzados.
    dmax = max(dado1, dado2, dado3)
    dmin = min(dado1, dado2, dado3)

    # Muestra de valores de los dados.
    print("\n» Dado 1: ", dado1)
    print("» Dado 2: ", dado2)
    print("» Dado 3: ", dado3)
    print("")
    print("-" * 60)

    print("\n> El mayor de ellos es: ", dmax)
    print("> El menor de ellos es: ", dmin)

    print("\n> Suma de valores: ", dado1, "+", dado2, "+", dado3, "=", res_suma)
    print("> La suma de los dados obtenidos es: ", res)

    if choice == res:    # Verificacion de acierto de apuesta de la paridad de la suma de los dados.
        puntaje_J1 += dmax
        print("\n> ¡¡Acertó su elección!! Suma ", dmax, " al puntaje.")
        aciertos_J1 += 1  # Conteo de aciertos
        if ((dado1 % 2) == 0) and ((dado2 % 2) == 0) and (
                (dado3 % 2) == 0):     # Verificacion de paridad igualitaria en cada dado.
            puntaje_J1 *= 2
            print("> ¡¡Acertó la paridad de los dados!! Se duplica su puntaje.")
    else:
        puntaje_J1 -= dmin
        print("\n> ¡No acertó la paridad elejida! Resta ", dmin, " al puntaje.")

    print("")
    print("-" * 60)
    print("\nPuntaje de", jugador1, ": ", puntaje_J1)

# ────────────────────────────────────────── JUGADOR UNO (2) ──────────────────────────────────────────────────

    # Asignación de valores al zar por dado.
    dado1, dado2 , dado3 = dado_random()

    print("")
    print("=" * 60)
    print("»»» TURNO DE", jugador2)
    print("=" * 60)

    choice = 0
    choice = paridad(choice)
    print("-" * 60)

    # Suma de los dados tirados.
    res_suma = (dado1 + dado2 + dado3)

    # Verificación de paridad de la suma de los dados.
    if (res_suma % 2) == 0:
        res = "par"
    else:
        res = "impar"

    # Asignación del valor menos y mayor lanzados.
    dmax = max(dado1, dado2, dado3)
    dmin = min(dado1, dado2, dado3)

    # Muestra de valores de los dados
    print("\n» Dado 1: ", dado1)
    print("» Dado 2: ", dado2)
    print("» Dado 3: ", dado3)
    print("")
    print("-" * 60)

    print("\n> El mayor de ellos es: ", dmax)
    print("> El menor de ellos es: ", dmin)

    print("\n> Suma de valores: ", dado1, "+", dado2, "+", dado3, "=", res_suma)
    print("> La suma de los dados obtenidos es: ", res)

    if choice == res:     # Verificacion de acierto de apuesta de la paridad de la suma de los dados.
        puntaje_J2 += dmax
        print("\n> ¡¡Acertó su elección!! Suma ", dmax, " al puntaje.")
        aciertos_J2 += 1  # Conteo de aciertos
        if ((dado1 % 2) == 0) and ((dado2 % 2) == 0) and (
                (dado3 % 2) == 0):      # Verificacion de paridad igualitaria en cada dado.
            puntaje_J2 *= 2
            print("> ¡¡Acertó la paridad de los dados!! Se duplica su puntaje.")
    else:
        puntaje_J2 -= dmin
        print("\n> ¡No acertó la paridad elejida! Resta ", dmin, " al puntaje.")

    print("")
    print("-" * 60)
    print("\nPuntaje de", jugador2, ": ", puntaje_J2)
    print("")
    print("=" * 60)

# ──────────────────────────────────── CONTADORES Y BANDERAS ──────────────────────────────────────────────────

    if puntaje_J1 == puntaje_J2:
        print("\n--------->    Los Jugadores empataron la ronda    <---------")
        hubo_empate = True      # Bandera de empate en alguna partida.
    else:
        if puntaje_J1 > puntaje_J2:
            print("\n------->    Gana la ronda", jugador1, "con", puntaje_J1, "pts    <-------")
            if racha_J1:  # Contador de partidas ganadas consecutivamente.
                wins_consecutivas_J1 += 1
            racha_J1 = True
            racha_J2 = False

        if puntaje_J1 < puntaje_J2:
            print("\n------->    Gana la ronda", jugador2, "con", puntaje_J2, "pts    <-------")
            if racha_J2:  # Contador de partidas ganadas consecutivamente.
                wins_consecutivas_J2 += 1
            racha_J1 = False
            racha_J2 = True


    # Contador de partidas jugadas.
    cont_partidas += 1

    # Acumulador de puntajes por Jugador.
    suma_puntaje_J1 += puntaje_J1
    suma_puntaje_J2 += puntaje_J2

# ───────────────────────────────────────── MUESTRA DE RESULTADOS ─────────────────────────────────────────────

print("")
print("=" * 60)
print("        T A B L E R O   D E   R E S U L T A D O S                ")
print("=" * 60)
print("\n» PUNTAJE TOTAL DE", jugador1, ": ", puntaje_J1, " PUNTOS")
print("» PUNTAJE TOTAL DE", jugador2, ": ", puntaje_J2, " PUNTOS")
print("")
print("=" * 60)

if puntaje_J1 == puntaje_J2:
    print("»»» ¡¡¡EMPATE ENTRE LOS JUGADORES", "!!!")
else:
    if puntaje_J1 > puntaje_J2:
        print("»»» ¡¡¡EL GANADOR ES", jugador1, "!!!")
    else:
        print("»»» ¡¡¡EL GANADOR ES", jugador2, "!!!")
print("=" * 60)

print("\n> Cantidad de jugadas realizadas:", cont_partidas)

if hubo_empate:
    print("> SI hubo un empate en alguna de las jugadas.")
else:
    print("> NO hubo un empate en las jugadas.")

# Asignación de los valores de la función.
porcent_aciertos_J1, prom_J1 = fun_calculos(aciertos_J1, suma_puntaje_J1, cont_partidas)
porcent_aciertos_J2, prom_J2 = fun_calculos(aciertos_J2, suma_puntaje_J2, cont_partidas)

print("> Puntaje promedio obtenido por jugada de", jugador1, ":", round(prom_J1, 2))
print("> Puntaje promedio obtenido por jugada de", jugador2, ":", round(prom_J2, 2))
print("> Porcentaje de aciertos de", jugador1, ":", round(porcent_aciertos_J1), "%")
print("> Porcentaje de aciertos de", jugador2, ":", round(porcent_aciertos_J2), "%")

# Indicar  si el ganador es el que tuvo mayor porcentaje de aciertos.
if puntaje_J1 > puntaje_J2:
    if porcent_aciertos_J1 > porcent_aciertos_J2:
        print("> El ganador SI obtuvo el mayor porcentaje de aciertos.")
    else:
        print("> El ganador NO obtuvo el mayor porcentaje de aciertos.")
if puntaje_J1 < puntaje_J2:
    if porcent_aciertos_J1 < porcent_aciertos_J2:
        print("> El ganador SI obtuvo el mayor porcentaje de aciertos.")
    else:
        print("> El ganador NO obtuvo el mayor porcentaje de aciertos.")

# Muestra de qué jugador obtuvo 3 victorias consecutivas.
if wins_consecutivas_J1 > 3 and wins_consecutivas_J2 > 3:
    print("> Ambos jugadores consiguieron ganar 3 rondas consecutivas.")
else:
    if wins_consecutivas_J1 > 3:
        print("> El jugador", jugador1, "consiguió ganar 3 rondas consecutivas.")
    else:
        if wins_consecutivas_J2 > 3:
            print("> El jugador", jugador2, "consiguió ganar 3 rondas consecutivas.")
        else:
            print("> Ningún Jugador consiguió ganar 3 rondas consecutivas.")
print("")
print("-" * 60)

input("\n\nJuego finalizado...")

# ─────────────────────────────────────────── FIN DEL JUEGO ───────────────────────────────────────────────────
