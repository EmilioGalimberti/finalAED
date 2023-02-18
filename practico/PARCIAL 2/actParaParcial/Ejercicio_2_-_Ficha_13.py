# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
#
# 1 - Determinar la cantidad de palabras que presentan digitos en la palabra.
# Por ejemplo, en el texto: “El 1K09 y el 1K15 son cursos espejos a partir del año 2020.”
# Tiene 3 palabras que cumplen con la condición: “1K09”, “1K15” y “2020”.
#
# 2 - Determinar el promedio de letras de la palabras del texto que presentan la
# combinacion “pe” a partir de la tercer letra de la palabra.
# Por ejemplo, en el texto: “El acampe del año apenas tuvo un ágape.”
# Tiene 2 palabras que cumplen con la condición “acampe” y “ágape” que
# suman 11 letras, por lo que el promedio seria 11/2 = 5.5 letras.
#
# 3 - Determinar la cantidad de palabras que finalizan con la letra “n” y que empiecen con una vocal.
# Por ejemplo, en el texto: “Los jovenes acamparon y asaron unos choripanes.” Tiene 2 palabras que cumplen con la condición “acamparon” y “asaron”.
#
# 4 - Determinar la cantidad de palabras que finalizan con la primera letra de esa palabra.
# Por ejemplo, en el texto: “Las simples vidas son solitarias.”
# Tiene 2 palabras que cumplen con la condición “simples” y “solitarias”.

def es_vocal(caracter):
    return caracter in "aeiouáéíóú"


def es_consonante(caracter):
    return caracter in "bcdfghjklmnñpqrstvwxyz"


def es_digito(caracter):
    return caracter in "0123456789"


def calculo_promedio(cantidad, total):
    if total > 0:
        promedio = cantidad / total
    else:
        promedio = 0
    return promedio


texto = input("Ingrese el texto (debe finalizar con punto): ")
texto = texto.lower()

cont_letras = 0
cont_palabras = 0
car_anterior = " "

cant_tiene_pe = 0
primer_letra = 0

hay_digito = False
contiene_pe = False
empieza_vocal = False
finaliza_n = False
suma_pe = 0

cpal_punto_1 = 0
cpal_punto_2 = 0
cpal_punto_3 = 0
cpal_punto_4 = 0

for caracter in texto:

    if caracter != " " and caracter != ".":
        cont_letras += 1

        # Punto 1:

        if es_digito(caracter):
            hay_digito = True


        # Punto 2:

        if cont_letras > 3 and caracter == "e" and car_anterior == "p":
            cant_tiene_pe = cant_tiene_pe + 1
            contiene_pe = True


        # Punto 3:
        if cont_letras == 1 and es_vocal(caracter):
            empieza_vocal = True


        # Punto 4:

        if cont_letras == 1:
            primer_letra = caracter


    else:
        if cont_letras > 0:
            cont_palabras += 1

        # Punto 1:

        if hay_digito:
            cpal_punto_1 = cpal_punto_1 + 1


        # Punto 2:

        if contiene_pe:
            suma_pe = cont_letras + suma_pe


        # Punto 3:

        if (caracter == " " or caracter == ".") and car_anterior == "n":
            finaliza_n = True

        if empieza_vocal and finaliza_n:
            cpal_punto_3 = cpal_punto_3 + 1


        # Punto 4:
        if (caracter == " " or caracter == ".") and car_anterior == primer_letra:
            cpal_punto_4 = cpal_punto_4 + 1

        # Reiniciamos a cero y false
        hay_digito = False
        contiene_pe = False
        empieza_vocal = False
        finaliza_n = False
        cont_letras = 0

    car_anterior = caracter

promedio = calculo_promedio(suma_pe, cant_tiene_pe)

print("\n===============================================")
print("             TABLA DE RESULTADOS               ")
print("===============================================")

print("\n>> Hay ", cpal_punto_1, " palabras que presentan dígitos en ellas", sep="")
print("\n>> El promedio de letras de las palabras que “pe” luego de la tercer letra es del ", round(promedio, 2), "%", sep="")
print("\n>> Hay ", cpal_punto_3, " palabras que finalizan con 'n' y comienzan con vocal", sep="")
print("\n>> Hay ", cpal_punto_4, " palabras que comienzan y terminan con la misma letra", sep="")
