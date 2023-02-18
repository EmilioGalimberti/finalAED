
#dif media

#determinar la cantidad de palabras que comienzan con la primera letra de todo el texto

def a(texto):
    primera_palabra = True
    car_anterior = ""
    cont_letras = 0
    cont = 0
    for caracter in texto:
        if caracter != " " and caracter != ".":
            cont_letras += 1
            if primera_palabra:
                car_anterior = caracter
                primera_palabra = False
            if cont_letras == 1 and caracter == car_anterior:
                cont += 1
        else:
            cont_letras = 0

    return cont

#determinar el porcentaje de palabras que comienzan con la primera letra de todo el texto
def b(texto):
    primera_palabra = True
    car_anterior = ""
    cont_letras = 0
    cont_palabras = 0
    cont = 0
    porcentaje = 0
    for caracter in texto:
        if caracter != " " and caracter != ".":
            cont_letras += 1
            if primera_palabra:
                car_anterior = caracter
                primera_palabra = False
            if cont_letras == 1 and caracter == car_anterior:
                cont += 1
        else:
            if cont_letras > 1:
                cont_palabras += 1


            cont_letras = 0
    #calculo porcentaje
    porcentaje = cont *100 /cont_palabras
    return porcentaje

def main():
    texto = input("Ingrese el texto (debe finalizar con punto): ")
    cont  = a(texto)
    print("determinar la cantidad de palabras que comienzan con la primera letra de todo el texto" , cont)
    por = b(texto)
    print("determinar el porcentaje de palabras que comienzan con la primera letra de todo el texto" , round(por,2))
    return

if __name__ == '__main__':
    main()
