__author__ = 'Catedra AED'

'''El responsable del consorcio de un pequeño barrio cerrado desea obtener una estadística
de los gastos incurridos en el barrio a lo largo de un trimestre por las n propiedades
que hay en el barrio. Para ello, se solicita crear tipo de registro designado como Consumo,
con los campos que describan el consumo realizado en un mes dado por una propiedad: en uno
de los campos almacenar el importe pagado por electricidad en ese mes, en otro el importe
gastado en gas, y en otro el importe gastado en servicio medido de agua.

Se debe crear una matriz cons de referencias a registros de tipo Consumo, en la que cada
columna represente uno de los tres meses del trimestre analizado (numerados de 0 a 2) y
en la que cada fila represente una de las n propiedades (numeradas de 0 a n-1).

El registro de tipo Consumo almacenado en la casilla cons[i][j], representará entonces
los gastos realizados por la propiedad i en el mes j. Se pide un que permita:
a.) Cargar los datos de la matriz.
b.) Mostrar adecuadamente los datos de toda la matriz.
c.) Mostrar por pantalla un listado general en el cual se indique el gasto acumulado por
cada propiedad en el trimestre (es decir, una totalización por filas de la matriz).
d.) Mostrar por pantalla el gasto acumulado para un determinado mes del trimestre
(es decir, una totalización de "una" de la matriz).
'''

import consumos

def validate(inf):
    n = inf
    while n <= inf:
        n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
        if n <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return n

def read(fils, cols):
    cons = [[None] * cols for f in range(fils)]
    print('Ingrese los montos consumidos por cada rubro...')
    for f in range(fils):
        print('Propiedad', f, ':')
        for c in range(cols):
            print('\tMes', c)
            el = float(input('\t\tGasto en electricidad: '))
            gs = float(input('\t\tGasto en gas: '))
            ag = float(input('\t\tGasto en agua: '))
            cons[f][c] = consumos.Consumo(el, gs, ag)
            print()
    return cons

def display(cons):
    filas, columnas = len(cons), len(cons[0])
    print('Planilla de gastos mensuales por propiedad...')
    for f in range(filas):
        print('Propiedad', f)
        for c in range(columnas):
            consumos.write(cons[f][c])
    print()

def total_per_property(cons):
    filas, columnas = len(cons), len(cons[0])
    print('Gastos por propiedad en cada trimestre')
    for f in range(filas):
        ac = 0
        for c in range(columnas):
            t = cons[f][c].electricidad + cons[f][c].gas + cons[f][c].agua
            ac += t
        print('Propiedad:', f, '\tGasto total:', ac)

def total_per_one_month(cons, mes):
    ac = 0
    filas = len(cons)
    print('Gastos por propiedad para un determinado mes')
    for f in range(filas):
        t = cons[f][mes].electricidad + cons[f][mes].gas + cons[f][mes].agua
        ac += t
    return ac

def test():
    # cargar cantidad de propiedades...
    print('Cantidad de propiedades -', end=' ')
    fils = validate(0)
    print()
    # crear y cargar la matriz de consumos...
    cols = 3
    cons = read(fils, cols)
    print()
    # mostrar todos los datos cargados...
    display(cons)
    print()
    # acumulación por filas...
    total_per_property(cons)
    print()
    # acumulación para una columna especifica...
    mes = int(input('Ingrese el mes (0,1 o 2):'))
    print(total_per_one_month(cons, mes))

# script principal...
if __name__ == '__main__':
    test()
