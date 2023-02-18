from funciones import *

def menu():
    print("1- Cargar")
    print("2- Mostrar")
    print("3- Contar")
    print("4- Buscar")
    print("5- Filtrar")
    print("6- Salir")


def principal():

    alquileres = None
    opcion = 0

    while opcion != 6:
        menu()
        opcion = int(input("Ingrese la opción:"))

        if opcion == 1:
            n = int(input("Ingrese la cantidad de alquieres"))
            alquileres = cargar_alquileres(n)
        elif opcion == 2:
            if alquileres:
                ordenar(alquileres)
                mostrar_alquileres("Todos los alquileres ingresados", alquileres)
            else:
                print("Debe cargar los alquileres!")
        elif opcion == 3:
            if alquileres:
                contadores = contar_por_tipo(alquileres)
                mostrar_vector(contadores)
            else:
                print("Debe cargar los alquileres!")

        elif opcion == 4:
            if alquileres:
                c = input("Ingrese la descripcion a buscar")
                x = int(input("Ingrese los días"))
                encontrado = buscar(alquileres, c, x)
                if encontrado:
                    print(to_string(encontrado))
                else:
                    print("No se encuentra")
            else:
                print("Debe cargar los alquileres!")
        elif opcion == 5:
            if alquileres:
                x = int(input("Ingrese el tipo a buscar"))
                z = float(input("Ingrese el importe mínimo"))
                encontrados = filtrar_tipo_importe(alquileres, x, z)
                mostrar_alquileres("Listado de alquieres que cumplen con la condición", encontrados)
                promedio = promedio_importes(encontrados)
                print("Promedio de importes:", promedio)
            else:
                print("Debe cargar los alquileres!")



if __name__ == "__main__":
    principal()


