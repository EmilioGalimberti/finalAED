__author__ = 'Catedra AED'

# Proceso de carga de la matriz.-

def carga_matriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            mat[f][c] = int(input('Ingrese un numéro en la fila '+ str(f) + ' y la columna ' + str(c) + ':'))

def test():
    n, m = 3, 2
    mat = [[None] * m for f in range(n)]
    carga_matriz(mat)
    print('Matriz cargada!')

if __name__ == '__main__':
    test()


