
import random

#?????????????????????????? MENU DE OPCIONES ????????????????????????????????

def generacion_y_carga():

    print("Tipo de carga:\n> 1.Manual\n> 2.Automática")
    carga = int(input(">> Seleccione el tipo de carga: "))

    # CARGA MANUAL
    if carga == 1:

        caran = " "
        conta_guion = 0
        cont = 10
        n = 0 #Acumulador
        #cant libros
        cantidad_libros = int(input('ingrese la cantidad de libros: '))
        a = 0
        arreglo_libro = []

        while a != cantidad_libros:

            #ISBN

            isbn = input("Ingrese el ISBN deseado: ")
            # ----- De Cadena a Vector Int -----
            isbn_entero = []
            for i in isbn:
                if i != "-":
                    isbn_entero.append(int(i))
            # ----------------------------------
             #   -------------------------------- FOR - BANDERAS ------------------------------------  #
            flag_guion_junto = False
            sintaxis_bien = False
            # VERIFICAMOS GUIONES
            for car in isbn:
                if car == "-":
                    conta_guion = conta_guion + 1
                if car == "-" and caran == "-":
                    flag_guion_junto = True
                caran = car
            if conta_guion == 3 and flag_guion_junto is False:
                sintaxis_bien = True
            # VERIFICAMOS SI ES DIVISIBLE
            for car in isbn_entero:
                if car >= 0 and car <= 9:
                    n = n + cont * car
                    cont = cont - 1
            if n % 11 == 0 and sintaxis_bien:
                print("\n>> ISBN VALIDO")
            else:
                print("\n>> ISBN NO VALIDO")

            conta_guion = 0
            flag_guion_junto = False
            sintaxis_bien = False

            arreglo_libro.append(isbn)
            #titulo
            titulo = input('ingrese titulo del libro: ')
            arreglo_libro.append(titulo)
            #genero
            print('\n 0.Autoayuda \n 1.Arte \n 2. Ficción \n 3.Computación \n 4.Economía \n 5.Escolar \n 6.Sociedad \n 7.Gastronomía \n 8.Infantil \n 9.Otros')
            num_genero_libro = int(input('ingrese el genero del libro:'))
            genero = ("Autoayuda", "Arte", "Ficción", "Computación", "Economía", "Escolar", "Sociedad", "Gastronomía", "Infantil", "Otros")

            arreglo_libro.append(genero[num_genero_libro])
            #Idioma
            print (' \n 0.Español \n 1.Inglés \n 2.Francés \n 3.Italiano \n 4.Otros')
            num_idioma_libro = int(input('ingrese el idioma del libro: '))
            idioma = ("Español", "Inglés", "Francés", "Italiano", "Otros")
            arreglo_libro.append(idioma[num_idioma_libro])

            #Precio
            precio = int(input('ingrese el precio del libro:'))
            arreglo_libro.append(precio)

            a += 1
    # CARGA AUTOMATICA
    if carga == 2:
        pass

    return  arreglo_libro

def mostrar(arreglo_libro): # ACA ESTA LO ULTIMO QUE HICIMOS
    print(arreglo_libro)




def conteo_y_genero_popular():
    pass

def busqueda_del_mayor():
    pass

def busqueda_por_ISBN():
    pass

def consulta_por_genero():
    pass

def consulta_precio_por_grupo():
    pass

# ???????????????????????????????????????????????????????????????????????????

def cadena_a_vector(isbn):
    isbn_entero = []
    for i in isbn:
        if i != "-":
            isbn_entero.append(int(i))
    return isbn_entero

def comprobar_ISBN():
    caran = " "
    conta_guion = 0
    cont = 10
    n = 0   # Acumulador

    #cant libros
    cantidad_libros = int(input('ingrese la cantidad de libros: '))
    a = 0
    arreglo_libro = []

    while a != cantidad_libros:
        isbn = input("Ingrese el ISBN deseado: ")
        isbn_entero = cadena_a_vector(isbn)

        # ?????????? FOR - BANDERAS ????????????
        sintaxis_bien = False

        # VERIFICAMOS GUIONES
        for car in isbn:
            if car == "-":
                conta_guion = conta_guion + 1

            if car == "-" and caran != "-":
                if conta_guion == 3:
                    sintaxis_bien = True

            caran = car


        # VERIFICAMOS SI ES DIVISIBLE
        for car in isbn_entero:
            if car >= 0 and car <= 9:
                n = n + cont * car
                cont = cont - 1

        if n % 11 == 0 and sintaxis_bien:
            print("\n>> ISBN VALIDO")
        else:
            print("\n>> ISBN NO VALIDO")

        conta_guion = 0
        sintaxis_bien = False

        # ??????????????????????????????????????
        arreglo_libro.append(isbn)

def principal():
    opc = None
    while opc != 8:
        print("?"*60)
        print("                TRABAJO PRACTICO N°3")
        print("?"*60)

        print(">> REFERENCIA DE OPCIONES:")
        print("1.) Generación y Carga.")
        print("2.) Mostrar.")
        print("3.) Conteo y género más popular.")
        print("4.) Búsqueda del mayor.")
        print("5.) Búsqueda por ISBN.")
        print("6.) Consulta de un género.")
        print("7.) Consulta de precio por grupo.")
        print("?"*60)
        opc = int(input("Ingrese el numero de la opción a ejecutar: "))
        print("?"*60)

        if opc == 1:
            arreglo_libro = generacion_y_carga()

        if opc == 2:
            mostrar(arreglo_libro)

        if opc == 3:
            pass
        if opc == 4:
            pass
        if opc == 5:
            pass
        if opc == 6:
            pass
        if opc == 7:
            pass
        input("Precione Enter para Continuar")


if __name__ == '__main__':
    principal()



