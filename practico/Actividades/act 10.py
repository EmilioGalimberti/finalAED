#. Sílaba "de" en la primera mitad
#Desarrollar un programa en Python que permita cargar por teclado un texto completo.
#Siempre se supone que el usuario cargará un punto para indicar el final del texto,
#y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

#a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito
#(un caracter entre '0' y '9').

#b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6
#letras.

#c) Determinar la longitud de la palabra más larga del texto.

#d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra.

def es_digito(caracter):
    return caracter in "0123456789"


def palabras_con_digito(texto):
        cont_letras = 0
        cont_palabras = 0
        digito = False
        acum_palabra_digito = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
                if es_digito(caracter):
                    digito =True
            else:
                if cont_letras > 0:
                    cont_palabras += 1
                if digito is True:
                    acum_palabra_digito += 1
                digito = False
                cont_letras = 0

        return acum_palabra_digito

def B(texto):
        cont_letras = 0
        cont_palabras_3 = 0
        cont_palabras_4 = 0
        cont_palabras_6 = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
            else:
                if cont_letras <= 3:         #contador palabra con menos de 3 letras
                    cont_palabras_3 += 1
                elif cont_letras >= 4 and cont_letras <=6 :
                    cont_palabras_4 += 1
                else:
                    cont_palabras_6 += 1
                cont_letras = 0
        return cont_palabras_3, cont_palabras_4, cont_palabras_6

def palabra_mas_larga(texto):
        cont_letras = 0
        acum_cont_letras = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
                acum_cont_letras = cont_letras
            else:
                if acum_cont_letras > acum_cont_letras:  #contador palabra con mas letras (longitud)
                    acum_cont_letras = acum_cont_letras
                cont_letras = 0
        return acum_cont_letras


def expresion_de_primera_mitad(texto):
        cont_letras = 0
        car_anterior = " "
        hay_de = False
        posicion_de = 0
        antes_de_mitad_de = 0
        for caracter in texto:
            if caracter != " " and caracter != ".": #contador letra
                cont_letras += 1
                if car_anterior == "d" and caracter == "e":
                    hay_de = True
                    posicion_de = cont_letras
            else:
                if hay_de and posicion_de <= (cont_letras//2):
                    antes_de_mitad_de +=1

                cont_letras = 0
                hay_de = False
            car_anterior = caracter
        return antes_de_mitad_de


def main():
    texto = input("Ingrese el texto (debe finalizar con punto): ")
    acum_palabra_digito = palabras_con_digito(texto)
    print("Cantidad de palabras con almenos un digito ", acum_palabra_digito)
    a , b , c = B(texto)
    print("Palbra con 3 letras o menos = ",a," Palabras entre 4 y 6 letras = ", b, " Palabras con mas de 6 letras = ",c)
    acum_cont_letras = palabra_mas_larga(texto)
    print("La palabra mas larga contine ",acum_cont_letras, " letras")
    antes_de_mitad_de = expresion_de_primera_mitad(texto)
    print("cantidad de palabras que contienen de en la primera mitad: " , antes_de_mitad_de)
    return

#scrip principal
main()
