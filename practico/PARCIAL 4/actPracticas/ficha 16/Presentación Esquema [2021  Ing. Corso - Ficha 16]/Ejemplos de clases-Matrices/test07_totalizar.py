__author__ = 'Catedra AED'

def crear_matriz(n, m):
    mat = [[None] * m for f in range(n)]
    return mat

def carga_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            mat[f][c] = int(input('Ingrese un numéro en la fila '+ str(f) + ' y la columna ' + str(c) + ':'))

def sumatoria_por_columnas(mat):
    acu = 0
    for c in range(len(mat[0])):
        for f in range(len(mat)):
            acu+= mat[f][c]
    return acu

def test():
    n, m = 3, 3
    mat = crear_matriz(n, m)
    carga_matriz(mat)
    print('Matriz cargada!')
    print('Sumatoria de los elementos:', sumatoria_por_columnas(mat))


if __name__ == '__main__':
    test()
