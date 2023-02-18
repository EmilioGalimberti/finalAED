__author__ = 'Catedra de AED'

import pickle


def test():
    print('Procediendo a grabar números en el archivo')
    m = open('prueba.dat', 'wb')

    x, y = 2.345, 19
    # Grabación en el archivo...
    pickle.dump(x, m)
    pickle.dump(y, m)

    m.close()

    m = open('prueba.dat', 'rb')
    # Lectura del archivo..
    a = pickle.load(m)
    b = pickle.load(m)
    m.close()

    print('Datos recuperados desde el archivo:', a, ' - ', b)
    print('Hecho...')

if __name__ == '__main__':
    test()
