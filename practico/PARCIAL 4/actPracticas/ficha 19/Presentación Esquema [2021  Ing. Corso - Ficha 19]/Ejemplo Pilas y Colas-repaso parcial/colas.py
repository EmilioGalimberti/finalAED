__author__ = 'Catedra AED'

def init():
    cola = []
    return cola

def esta_vacia(cola):
    n = len(cola)
    return n == 0

def add(cola, x):
    cola.append(x)

def remove(cola):
    x = None
    if not esta_vacia(cola):
        x = cola[0]
        del cola[0]
    return x

def test():
    c1 = init()

    add(c1, 5)
    add(c1, 7)
    add(c1, 2)
    add(c1, 4)
    print('Estado actual de la cola:', c1)

    print('Listado de elementos que se irán retirando de la cola..')
    while not esta_vacia(c1):
        print('El elemento eliminado de la cola:',remove(c1))

if __name__=="__main__":
    test()