#1k07 Emilio Galimberti 90747 :)

#Turno 04 – Enunciado 02 [T4E2]:
#Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

#1.)    Ingrese el nombre de tres localidades turísticas e ingrese además la cantidad de turistas que recibió cada una.
# Detetermine el nombre de la localidad que recibió más turistas, e indique también con un mensaje la cantidad de turistas de
# esta esa localidad superó o no a la suma de las otras dos localidades juntas.

#2.)    Ingresar una secuencia de números, a razón de un número por vuelta de ciclo. La carga de dicha secuencia finaliza cuando se ingresa un cero.
# Determine cuántos números positivos pero menores a 180 se ingresaron. Además, determine el promedio de los números negativos. Por último muestre
# el porcentaje que representan los números positivos pero menores a 180 respecto del total de números leidos.

#3.)    Terminar el programa.


# Menu de opciones
opcion=None



while opcion != 3:
    print('=' * 15)
    print('MENU DE OPCIONES')
    print('=' * 15)
    print('Seleccione alguna de las opciones')
    print('>> 1. Localidades turisticas.')
    print('>> 2. Secuencia de numeros.')
    print('>> 3. Salir')
    opcion = int(input('\n>>Ingrese la opcion: '))
    print('=' * 15)

#1.)    Ingrese el nombre de tres localidades turísticas e ingrese además la cantidad de turistas que recibió cada una.
# Detetermine el nombre de la localidad que recibió más turistas, e indique también con un mensaje la cantidad de turistas de
# esta esa localidad superó o no a la suma de las otras dos localidades juntas.

    if opcion == 1:
        print('\nSe selecciono la opcion 1 ')

        localidad1 = input("\nIngrese el nombre de la primera localidad: ")
        cant1 = int(input("Ingrese la cantidad de turistas que recibio "+ localidad1 + ": "))

        localidad2 = input("\nIngrese el nombre de la segunda localidad: ")
        cant2 = int(input("Ingrese la cantidad de turistas que recibio "+ localidad2 + ": "))

        localidad3 = input("\nIngrese el nombre de la tercera localidad: ")
        cant3 = int(input("Ingrese la cantidad de turistas que recibio "+ localidad3 + ": "))

        if cant1 > cant2 and cant1 > cant3:
            may = cant1
            print("\nla localidad con mas turistas fue "+ str(localidad1)+" con una cantidad de: ",cant1," turistas")
            suma = cant2 + cant3
            if may > suma:
                print("\nEsta localidad supero la suma de las otras dos localidades juntas")
            else:
                print("\nEsta localidad NO supero la suma de las otras dos localidades juntas")
        elif cant2 > cant3:
            may = cant2
            print("\nla localidad con mas turistas fue "+ str(localidad2)+" con una cantidad de: ",cant2," turistas")
            suma = cant3 + cant1
            if may > suma:
                print("\nEsta localidad supero la suma de las otras dos localidades juntas")
            else:
                print("\nEsta localidad NO supero la suma de las otras dos localidades juntas")
        else:
            may = cant3
            print("\nla localidad con mas turistas fue "+str(localidad3)+" con una cantidad de: ",cant3," turistas")
            suma = cant1 + cant2
            if may > suma:
                print("\nEsta localidad supero la suma de las otras dos localidades juntas")
            else:
                print("\nEsta localidad NO supero la suma de las otras dos localidades juntas")

#2.)    Ingresar una secuencia de números, a razón de un número por vuelta de ciclo. La carga de dicha secuencia finaliza cuando se ingresa un cero.
# Determine cuántos números positivos pero menores a 180 se ingresaron. Además, determine el promedio de los números negativos. Por último muestre
# el porcentaje que representan los números positivos pero menores a 180 respecto del total de números leidos.

    elif opcion ==2:
        print('\nSe selecciono la opcion 2 ')
        conta = 0
        conta_positivos = 0
        conta_negativos = 0
        conta_total = 0
        acum_negativos = 0
        n = int(input("Ingrese el " + str(conta+1) + " numero de la secuencia: "))
        if n > 0 and n < 180:
            conta_positivos = conta_positivos + 1
        elif n < 0:
            conta_negativos = conta_negativos + 1
            acum_negativos = acum_negativos + n

        conta = conta + 1
        conta_total = conta_total + 1
        while n != 0:
            n = int(input("Ingrese el " + str(conta+1) + "° numero de la secuencia: "))
            conta_total = conta_total + 1
            if n > 0 and n < 180:
                conta_positivos = conta_positivos + 1
            elif n < 0:
                conta_negativos = conta_negativos + 1
                acum_negativos = acum_negativos + n
            conta = conta + 1

        promedio_negativos = acum_negativos / conta_negativos
        conta_total = conta_total - 1
        porcentaje_positivos = (conta_positivos * 100) / conta_total

        print("\n Se ingresaron ", conta_positivos, " numeros positivos menores a 180")
        print("El promedio de los negativos es: ", round(promedio_negativos, 2))
        print("Los de positivos menores a 180 representan un ", round(porcentaje_positivos, 2), "% respecto al total.")

    #3.)    Terminar el programa.

    elif opcion == 3:
        print('\nSALIO DEL PROGRAMA')
    else:
        print('\nOpcion incorrecta ingrese nuevamente')
