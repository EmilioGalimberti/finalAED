__author__ = 'Catedra AED'

def crear_matriz(n, m):
    mat = [[None] * m for f in range(n)]
    return mat

def carga_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            mat[f][c] = int(input('Ingrese un numéro en la fila '+ str(f) + ' y la columna ' + str(c) + ':'))

def mostrar_por_columnas(mat):
    for c in range(len(mat[0])):
        for f in range(len(mat)):
            print('Elemento de la matriz en la columna ', str(c), ' y fila ', str(f), ' es:',mat[f][c])
def test():
    n, m = 3, 2
    mat = crear_matriz(n, m)
    carga_matriz(mat)
    print('Matriz cargada!')
    mostrar_por_columnas(mat)

if __name__ == '__main__':
    test()
