# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres.
# El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto
# está separada de las demás por un espacio en blanco. El programa debe:
#
#
# 1- Determinar la cantidad de palabras que incluyen al menos una vocal.
# Por ejemplo, en el texto: “Los cursos 1k4 y 1k8.”
# Respuesta: 2 palabras. La palabras que cumplen con la condición son: “Los” y “cursos”.
#
# 2- Determinar cuántas palabras incluyen la expresión ‘sa’ en la primera mitad de la palabra.
# Por ejemplo, en el texto: “una saludable siesta y luego comer salsa bolognesa.”
# Respuesta: 2 palabras. Las palabras que cumplen con la condición son: “saludable” y “salsa”.
#
# 3- Determinar el porcentaje de palabras en todo el texto que tienen una cantidad par de caracteres.
#  Por ejemplo, en el texto: “La zapatilla de temporada.”
#  Respuesta: 50,00 %. Palabras que cumplen la condición: 2, total de palabras: 4. Porcentaje = 2 * 100 / 4 = 50.00%.
#
# 4- Determinar cuántas palabras incluyen el último caracter de la primera palabra ingresada en el texto.
# Por ejemplo, en el texto: “esperamos les guste la materia.”
# Respuesta: 2 palabras. Las palabras que cumplen la condición son: “les” y “guste”.
# El último caracter de la primera palabra es ‘s’, y las dos palabra citadas tienen alguna 's' en alguna parte.

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

car_anterior = " "

incluye_vocal = False
incluye_sa = False
posicion_a = 0
cont_palabras_par = 0
ultimo_caracter = " "

cpal_punto_1 = 0
cpal_punto_2 = 0
cpal_punto_3 = 0
cpal_punto_4 = 0

for caracter in texto:
    if caracter != " " and caracter != ".":
        cont_letras += 1

        # Punto 1:
        if es_vocal(caracter):
            incluye_vocal = True

        # Punto 2:
        if car_anterior == "s" and caracter == "a":
            incluye_sa = True
            posicion_a = cont_letras

        # Punto 4:
        if caracter == ultimo_caracter:
            cpal_punto_4 = cpal_punto_4 + 1


    else:
        if cont_letras > 0:
            cont_palabras += 1

        # Punto 1:
        if incluye_vocal:
            cpal_punto_1 = cpal_punto_1 + 1

        # Punto 2:
        mitad = cont_letras // 2

        if posicion_a < mitad and incluye_sa:
            cpal_punto_2 = cpal_punto_2 + 1

        # Punto 3:
        if cont_letras % 2 == 0:
            cont_palabras_par = cont_palabras_par + 1

        # Punto 4:
        if cont_palabras == 1:
            ultimo_caracter = car_anterior


        # Reiniciamos a false y cero
        cont_letras = 0
        incluye_vocal = False

    car_anterior = caracter

porcentaje = calculo_porcentaje(cont_palabras_par, cont_palabras)

print("\n===============================================")
print("             TABLA DE RESULTADOS               ")
print("===============================================")

print("\n>> Hay ", cpal_punto_1, " palabras que contienen al menos una vocal", sep="")
print("\n>> Hay ", cpal_punto_2, " palabras que contienen 'sa' en la primera mitad de la palabra", sep="")
print("\n>> Hay ", cont_palabras_par, " palabras que tienen una cantidad par de caracteres y representan un ", round(porcentaje, 2), "% de las palabras del texto" , sep="")
print("\n>> Hay ", cpal_punto_4, " palabras que contienen el ultimo caracter de la primer palabra", sep="")



