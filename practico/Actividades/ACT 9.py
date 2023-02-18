#1. Sílaba "mo"
#Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones:
#una es cargar todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador;
# y la otra es cargar cada caracter uno por uno a través de un while). Siempre se supone que el usuario cargará
#un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio
#en blanco. El programa debe:

#a) Determinar cuántas palabras tenían más de 4 letras.

#b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

#c) Determinar el promedio de letras por palabra en todo el texto.

#d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".
#if caracter == "x" and caracter == "y":
#********************************************************************************
#Ejemplo: 'el mono momoxy toca el xilofon.'
#********************************************************************************
#Palabras con más de 4 letras: 2
#Palabras tenían al menos una vez la letra "x" o la letra "y": 2
#El promedio de letras por palabra en todo el texto es: 4.17
#Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1

def palabra_exprsion_mo(texto):
                cont_letras = 0
                car_anterior = 0
                caracter_mo = 0
                acumulador_mo = 0
                for caracter in texto:
                    if caracter != " " and caracter != ".": #contador letra
                        cont_letras += 1
                        if car_anterior == "m" and caracter == "o":
                            caracter_mo += 1
                    else:
                        if caracter_mo == 1:
                            acumulador_mo +=1       #contador de palabra con solo una vez mo
                        cont_letras = 0
                        caracter_mo = 0
                    car_anterior = caracter
                return acumulador_mo
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

def palabra_con_x_o_y(texto):
        cont_letras = 0
        cont_palabras = 0
        cont_palabras_x_y = False
        acum_x_o_y = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
                if caracter == "x" or caracter == "y":
                    cont_palabras_x_y = True
            else:
                if cont_letras > 0:         #contador palabra que tiene x o y
                    cont_palabras += 1
                if cont_palabras_x_y is True:
                    acum_x_o_y +=1
                cont_letras= 0
                cont_palabras_x_y = False
        return acum_x_o_y


def main():
    texto = input("Ingrese el texto (debe finalizar con punto): ")
    cont_palabras = palabra_mayor_4_letras(texto)
    print("palabras con mas de 4 letras =", cont_palabras)
    a = palabra_con_x_o_y(texto)
    print("palabras con mas de (x) o (y) = ", a)
    acumulador_mo = palabra_exprsion_mo(texto)
    print("palabra con solo una vez mo =", acumulador_mo)

#scrip principal
main()
