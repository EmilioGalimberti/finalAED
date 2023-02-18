# Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
#
# 1) - Determinar la cantidad de palabras que contiene la letra “l” en la primera mitad de la palabra y terminan con “s”.
# Por ejemplo, en el texto: “Los elementos allanados seran totalizados en el juzgado.”
# Tiene 2 palabras que cumplen con la condición “elementos” y “allanados”.
#
# 2) - Determinar el porcentaje que representan las palabras de longitud impar con respecto del total de palabras del texto.
# Por ejemplo, en el texto: “La carta se entrega en el correo por la mañana.”
# Tiene 3 palabras de longitud impar, hay 10 palabras del texto, el porcentaje seria 3 / 10 = 33.33 %.
#
# 3) - Determinar la cantidad de palabras que contiene la secuencia “pl” a partir de la tercer letra.
# Por ejemplo, en el texto : “El empleado tenia que emplear un pegamento para unir el plegado.”
# Tiene 2 palabras que cumplen con la condición “empleado” y “emplear”.
#
# 4) - Determinar la cantidad de palabras que tiene una mayor cantidad de digitos que letras,
# pero dicha palabra debe contener al menos una letra.
# Por ejemplo, en el texto: “Los cursos 1K09 y 1K15 son espejos desde el 2020.”
# Tiene 2 palabras que cumplen con la condición “1K09” y “1K15”..

def es_letra(caracter):
    return caracter in "abcdefghijklmnñopqrstuvwxyz"


def calculo_porcentaje(cantidad, total):
    porcentaje = 0
    if total > 0:
        porcentaje = cantidad * 100 / total
    return porcentaje


def es_digito(caracter):
    return caracter in "0123456789"


# Punto 1:
posicion_l = 0
termina_s = False

# Punto 2:
conta_palabras_impares = 0

# Punto 3:
cant_tiene_pl = 0
contiene_pl = False

# Punto 4:
cont_digitos = 0
contiene_letra = False
contiene_digito = False

car_anterior = " "

cont_letras = 0
cont_palabras = 0

cpal_punto_1 = 0
cpal_punto_2 = 0
cpal_punto_3 = 0
cpal_punto_4 = 0

texto = input("Ingrese el texto (debe finalizar con punto): ")
texto = texto.lower()


for caracter in texto:    # Estoy en una letra

    if caracter != " " and caracter != ".":
        if es_letra(caracter):
            cont_letras = cont_letras + 1
            contiene_letra = True

        # Punto 1:

        if caracter == "l":
            posicion_l = cont_letras


        # Punto 3:

        if cont_letras > 3 and caracter == "l" and car_anterior == "p":
            cant_tiene_pl = cant_tiene_pl + 1
            contiene_pl = True


        # Punto 4:
        if es_digito(caracter):
            cont_digitos = cont_digitos + 1
            contiene_digito = True


    else:    # Terminé una palabra

        if cont_letras > 0:
            cont_palabras += 1

        # Punto 1:
        mitad = cont_letras // 2

        if (caracter == " " or caracter == ".") and car_anterior == "s":
            termina_s = True

        if posicion_l < mitad and termina_s:
            cpal_punto_1 = cpal_punto_1 + 1


        # Punto 2:
        if cont_letras % 2 != 0:
            conta_palabras_impares = conta_palabras_impares + 1


        # Punto 4:
        if contiene_digito and contiene_letra:
            if cont_digitos > cont_letras:
                cpal_punto_4 = cpal_punto_4 + 1

        # Reiniciamos a cero y false
        termina_s = False
        contiene_pl = False
        contiene_letra = False
        contiene_digito = False
        cont_letras = 0
        cont_digitos = 0

    car_anterior = caracter

porcentaje = calculo_porcentaje(conta_palabras_impares, cont_palabras)

print("\n===============================================")
print("             TABLA DE RESULTADOS               ")
print("===============================================")

print("\n>> Hay ", cpal_punto_1, " palabras que que contiene la letra “l” en la primera mitad de la palabra y terminan con 's'", sep="")
print("\n>> Hay ", conta_palabras_impares, " palabras con de longitud impar y representan un ", round(porcentaje, 2), "% de las palabras del texto", sep="")
print("\n>> Hay ", cant_tiene_pl, " palabras que contienen la silaba 'pl' a partir de la tercer letra", sep="")
print("\n>> Hay ", cpal_punto_4, " palabras que tienen mas dígitos que letras y contienen al menos una letra", sep="")
