# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres.
# El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto
# está separada de las demás por un espacio en blanco. El programa debe:
#
# 1)      Determinar la cantidad de palabras que incluyen exactamente dos vocales.
# Por ejemplo, en el texto: “Los cursos del turno tarde.” Respuesta: 3 palabras.
# Las palabras que cumplen con la condición son: “cursos”, “turno” y “tarde”.
#
# 2)      Determinar el porcentaje de palabras en todo el texto que tienen una cantidad impar de caracteres.
#  Por ejemplo, en el texto: “Hoy es un lindo día.”
#  Respuesta: 60,00 % (palabras que cumplen la condición: 3 ("Hoy", "lindo" y "día") sobre un total de palabras de 5).
#
# 3)      Determinar cuántas palabras del texto inician con consonante y tienen más de 4 letras.
# Por ejemplo, en el texto: “Confiamos que aprueben el parcial.”
# Respuesta: 2 palabras. Las palabras que cumplen la condición son: “Confiamos” y “parcial”.
#
# 4)      Determinar cuántas palabras incluyen la expresión "sa" pero más de una vez.
# Por ejemplo, en el texto: “La salsa es muy sabrosa.”
# Respuesta: 2 palabras. Las palabras que cumple con la condición son: “salsa” y "sabrosa".

def es_vocal(caracter):
    return caracter in "aeiouáéíóú"


def es_consonante(caracter):
    return caracter in "bcdfghjklmnñpqrstvwxyz"


def calculo_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


texto = input("Ingrese el texto (debe finalizar con punto): ")
texto = texto.lower()

cont_letras = 0
cont_palabras = 0
car_anterior = " "

cant_vocales = 0
palabras_car_impares = 0
inicia_cons = False
cont_sa = 0

cpal_punto_1 = 0
cpal_punto_3 = 0
cpal_punto_4 = 0


for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1

        # Punto 1:

        if es_vocal(caracter):
            cant_vocales = cant_vocales + 1


        # Punto 3:

        if cont_letras == 1 and es_consonante(caracter):
            inicia_cons = True

        # Punto 4:

        if car_anterior == "s" and caracter == "a":
            cont_sa = cont_sa + 1


    else:
        if cont_letras > 0:
            cont_palabras += 1

        # Punto 1:

        if cant_vocales == 2:
            cpal_punto_1 = cpal_punto_1 + 1


        # Punto 2:
        if cont_letras % 2 != 0:
            palabras_car_impares = palabras_car_impares + 1


        # Punto 3:

        if inicia_cons and cont_letras > 4:
            cpal_punto_3 = cpal_punto_3 + 1


        # Punto 4:
        if cont_sa > 1:
            cpal_punto_4 = cpal_punto_4 + 1



        # Reiniciamos a false y cero:
        cant_vocales = 0
        inicia_cons = False
        cont_letras = 0
        cont_sa = 0

    car_anterior = caracter

porcentaje = calculo_porcentaje(palabras_car_impares, cont_palabras)

print("\n===============================================")
print("             TABLA DE RESULTADOS               ")
print("===============================================")

print("\n>> Hay ", cpal_punto_1, " palabras que contienen 2 vocales", sep="")
print("\n>> Hay ", palabras_car_impares, " palabras con cantidad impar de caracteres y representan un ", round(porcentaje, 2), "% de las palabras del texto", sep="")
print("\n>> Hay ", cpal_punto_3, " palabras que comienzan con consonante y tienen mas de 4 letras", sep="")
print("\n>> Hay ", cpal_punto_4, " palabras que contienen la expresión 'sa' más de una vez", sep="")


# Los cursos del turno tarde dijeron confiamos en que aprobamos el parcial pero en este lindo día vamos a preparar una salsa muy sabrosa.

# 8 - 15 y 68.18% - 11 - 2
