__author__ = 'Catedra AED'

''' Enunciado: Un comercio mayorista trabaja con cierta cantidad "n" de artículos, numerados
del 0 al n-1. Dispone de un plantel de "m" vendedores para su venta, los cuales están
enumerados del 0 al m-1 inclusive, en forma contigua. El gerente de dicho comercio desea
obtener cierta información estadística respecto de las ventas realizadas en el mes. El
programa que se pide, deberá cargar una matriz cant, de orden m*n, en la que cada fila
represente un vendedor, cada columna un artículo, y cada componente cant[i][j] almacene la
cantidad del artículo j vendida por el vendedor i.
Se pide emitir un listado con las cantidades totales realizadas por cada vendedor y las
cantidades totales que se vendieron de cada artículo.'''

# filas =representa un vendedor.
# columnas = representa un articulo.
# cant [fila] [columa] = cant. articulos vendidos del articulo j vendida por el vendedor i

def validate(inf):
    t = inf
    while t <= inf:
        t = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
        if t <= inf:
            print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
    return t

def read(m, n):
    # crear y cargar por teclado una matriz... filas en orden creciente...
    cant = [[0] * n for f in range(m)]
    for f in range(m):
        for c in range(n):
            cant[f][c] = int(input('Valor [' + str(f) + '][' + str(c) + ']: '))
    return cant

def totales_por_vendedor(cant):
    # totalización por filas...
    m, n = len(cant), len(cant[0])
    print()
    print('Cantidades vendidas por cada vendedor')
    for f in range(m):
        ac = 0
        for c in range(n):
            ac += cant[f][c]
        print('Vendedor', f, '\t- Cantidad total vendida:', ac)

def totales_por_articulo(cant): # total por columna...
    # totalización por columnas...
    m, n = len(cant), len(cant[0])
    print()
    print('Cantidades totales vendidas de cada artículo')
    for c in range(n):
        ac = 0
        for f in range(m):
            ac += cant[f][c]
        print('Artículo', c, '\t- Cantidad total vendida:', ac)


def test():
    print('Cantidad de vendedores...')
    m = validate(0)
    print('Cantidad de artículos...')
    n = validate(0)
    print('Cargue las cantidades de artículos por vendedor...')
    cant = read(m, n)
    totales_por_vendedor(cant)
    totales_por_articulo(cant)

if __name__ == '__main__':
    test()

