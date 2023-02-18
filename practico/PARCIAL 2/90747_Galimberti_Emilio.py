# Se pide desarrollar un programa en Python que permita cargar por teclado un texto
# completo en una variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y
# se supone que el usuario cargará el punto para indicar el final del texto, y que cada
# palabra de ese texto está separada de las demás por un espacio en blanco.
# El programa debe incluir al menos una función simple con parámetros y retorno de resultado,
# debe procesar el texto caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

#Determinar la cantidad de palabras que tienen dos o más vocales (en minúscula o mayúscula) y contienen también al menos una "s" (minúscula o mayúscula)
# o una "n" (minúscula o mayúscula). Por ejemplo, en el texto "Los equipos que ganen juegan a la tarde." hay 3 palabras que cumplen con la condición
# ("equipos", "ganen" y "juegan").


#Determinar el promedio de caracteres que contienen las palabras del texto que tienen más de 2 consonantes (en minúscula o mayúscula). Por ejemplo, en el texto:
# "La cuenta no cerraba." hay 2 palabras en que tienen más de 2 consonantes ("cuenta" y "cerraba"), y tienen 6 y 7 caracteres respectivamente,
# por lo cual el promedio sería 6.5 caracteres por palabra. Por "caracteres", se entiende "cualquier tipo de símbolo, sea este un dígito, una letra,
# o cualquier otro que pueda aparecer".

#Determinar cuántas palabras contienen entre sus tres primeras posiciones 2 vocales (en minúscula o en mayúscula). Por ejemplo, en el texto:
# "Nos cuesta cien pesos el servicio." solo hay dos palabras que cumplen con la condición: "cuesta" y “cien”.


#Determinar la cantidad de palabras que contienen la expresión "an" (con cualquiera de sus letras en minúscula o en mayúscula)
# pero de forma que la palabra NO TERMINE con esa expresión. Por ejemplo en el texto: "Se paran las máquinas antes que aparezca el fantasma."
# hay dos palabras ("antes" y "fantasma") que cumplen con la condición. Notar que "paran" contiene "an" pero termina con esa expresión,
# y por lo tanto no debe ser contada.

#----------------------------------------------------------------------------------------------------------------------------------------------------

#Determinar la cantidad de palabras que tienen dos o más vocales (en minúscula o mayúscula) y contienen también al menos una "s" (minúscula o mayúscula)
# o una "n" (minúscula o mayúscula). Por ejemplo, en el texto "Los equipos que ganen juegan a la tarde." hay 3 palabras que cumplen con la condición
# ("equipos", "ganen" y "juegan").
def es_vocal(caracter):
    return caracter in "aeiouáéíóúAEIOUÁÉÍÓÚ"

def es_consonante(caracter):
    return caracter in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"

def problema_1(texto):
        cont_letras = 0
        cont_palabras = 0
        cont_vocales = 0
        tiene_s = False
        for caracter in texto:
            if caracter != " " and caracter != ".":
                cont_letras += 1
                if es_vocal(caracter):
                    cont_vocales += 1
                if caracter == "s" or caracter == "S" or caracter == "n" or caracter == "N":
                    tiene_s = True
            else:
                if cont_vocales >= 2 and tiene_s:
                    cont_palabras += 1
                cont_letras = 0
                cont_vocales = 0
                tiene_s = False
        return cont_palabras

#Determinar el promedio de caracteres que contienen las palabras del texto que tienen más de 2 consonantes (en minúscula o mayúscula). Por ejemplo, en el texto:
# "La cuenta no cerraba." hay 2 palabras en que tienen más de 2 consonantes ("cuenta" y "cerraba"), y tienen 6 y 7 caracteres respectivamente,
# por lo cual el promedio sería 6.5 caracteres por palabra. Por "caracteres", se entiende "cualquier tipo de símbolo, sea este un dígito, una letra,
# o cualquier otro que pueda aparecer".
def problema_2(texto):
    cont_letras = 0
    cont_palabras = 0
    cont_consonantes = 0
    cont_palabara_consonante = 0
    suma_caracteres = 0
    promedio = 0
    for caracter in texto:
        if caracter != " " and caracter != ".":
            cont_letras += 1
            if es_consonante(caracter):
                cont_consonantes = cont_consonantes + 1
        else:
            if cont_letras > 0:
                cont_palabras += 1
            if cont_consonantes > 2:
                cont_palabara_consonante += 1
                suma_caracteres = cont_letras + suma_caracteres

            cont_letras = 0
            cont_consonantes = 0
    if cont_palabara_consonante != 0:
        promedio = suma_caracteres /  cont_palabara_consonante
    return cont_palabara_consonante ,promedio

#Determinar cuántas palabras contienen entre sus tres primeras posiciones 2 vocales (en minúscula o en mayúscula). Por ejemplo, en el texto:
# "Nos cuesta cien pesos el servicio." solo hay dos palabras que cumplen con la condición: "cuesta" y “cien”.

def problema_3(texto):
        cont_letras = 0
        cont_vocales = 0
        palabras_pto_3 = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
                if cont_letras <= 3 and es_vocal(caracter):
                    cont_vocales = cont_vocales+1
            else:
                if cont_vocales == 2:
                    palabras_pto_3 += 1
                cont_letras = 0
                cont_vocales = 0
        return palabras_pto_3

#Determinar la cantidad de palabras que contienen la expresión "an" (con cualquiera de sus letras en minúscula o en mayúscula)
# pero de forma que la palabra NO TERMINE con esa expresión. Por ejemplo en el texto: "Se paran las máquinas antes que aparezca el fantasma."
# hay dos palabras ("antes" y "fantasma") que cumplen con la condición. Notar que "paran" contiene "an" pero termina con esa expresión,
# y por lo tanto no debe ser contada.
def es_a(caracter):
    return caracter in "aA"
def es_n(caracter):
    return caracter in "nN"
def problema_4(texto):
        cont_letras = 0
        hay_an = False
        palabras_pto_4 = 0
        caracter_anterior = " "
        caracter_anterior_2 = " "
        for caracter in texto:
            if caracter != " " and caracter != ".":
                cont_letras += 1
                if es_a(caracter_anterior) and es_n(caracter):
                    hay_an = True
            else:
                if hay_an:
                    palabras_pto_4 += 1
                if caracter_anterior_2 == "a" and caracter_anterior == "n" :
                    palabras_pto_4 = palabras_pto_4 - 1
                cont_letras = 0
                hay_an = False
            caracter_anterior_2 = caracter_anterior
            caracter_anterior = caracter

        return palabras_pto_4

def main():
    texto = input("Ingrese el texto (debe finalizar con punto): ")
    a = problema_1(texto)
    cont_palabara_consonante , promedio = problema_2(texto)
    palabras_pto_3 = problema_3(texto)
    palabras_pto_4 = problema_4(texto)

    print("\nRESULTADOS               ")
    print("===============================================")
    print("\n* Hay ",a, "palabras que cumplen con las condiciones pedidas en el punto 1 ")
    print("\n* Hay ",cont_palabara_consonante, "palabras que cumplen con las condiciones y el promedio es ", round(promedio,2))
    print("\n* Hay ",palabras_pto_3, "palabras que cumplen con las condiciones pedidas en el PUNTO 3")
    print("\n* Hay ",palabras_pto_4, "palabras que cumplen con las condiciones pedidas en el PUNTO 4")
    input(" ")
    return

if __name__ == '__main__':
    main()
