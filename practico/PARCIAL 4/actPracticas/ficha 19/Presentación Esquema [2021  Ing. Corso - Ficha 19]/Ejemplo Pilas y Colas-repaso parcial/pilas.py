__author__ = 'Catedra AED'

def init():
    pila = []
    return pila

def esta_vacia(pila):
    n = len(pila)
    return n == 0

def add(pila, x):
    pila.append(x)


def remove(pila):
    x = None
    if not esta_vacia(pila):
        #Recupero el elemento que voy a borrar de la pila.-
        x = pila[-1]
        #Borrar el elemento de la pila
        del pila[-1]
    return x

def test():
    p1 = init()

    add(p1, 5)
    add(p1, 7)
    add(p1, 2)
    add(p1, 4)

    print('Estado actual de la pila:', p1)


    print('Listado de elementos que se irán retirando de la pila..')
    while not esta_vacia(p1):
        print('El elemento eliminado de la pila:',remove(p1))


if __name__== "__main__":
    test()