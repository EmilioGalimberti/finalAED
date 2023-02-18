# menu de opciones

# 1) ingresar el nombre de tres atletas, ademas ingrese tambien los tiempoes que lograron, informe el nombre del ganador, ademas indicar
# con un menjase si el tiempo del ganador es menor a 850 segs, batio el record de la act

#2) ingresar un texto el mismo termna con punto, recorrer caracter a caracter y determinar cuantas letras p hay en el textos, cuantas letras j, ademas indique
# cual es el porcentaje que cada conteo representa sobre el total de caracteres del texto

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
        print('\nSe selecciono la opcion 1 ')
        comp1 = input("Ingrese el nombre del competidor 1")
        tiempo_1 = int(input("Ingrese el tiempo de " + comp1 + " en segundos"))

        comp2 = input("Ingrese el nombre del competidor 2")
        tiempo_2 = int(input("Ingrese el tiempo de " + comp2 + " en segundos"))

        comp3 = input("Ingrese el nombre del competidor 3")
        tiempo_3 = int(input("Ingrese el tiempo de " + comp3 + " en segundos"))

        if tiempo_1 < tiempo_2 and tiempo_1 < tiempo_3:
            ganador = comp1
            t_ganador = tiempo_1

        elif tiempo_2 < tiempo_3:
            ganador = comp2
            t_ganador = tiempo_2
        else:
            ganador = comp3
            t_ganador = tiempo_3

        print("\nEl ganador es", ganador, "en", t_ganador,"segundos")

        if t_ganador < 850:
            print("Ha superado el record de 850s")

#2) ingresar un texto el mismo termna con punto, recorrer caracter a caracter y determinar cuantas letras "p" hay en el textos, cuantas letras "j" , ademas indique
# cual es el porcentaje que cada conteo representa sobre el total de caracteres del texto

    elif opcion ==2:
        print('\nSe selecciono la opcion 2 ')
# se puede pone al final .lower() para poner en minuzcula
        texto = input("ingrese el texto a procesar. Finaliza con .")
        c_letras = 0
        cont_p = 0
        cont_j = 0
#el for recorre caracter a caracter



        for letra in texto:
            # if letra == "." or " ":
            if letra != "." and " ":
                #dentro de la palabra
                c_letras = c_letras + 1
                #para sacar cuantas p aparecieron
                if letra == "p" or letra == "P":
                    cont_p += 1
                if letra == "j" or letra == "J":
                    cont_j += 1
            else:
                #final de la palabra
                if c_letras > 0:
                    pass

        porc_p = cont_p*100/c_letras
        porc_j = cont_j*100/c_letras

        print("\ntotal de p ingresadas: ",cont_p , "representan",round(porc_p, 2),"% total de letras")
        print("total de j ingresadas", cont_j , "representan",round(porc_j, 2),"% total de letras")

    elif opcion == 3:
        print('\nSALIO DEL PROGRAMA')
    else:
        print('\nOpcion incorrecta ingrese nuevamente')

#caracter y letra es = ? preguntar si los espacios en blanco los tomamos como caracteres
