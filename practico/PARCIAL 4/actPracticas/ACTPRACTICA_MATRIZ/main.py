# matriz de num enteros
import random
from funciones import *

def main():
    n = validar_mayor_que(0,'Ingrese la cant de filas: ')
    m = validar_mayor_que(0,'Ingrese la cant de columnas: ')
    # creacion matriz, una matriz es una lista de listas para python
    # Una forma mat = [[random.randint(0,9)]* m for i in range(n)] # por cada fila estoy creando un vector de m elementos
    mat = [[0] * m for i in range(n)]
    for i in  range(n): #recorrido por filas
        for j in range(m):
            mat[i][j] = random.randint(0,9)

    op = -1
    while op != 8:
        op = menu()

        if  op == 1:
            print(mat)
        elif op == 2:
            print(sumar_matriz(mat))
        elif op == 3:
            vec = sumar_filas(mat)
            for i in range(len(vec)):
                print("FIla ", i ,':', vec[i])
        elif op == 4:
            v = sumar_matriz(mat)
            for i in range(len(v)):
                print("FIla ", i ,':', v[i])
        elif op == 5:
            pass
        elif op == 6:
            s = suma_mitad_sup(mat)
            print('La suma de la mitad superior es de ', s)
        elif op == 7:
            inf = suma_mitad_inf(mat)
            print('La suma de la mitad superior es de ', inf)
    pass

if __name__ == '__main__':
    main()
