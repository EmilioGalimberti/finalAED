__author__ = 'Catedra AED'

# Creación de una matriz.- Alternativa 3
def crear_matriz(n, m):
    m3 = [[None] * m for f in range(n)]
    return m3

def test():
    n, m = 3, 2
    m3 = crear_matriz(n, m)
    print('Matriz creada m3:', m3)

if __name__ == '__main__':
    test()
