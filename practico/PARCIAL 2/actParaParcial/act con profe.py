"""
* 2 - Determinar la cantidad de palabras que comienzan con 'le' y terminan en 'to'.
* 7 - Determinar cuantas palabras incluyeron '10' antes de la mitad.
* 9 - Determinar la cantidad de palabras que comienzan con la última letra de la primera palabra del texto y tienen más de 2 vocales
* 14 - Determinar la cantidad de palabras con vocales y consonantes alternadas.
"""

def es_palabra(i):
    return i != ' ' and i != '.'


def main():
    texto = input('Ingrese un texto:\n').lower()

    c_letras = 0
    primera_palabra = True
    anterior = ''
    anterior_2 = ''
    empieza_le = False
    le_to = 0
    hay_10 = False
    posicion_10 = 0
    antes_mitad_10 = 0
    ult_letra_primera_palabra = ''
    pal_ult_let_pri_pal = 0

    for i in texto:
        if es_palabra(i):
            c_letras += 1

            if c_letras == 2 and i == 'e' and anterior == 'l':
                empieza_le = True

            if i == '0' and anterior == '1' and not hay_10:
                hay_10 = True
                posicion_10 = c_letras

            if c_letras == 1 and i == ult_letra_primera_palabra:
                pal_ult_let_pri_pal += 1

        else:

            if anterior_2 == 't' and anterior == 'o' and empieza_le:
                le_to += 1

            if hay_10 and posicion_10 <= (c_letras // 2):
                antes_mitad_10 += 1

            if primera_palabra:
                ult_letra_primera_palabra = anterior
                primera_palabra = False

            c_letras = 0
            empieza_le = False
            hay_10 = False

        anterior_2 = anterior
        anterior = i

    print(le_to)
    print(antes_mitad_10)
    print(pal_ult_let_pri_pal)


if __name__ == '__main__':
    main()
