# menu de opciones

# 1) ingresar el nombre de tres atletas, ademas ingrese tambien los tiempoes que lograron, informe el nombre del ganador, ademas indicar
# con un menjase si el tiempo del ganador es menor a 850 segs, batio el record de la act

#2) ingresar un texto el mismo termna con punto, recorrer caracter a caracter y determinar cuantas letras p hay en el textos, cuantas letras j, ademas indique
# cual es el porcentaje que cada conteo representa sobre el total de caracteres del texto


#extra contar cant de palabras que tiene mas de 2 "J" y almenos 1 "p"

# 3) Terminar el programa

#menu de opciones
opcion=None

while opcion != 3:
    print('=' * 15)
    print('MENU DE OPCIONES')
    print('=' * 15)
    print('Seleccione alguna de las opciones')
    print('>> 1.')
    print('>> 2.')
    print('>> 3. Salir')
    opcion = int(input('\n>>Ingrese la opcion: '))
    print('=' * 15)

 # 1) ingresar el nombre de tres atletas, ademas ingrese tambien los tiempoes que lograron, informe el nombre del ganador, ademas indicar
# con un menjase si el tiempo del ganador es menor a 850 segs, batio el record de la act

    if opcion == 1:
        print("")
    elif opcion ==2:
        print('\nSe selecciono la opcion 2 ')
# se puede pone al final .lower() para poner en minuzcula
        texto = input("ingrese el texto a procesar. Finaliza con .")
        c_letras = 0
        c_letras_total = 0
        c_palabras_bonus = 0
        cont_p = 0
        cont_j = 0
        cont_p_totales = 0
        cont_j_totales = 0
#el for recorre caracter a caracter

        for letra in texto:
            # if letra == "." or " ":
            if letra != "." and " ":
                #dentro de la palabra
                c_letras += 1
                #para sacar cuantas p aparecieron
                if letra == "p" or letra == "P":
                    cont_p += 1
                if letra == "j" or letra == "J":
                    cont_j += 1
            else:
                #final de la palabra
                #extra contar cant de palabras que tiene mas de 2 "J" y almenos 1 "p"
                if c_letras > 0: #tengo una palabra con almenos una letra
                    if cont_j > 2 and cont_p:
                        c_palabras_bonus += 1
                    c_letras_total += c_letras
                    cont_p_totales += cont_p
                    cont_j_totales += cont_j
                c_letras = 0
                cont_p = 0
                cont_j = 0

        porc_p = cont_p_totales*100/c_letras_total
        porc_j = cont_j_totales*100/c_letras_total

        print("\ntotal de p ingresadas: ",cont_p , "representan",round(porc_p, 2),"% total de letras")
        print("total de j ingresadas", cont_j , "representan",round(porc_j, 2),"% total de letras")

    elif opcion == 3:
        print('\nSALIO DEL PROGRAMA')
    else:
        print('\nOpcion incorrecta ingrese nuevamente')

#caracter y letra es = ? preguntar si los espacios en blanco los tomamos como caracteres
