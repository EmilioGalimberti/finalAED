__author__ = 'Catreda AED'

# Creación de una matriz.- Alternativa 1

def creacion_matriz(n, m):
    m1 = []
    for f in range(n):
        m1.append([])
        for c in range(m):
            nro = int(input('Ingrese un número:'))
            m1[f].append(nro)
            #m1[f].append(None)
    return m1

def test():
  # n = representa las filas de la matriz.
  # m = representa las columnas de la matriz.
  n, m = 3, 2
  m1 = creacion_matriz(n, m)
  print('Matriz creada m1:', m1)

if __name__ == '__main__':
    test()
