#Determinar la cantidad de palabras que tienen al menos dos consonantes (minúsculas o mayúsculas) y no contienen dígitos.
# Por ejemplo, en el texto: "Los vuelos AR1KL03 y AR1VL21 tienen un retraso superior a 2 horas." Hay 6 palabras que cumplen con la condición:
# "Los", "vuelos", "tienen", "retraso", "superior" y  "horas".

#Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que tienen igual cantidad de vocales (minúsculas o mayúsculas) que dígitos.
# Por ejemplo, en el texto: "Al infinito y más allá de A5." Hay 1 palabra ("A5") que tiene igual cantidad de vocales que digitos, sobre un total de 7 palabras.
# Por lo tanto, el porcentaje pedido es 14.28%.

#Determinar cuántas palabras contienen 2 vocales mayúsculas en sus primeras dos posiciones, o dos vocales minúsculas entre las posiciones cuatro y cinco.
# Por ejemplo, en el texto: "EEHHH a esa no la teniaaaaa." hay dos palabras que cumplen con la condición: "EEHHH" y "teniaaaaaa".

#Determinar la cantidad de palabras que contienen la expresión "d2" (d minúscula o mayúscula) pero solo una vez, y de forma que esa palabra no
# contenga ningún otro dígito (ni el 2 ni ningún otro) en otra posición. Por ejemplo en el texto: "Se ha separad2 del grupo d2d2 y del principal ad2h1.“
# hay 1 palabra que cumple con la condición ( "separad2"). La palabra "d2d2" no cumple porque "d2" está 2 veces, y la palabra "ad2h1" tampoco porque tiene
# un segundo dígito además del "2" que forma la expresión "d2".

def es_vocal(caracter):
    return caracter in "aeiouAEIOU"

def es_digito(caracter):
    return caracter in "0123456789"



def xd(texto):
                cont_letras = 0
                acumulador = 0
                vocal = False
                digito = False
                for caracter in texto:
                    if caracter != " " and caracter != ".": #contador letra
                        cont_letras += 1
                        if es_vocal(caracter):
                            vocal = True
                        if es_digito(caracter):
                            digito = True
                    else:
                        if vocal is True and digito is True:
                            acumulador += 1

                        cont_letras = 0
                        vocal = 0
                        digito = 0


                return acumulador




def d2(texto):
        cont_letras = 0
        car_anterior = ""
        car_d2 = 0
        digito = 0
        acum_d2 = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
                if car_anterior == "d" or car_anterior == "D":
                    if caracter == "2":
                        car_d2 +=1
                if es_digito(caracter):
                    digito += 1
            else:
                if car_d2 == 1 and digito == 1:
                    acum_d2 += 1
                car_d2 = 0
                digito = 0
            car_anterior = caracter
        return acum_d2


def main():
    texto = input("Ingrese el texto (debe finalizar con punto): ")
    acum_d2 = d2(texto)
    print("hay ",acum_d2," que cumplen con la condicion")
    acumulador  = xd(texto)
    print("hay, ", acumulador, " que cumplen con la condicion del punto 2")
    return


main()
