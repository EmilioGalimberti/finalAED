def es_vocal(caracter):
    return caracter in "aeiouáéíóú"

def es_consonante(caracter):
    return caracter in "bcdfghjklmnñpqrstvwxyz"

def es_digito(caracter):
    return caracter in "0123456789"

def calculo_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje

def palabra_mayor_4_letras(texto):
        cont_letras = 0
        cont_palabras = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
            else:
                if cont_letras > 4:         #contador palabra con mas de 4 letras
                    cont_palabras += 1
                cont_letras = 0
        return cont_palabras

def menu():
    print("Menu de opciones.")
    opcion = None
    while opcion != 4:
        print('1. Impares multiplos de 3')
        print('2. Primos en un intervalo')
        print('3. Secuencia ordenada')
        print('4. Salir')
        opcion = int(input('Ingrese el numero de la opcion elegida: '))
        # chequeo de la opcion elegida...
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()

def opcion1():

    return

def opcion2():

    return

def opcion3():

    return



#problemas y subproblemas

# script principal...
menu()
