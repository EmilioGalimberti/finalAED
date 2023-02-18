__author__ = 'Catedra AED'

class Articulo:
    def __init__(self, num, desc, venta, compra, pais, tipo, stock):
        self.identificacion = num
        self.descripcion = desc
        self.precio_venta = venta
        self.precio_compra = compra
        self.pais = pais
        self.tipo = tipo
        self.stock = stock

def to_string(info):
    r = ''
    r += '{:<25}'.format('Identidicacion: ' + str(info.identificacion))
    r += '{:<20}'.format('Descripcion: ' + info.descripcion)
    r += '{:<25}'.format('Precio Venta: ' + str(info.precio_venta))
    r += '{:<25}'.format('Precio Compra: ' + str(info.precio_compra))
    r += '{:<15}'.format('Pais: ' + str(info.pais))
    r += '{:<15}'.format('Tipo: ' + str(info.tipo))
    r += '{:<15}'.format('Stock: ' + str(info.stock))
    return r

