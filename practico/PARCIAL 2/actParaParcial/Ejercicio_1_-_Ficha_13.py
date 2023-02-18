# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en
# una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario
# cargará el punto para indicar el final del texto, y que cada palabra de ese texto está separada
# de las demás por un espacio en blanco. El programa debe:
#
#   1 - Determinar la cantidad de palabras que terminan con la tercer letra de la primera palabra del texto.
#   Por ejemplo, en el texto: “Las casas se terminaron antes de lo previsto.”
#   Tiene 2 palabras que cumplen con la condición: “casas” y “antes”.
#
#   2 - Determinar la cantidad palabras que tienen vocales en la segunda mitad de la palabra y cuya longitud
#   sea mayor o igual a 5 letras. Por ejemplo, en el texto “Las materias de la facultad en cuarentena se rinden en aula virtual.”
#   Tiene 5 palabras que cumplen con la condición: “materias”, “facultad”, “rinden”, ”cuarentena” y “virtual”.
#
#   3 - Determinar la cantidad de palabras de longitud impar que se encuentran en el texto y que comienzan con una consonante.
#   Por ejemplo, en el texto: “En el aula virtual los alumnos realizan tareas.”
#   Tiene 2 palabras que cumplen con la condición: “virtual” y “realizan”.
#
#   4 - Determinar el porcentaje que representan las palabras del punto 3 en base al total de palabras que se encuentran en el texto.
#   Por ejemplo, en el texto: “En el aula virtual los alumnos realizan tareas.”
#   La cantidad de palabras son 8, 2 palabras cumplen con el punto 3, el porcentaje seria 2/8 = 25%.

def es_consonante(caracter):
    return caracter in "bcdfghjklmnñpqrstvwxyz"


def es_vocal(caracter):
    return caracter in "aeiouáéíóú"


def calculo_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


texto = input("Ingrese el texto (debe finalizar con punto): ")
texto = texto.lower()

cont_letras = 0
cont_palabras = 0
mitad = 0
posicion_vocal = 0

palabra_empieza_cons = False
contiene_vocal = False
mayor_igual_5_letras = False

primer_palabra = False
tercer_letra = " "
caran = " "

cpal_punto_1 = -1
cpal_punto_2 = 0
cpal_punto_3 = 0
cpal_punto_4 = 0

for caracter in texto:
    if caracter != " " and caracter != ".":  # Estoy en una letra
        cont_letras += 1

        # Punto 1:
        if cont_letras == 3 and primer_palabra is False:
            tercer_letra = caracter
            primer_palabra = True

        # Punto 2:

        if es_vocal(caracter):
            contiene_vocal = True
            posicion_vocal = cont_letras


        # Punto 3:
        if cont_letras == 1 and es_consonante(caracter):
            palabra_empieza_cons = True



    else:  # Terminé una palabra

        if cont_letras > 0:
            cont_palabras += 1

        # Punto 1:

        if caracter == " " and caran == tercer_letra:
            cpal_punto_1 = cpal_punto_1 + 1


        # Punto 2:
        if cont_letras >= 5:
            mayor_igual_5_letras = True
            mitad = cont_letras // 2

        if mayor_igual_5_letras and contiene_vocal:
            if posicion_vocal >= mitad:
                cpal_punto_2 = cpal_punto_2 + 1

        # Punto 3:

        if cont_letras % 2 != 0 and palabra_empieza_cons:
            cpal_punto_3 = cpal_punto_3 + 1


        # Reiniciar todas las variables a cero
        cont_letras = 0
        palabra_empieza_cons = False
        mayor_igual_5_letras = False

    caran = caracter

# Punto 4
porcentaje = calculo_porcentaje(cpal_punto_3, cont_palabras)

print("\n===============================================")
print("             TABLA DE RESULTADOS               ")
print("===============================================")

print("\n>> Hay ", cpal_punto_1, " palabras que terminan con la tercer letra de la primer palabra del texto", sep="")
print("\n>> Hay ", cpal_punto_2, " palabras mayores o iguales a 5 letras que tienen vocal en la segunda mitad", sep="")
print("\n>> Hay ", cpal_punto_3, " palabras de longitud impar que comienzan con una consonante", sep="")
print("\n>> Hay ", cpal_punto_3, " palabras de longitud impar que comienzan con una consonante y representan un ", round(porcentaje, 2), "% de las palabras del texto", sep="")
