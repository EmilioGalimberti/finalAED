#Resultados Al terminar el juego, el programa debe informar el nombre de cada jugador y su puntaje total.
#Además, debe indicar el nombre del ganador (o mostrar un mensaje informando que se produjo un empate)

#Entradas:

# ─────────────────────────────── INGRESO DE NOMBRE ───────────────────────────────────────────

jugador1 = input("Ingreso el nombre del jugador 1: ")
jugador2 = input("Ingreso el nombre del jugador 2: ")

jugador1 = jugador1.upper()
jugador2 = jugador2.upper()

# ────────────────────────────────── PRIMERA RONDA ──────────────────────────────────────────────────

import random

p1 = 0  #Puntaje Jugador 1
p2 = 0  #Puntaje Jugador 2


print("\n\n               J U E G O   D E   D A D O S                ")
print("=" * 60)

print("                     INICIO RONDA 1               ")
print("=" * 60)

# ────────────────────────────────── JUGADOR UNO (1) ──────────────────────────────────────────────────

print("TURNO DE ", jugador1)
print("-" * 60)

pause = input("PRESIONE ENTER PARA LANZAR LOS DADOS...")

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

print("\n» Dado 1: ", d1)
print("» Dado 2: ", d2)
print("» Dado 3: ", d3)

print("-" * 60)


if d1 == d2 == d3:
    p1 = 6
else:
    if d1 == d2 and d1 != d3 and d2 != d3: # D3 DISTINTO
        d3 = random.randint(1, 6)
        print("EL DADO 3 ES DISTINTO, AL TIRAR OTRA VEZ OBTENEMOS: ")
        print("\n» Dado 3: ", d3)
        if d1 == d2 == d3:
            p1 = 6
        else:
            p1 = 3
    if d2 == d3 and d2 != d1 and d3 != d1: # D1 DISTINTO
        d1 = random.randint(1, 6)
        print("EL DADO 1 ES DISTINTO, AL TIRAR OTRA VEZ OBTENEMOS:  ")
        print("\n» Dado 1: ", d1)
        if d1 == d2 == d3:
            p1 = 6
        else:
            p1 = 3

    if d3 == d1 and d3 != d2 and d1 != d2: # D2 DISTINTO
        d2 = random.randint(1, 6)
        print("EL DADO 2 ES DISTINTO, AL TIRAR OTRA VEZ OBTENEMOS: ")
        print("\n» Dado 2: ", d2)
        if d1 == d2 == d3:
            p1 = 6
        else:
            p1 = 3

if d1 != d2 and d1 != d3 and d2 != d3 :
    print("El Jugador 1 no suma puntos")



print("-" * 60)
print("\nPuntaje de ", jugador1,": ", p1)
print("")
print("=" * 60) #REVISAR ESTO CUANDO SE EJECUTE


# ────────────────────────────────── JUGADOR DOS (2) ──────────────────────────────────────────────────

print("TURNO DE ", jugador2)
print("-" * 60)

pause = input("PRESIONE ENTER PARA LANZAR LOS DADOS...")

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
d3 = random.randint(1, 6)

print("» Dado 1: ", d1)
print("» Dado 2: ", d2)
print("» Dado 3: ", d3)

print("-" * 60)


if d1 == d2 == d3:
    p2 = 6
else:
    if d1 == d2 and d1 != d3 and d2 != d3: # D3 DISTINTO
        d3 = random.randint(1, 6)
        print("EL DADO 3 ES DISTINTO, AL TIRAR OTRA VEZ OBTENEMOS: ")
        print("\n» Dado 3: ", d3)
        if d1 == d2 == d3:
            p2 = 6
        else:
            p2 = 3
    if d2 == d3 and d2 != d1 and d3 != d1: # D1 DISTINTO
        d1 = random.randint(1, 6)
        print("EL DADO 1 ES DISTINTO, AL TIRAR OTRA VEZ OBTENEMOS:  ")
        print("\n» Dado 1: ", d1)
        if d1 == d2 == d3:
            p2 = 6
        else:
            p2 = 3

    if d3 == d1 and d3 != d2 and d1 != d2: # D2 DISTINTO
        d2 = random.randint(1, 6)
        print("EL DADO 2 ES DISTINTO, AL TIRAR OTRA VEZ OBTENEMOS: ")
        print("\n» Dado 2: ", d2)
        if d1 == d2 == d3:
            p2 = 6
        else:
            p2 = 3

if d1 != d2 and d1 != d3 and d2 != d3 :
    print("El Jugador 2 no suma puntos")

print("-" * 60)
print("\nPuntaje de ", jugador2,": ", p2)
print("\n")
print("=" * 60)

# ────────────────────────────────── SEGUNDA RONDA ──────────────────────────────────────────────────

pause = input("\nPRESIONE ENTER PARA INICIAR RONDA DOS...")

print("\n                       INICIO RONDA 2                          ")
print("=" * 60)

# ────────────────────────────────── JUGADOR UNO (1) ──────────────────────────────────────────────────

Ptsr2j1 = 0

d1p = random.randint(1, 6)
d2p = random.randint(1, 6)
d3p = random.randint(1, 6)

#a y b

print("       TURNO DE ",jugador1, sep="")
print("-" * 60)

choicej1 = input("Eliga su apuesta a PAR O IMPAR: ")
choicej1 = choicej1.lower()
print("-" * 60)

resultado1 = (d1p + d2p + d3p)

if (resultado1 % 2) == 0:
    res = "par"
else:
    res = "impar"

dmax = max(d1p, d2p, d3p)
dmin = min(d1p, d2p, d3p)

print("")
print("La suma de los dados obtenidos es: ", res)

print("\n» Dado 1: ", d1p, sep="")
print("» Dado 2: ", d2p, sep="")
print("» Dado 3: ", d3p, sep="")

print("\n> El mayor de ellos es: ", dmax)
print("> El menor de ellos es: ", dmin)

if choicej1 == res:
    Ptsr2j1 = p1 + dmax
    print("Acertó su elección. SU PUNTAJE ES ", Ptsr2j1, sep="")
    if ((d1p % 2 ) == 0) and ((d2p % 2 ) == 0) and ((d3p % 2 ) == 0):       #c
        Ptsr2j1 = Ptsr2j1 * 2
        print("Acertó la elección y paridad, se duplica su puntaje, PUNTOS TOTAL: ", Ptsr2j1, sep="")
else:
    Ptsr2j1 = p1 - dmin
    print("No acertó la paridad elejida, PUNTOS TOTAL: ", Ptsr2j1, sep="")







# ────────────────────────────────── JUGADOR UNO (2) ──────────────────────────────────────────────────

Ptsr2j2 = 0

d1p = random.randint(1, 6)

d2p = random.randint(1, 6)

d3p = random.randint(1, 6)

#a y b

print("=" * 60)
print("       TURNO DE ",jugador2, sep="")
print("-" * 60)

choicej2 = input("Eliga su apuesta a PAR O IMPAR: ")
choicej2 = choicej2.lower()
print("-" * 60)

resultado1 = (d1p + d2p + d3p)

if (resultado1 % 2) == 0:
    res = "par"
else:
    res = "impar"

dmax = max(d1p, d2p, d3p)

dmin = min(d1p, d2p, d3p)

print("\n» Dado 1: ", d1p, sep="")
print("» Dado 2: ", d2p, sep="")
print("» Dado 3: " , d3p, sep="")

print("\n> El mayor de ellos es: ", dmax)
print("> El menor de ellos es: ", dmin)

print("")
print("La suma de los dados obtenidos es: ", res)

if choicej2 == res:
    Ptsr2j2 = p2 + dmax
    print("Acertó su elección. SU PUNTAJE ES ", Ptsr2j2, sep="")
    if ((d1p % 2 ) == 0) and ((d2p % 2 ) == 0) and ((d3p % 2 ) == 0):       #c
        Ptsr2j2 = Ptsr2j2 * 2
        print("Acertó la elección y paridad, se duplica su puntaje, PUNTOS TOTAL: ", Ptsr2j2, sep="")
else:
    Ptsr2j2 = p2 - dmin
    print("No acertó la paridad elejida, PUNTOS TOTAL: ", Ptsr2j2, sep="")

#repetir para jugador 2



# Final de juego
print("=" * 60)

print("» EL PUNTAJE DE ", jugador1," ES DE ", Ptsr2j1, " PUNTOS", sep="")
print("» EL PUNTAJE DE ", jugador2," ES DE ", Ptsr2j2, " PUNTOS", sep="")

if Ptsr2j1 == Ptsr2j2:
    print("EMPATE ENTRE LOS JUGADORES", sep="")
elif Ptsr2j1 > Ptsr2j2:
    print("» EL GANADOR ES ", jugador1, sep="")
else:
    print("» EL GANADOR ES ", jugador2, sep="")
