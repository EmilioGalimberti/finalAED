__author__ = 'Catedra AED'

# Creación de una matriz.- Alternativa 2

def creacion_matriz(n, m):
   m2 = [None] * n
   for f in range(n):
     # Crea la columnas para cada fila
     m2[f] = [None] * m
   return m2


def test():
  n, m = 3, 2
  m2 = creacion_matriz(n, m)
  print('Matriz creada m2:', m2)

if __name__ == '__main__':
    test()
