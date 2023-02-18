# Se pide desarrollar un programa en Python que permita cargar por teclado un texto
# completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y
# se supone que el usuario cargará el punto para indicar el final del texto, y que cada
# palabra de ese texto está separada de las demás por un espacio en blanco.
# El programa debe incluir al menos una función simple con parámetros y retorno de resultado,
# debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

# Turno 02 – Enunciado 04 [T2E4]
#
# Determinar la cantidad de palabras que tienen al menos dos consonantes (minúsculas o mayúsculas)
# y no contienen dígitos. Por ejemplo, en el texto: "Los vuelos AR1KL03 y AR1VL21 tienen un retraso superior a 2 horas."
# Hay 6 palabras que cumplen con la condición: "Los", "vuelos", "tienen", "retraso", "superior" y  "horas".
#
# Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que tienen igual
# cantidad de vocales (minúsculas o mayúsculas) que dígitos.
# Por ejemplo, en el texto: "Al infinito y más allá de A5."
# Hay 1 palabra ("A5") que tiene igual cantidad de vocales que digitos,
# sobre un total de 7 palabras. Por lo tanto, el porcentaje pedido es 14.28%.
#
# Determinar cuántas palabras contienen 2 vocales mayúsculas en sus primeras dos posiciones,
# o dos vocales minúsculas entre las posiciones cuatro y cinco.
# Por ejemplo, en el texto: "EEHHH a esa no la teniaaaaa." hay dos palabras que cumplen con la condición: "EEHHH" y "teniaaaaaa".
#
# Determinar la cantidad de palabras que contienen la expresión "d2" (d minúscula o mayúscula)
# pero solo una vez, y de forma que esa palabra no contenga ningún otro dígito (ni el 2 ni ningún otro)
# en otra posición.
# Por ejemplo en el texto: "Se ha separad2 del grupo d2d2 y del principal ad2h1.“
# hay 1 palabra que cumple con la condición ( "separad2").
# La palabra "d2d2" no cumple porque "d2" está 2 veces, y la palabra "ad2h1" tampoco
# porque tiene un segundo dígito además del "2" que forma la expresión "d2".


def es_vocal(caracter):
    return caracter in "aeiouáéíóúAEIOUÁÉÍÓÚ"


def es_vocal_mayus(caracter):
    return caracter in "AEIOUÁÉÍÓÚ"


def es_vocal_min(caracter):
    return caracter in "aeiouáéíóú"


def es_consonante(caracter):
    return caracter in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"


def es_digito(caracter):
    return caracter in "0123456789"


def calculo_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


def principal():
    texto = input("Ingrese el texto (debe finalizar con punto): ")

    cont_letras = 0
    cont_palabras = 0
    car_anterior = " "

    cont_consonantes = 0
    hay_digito = False

    tiene_mayus = False
    tiene_minus = False

    cant_vocales = 0
    cant_digitos = 0
    tiene_vocal = False
    tiene_digito = False

    cont_aparece_d2 = 0
    cont_digitos = 0

    cont_palabras_punto_1 = 0
    cont_palabras_punto_2 = 0
    cont_palabras_punto_3 = 0
    cont_palabras_punto_4 = 0

    for caracter in texto:
        if caracter != " " and caracter != ".":
            cont_letras = cont_letras + 1

            # Punto 1:
            if es_consonante(caracter):
                cont_consonantes = cont_consonantes + 1

            if es_digito(caracter):
                hay_digito = True

            # Punto 2:

            if es_vocal(caracter):
                cant_vocales = cant_vocales + 1
                tiene_vocal = True

            if es_digito(caracter):
                cant_digitos = cant_digitos + 1
                tiene_digito = True

            # Punto 3:

            if cont_letras == 2 and es_vocal_mayus(caracter) and es_vocal_mayus(car_anterior):
                tiene_mayus = True

            if cont_letras == 5 and (es_vocal_min(caracter) and es_vocal_min(car_anterior)):
                tiene_minus = True

            # Punto 4:
            if car_anterior == "d" or car_anterior == "D":
                if caracter == "2":
                    cont_aparece_d2 = cont_aparece_d2 + 1
            if es_digito(caracter):
                cont_digitos = cont_digitos + 1



        else:
            if cont_letras > 0:
                cont_palabras = cont_palabras + 1

            # Punto 1:

            if cont_consonantes >= 2 and hay_digito is False:
                cont_palabras_punto_1 = cont_palabras_punto_1 + 1


            # Punto 2:

            if (tiene_vocal and tiene_digito) and cant_vocales == cant_digitos:
                cont_palabras_punto_2 = cont_palabras_punto_2 + 1


            # Punto 3:

            if tiene_mayus or tiene_minus:
                cont_palabras_punto_3 = cont_palabras_punto_3 + 1

            # Punto 4:

            if cont_aparece_d2 == 1 and cont_digitos == 1:
                cont_palabras_punto_4 = cont_palabras_punto_4 + 1

            # Reiniciamos a false y cero
            cont_letras = 0
            cont_consonantes = 0
            hay_digito = False
            cant_vocales = 0
            cant_digitos = 0
            cont_aparece_d2 = 0
            cont_digitos = 0
            tiene_mayus = False
            tiene_minus = False
            tiene_vocal = False
            tiene_digito = False

        car_anterior = caracter

    porcentaje = calculo_porcentaje(cont_palabras_punto_2, cont_palabras)

    print("\n===============================================")
    print("             TABLA DE RESULTADOS               ")
    print("===============================================")

    print("\n>> Hay ", cont_palabras_punto_1, " palabras que tienen al menos 2 consonantes y no tienen dígitos", sep="")
    print("\n>> Hay ", cont_palabras_punto_2, " palabras que tienen igual cantidad de vocales que de dígitos y representan un ", round(porcentaje, 2), "% de las palabras del texto", sep="")
    print("\n>> Hay ", cont_palabras_punto_3, " palabras que tienen vocales mayusculas o minusculas", sep="")
    print("\n>> Hay ", cont_palabras_punto_4, " palabras que cumplen con la condicion", sep="")


if __name__ == '__main__':
    principal()
