def menu():
    print('1- mostrar matriz completa')
    print('2- Sumar toda la matriz')
    print('3- Sumar cada fila de la matriz')
    print('4- Sumar cada columna')
    print('5- Sumar el contorno')
    print('6- Sumar la mitad de arriba')
    print('7- Sumar parte inferior')
    print('8- Exit')
    return int(input('Ingrese una opcion'))

def validar_mayor_que(inf,mensaje):
    n = inf
    while n <= inf:
        n = int(input(mensaje))
    return n

# 2
def sumar_matriz(m):
    suma = 0
    filas = len(m)
    columnas = len(m[0])

    for i in range(filas):
        for j in range(columnas):
            suma += m[i][j]
    return suma

#3
def sumar_filas(mat):
    n = len(mat)
    v = [0] * n
    for i in range(n):
        m = len(mat[i])  #largo de una columa
        for j in range(m): #recorrer por filas
            v[i] += m[i][j]
            # es vv[i] por que sumo por filas si fuera por columnas es sub J # y va cambiando el subindcie solo para sumar las filas
            #v[i] es otro vector que va ir guardando la suma de cada uno de las filas y es sub i para ir parandose en diferentes filas
    return v

#4
def sumar_columnas(mat):
    n = len(mat)
    m = len(mat[0])  #largo de una columa
    v = [0] * m
    for i in range(n):
        for j in range(m): #recorrer por filas
            v[j] += m[i][j]
    return v

# 5
def suma_contorno(mat):
    n = len(mat)
    m = len(mat[0])
    acum = 0
    for i in range(n):
        acum += mat[i][0] + mat[i][m-1]
    for j in range(1, m - 2):
        acum += mat[0][j] + mat[n-1][j]

    return acum

#6
def suma_mitad_sup(mat):
    sum = 0
    filas = len(mat)
    columnas = len(mat[0])

    for i in range(filas//2):
        for j in range(columnas):
            sum += mat[i][j]
    return sum

#7
def suma_mitad_inf(mat):
    sum = 0
    filas = len(mat)
    columnas = len(mat[0])

    for i in range(filas//2,filas):
        for j in range(columnas):
            sum += mat[i][j]
    return sum
