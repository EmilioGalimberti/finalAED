''' Funciones reutilizables en el manejo de cadenas de caracteres...'''

# determina si un caracter es una vocal...
def es_vocal(car):
    if car in 'aeiouAEIOU':
        return True
    return False


# determina si un caracter es un dígito...
def es_digito(car):
    if car in '0123456789':
        return True
    return False


# determina si un caracter es una consonante...
def es_consonante(car):
    if car in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        return True
    return False


# determina si un caracter es un blanco o un punto...
def es_terminador(car):
    if car in ' .':
        return True
    return False
