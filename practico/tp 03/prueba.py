def busqueda_del_mayor(v):
    print("Funcion de busqueda del libro de mayor precio según su idioma.")
    print("\nRerencia de Idiomas:\n0. Español.\n1. Inglés.\n2. Francés.\n3. Italiano.\n4. Otros.")

    i_lenguaje = int(input("\n>> Ingrese el numero del lenguaje que desea buscar: "))

    for i in range(len(v)):
        if v[i].idioma== i_lenguaje:
            lenguaje = str(idioma[i_lenguaje])
            i_may = may_precio(v, lenguaje)

            print("\n> Libro mas costoso en el idioma", v[i_may].idioma, ":")
            print(to_string(v[i_may]))
