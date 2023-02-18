#1. Complejo de cines
#Desarrollar un programa que permita procesar funciones de un complejo de cines.
#Por cada función se conoce: cantidad de espectadores y descuento (S/N).
#La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

#El programa deberá:

#a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de
#$50 en los días con descuento y $75 en los días sin descuento.
#
#b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre
#el total de funciones.

#A)

total = 0
cont_funciones = 0
cont_con_dto = 0

espectadores = int(input("Ingrese la cantidad de espectadores: "))

while espectadores != 0:
    con_descuento = input("Es con descuento? (S/N)" )

    if con_descuento == "S":
        # ES LO MISMO HACER total = total + (espectadores*50)
        total += espectadores * 50
        cont_con_dto += 1
    else:
        total += espectadores * 75

    cont_funciones = cont_funciones + 1


#B)
    espectadores = int(input("ingrese la cantidad de espectadores"))

print(total)

if cont_funciones>0:
    porcentaje = cont_con_dto * 100 / cont_funciones
else:
    porcentaje = 0

print("funciones con descuento: ", cont_con_dto)
print("porcentaje de funciones con descuento ", porcentaje)
