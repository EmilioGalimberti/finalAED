import random
import string


class Programa:
    def __init__(self, clave, nombre, descripcion, cantidad, deporte, nivel):
        self.clave = clave
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.deporte = deporte
        self.nivel = nivel



def to_string(programa):
    r = ''
    r += '{:<35}'.format('Clave de identificacion: ' + str(programa.clave))
    r += '{:<75}'.format('nombre:: ' + str(programa.nombre))
    r += '{:<45}'.format('descripción: ' + str(programa.descripcion))
    r += '{:<55}'.format('cantidad: $' + str(programa.cantidad))
    r += '{:<25}'.format('deporte: ' + str(programa.deporte))
    r += '{:<35}'.format('nivel: : ' + str(programa.nivel))
    print()
    print(r)
def encabezado():
    cadena = '{:<91}\n' \
             '| {:^15} | {:^20} | {:^15} | {:^10} | {:^10} | {:^10} |\n' \
             '{:<91}\n'
    return cadena.format('=' * 100, 'Clave', 'Nombre', 'Descipcion', 'Cantidad', 'Deporte', 'Nivel', '=' * 100)


def clave_2():
    clav = ("1qasd345", "1wert23d", "4fghytd4", "7ugjrlt5", "a96nfj57", "0otnyj69", "polen458", "plÃ±etcb7", "qwbc4523",
            "lpntre56")
    return random.choice(clav)


def generar_descripcion():
    descripcion = ''
    for i in range(4):
        if i < 3:
            descripcion += ''.join(random.choices(string.ascii_letters, k=13)) + ' '
        else:
            descripcion += ''.join(random.choices(string.ascii_letters, k=12)) + '.'
    return descripcion

