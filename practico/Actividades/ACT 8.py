#1. Menu de Opciones con secuencias
#Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones:

#a) Dada la serie de números naturales desde 1 hasta n (n ingresado por teclado y validando que sea mayor a cero) mostrar
 #la suma de los cuadrados

#b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales

#c) Ingresar una serie de números (la carga finaliza con cero) y determinar
#si hay mayor cantidad de valores pares o de impares

#d) Salir


#interfaz de usuario

def es_vocal(caracter):
    return caracter in "aeiouáéíóú"

def text():

    texto = input("Ingrese el texto (debe finalizar con punto): ")

    cont_letras = 0
    cont_palabras = 0
    c_palabras = 0
    caracter_anterior = " "



    for caracter in texto:
        # cant de palabras q termian en vocal

        if caracter != " " and caracter != ".":
            cont_letras += 1



        else:
            if cont_letras > 0:
                cont_palabras += 1

            if caracter == " " or caracter == "." and es_vocal(caracter_anterior): #palabras que finalizan en vocal
                c_palabras = c_palabras + 1


        cont_letras = 0
        caracter_anterior = caracter

    print("Hay ", c_palabras, " que terminan en vocal.")
    return




def menu():
    print("Menu de opciones.")
    opcion = None
    while opcion != 4:
        print('1. ')
        print('2. cant vocales')
        print('3. ')
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
    text()
    return

def opcion3():

    return



#problemas y subproblemas

# script principal...
menu()
