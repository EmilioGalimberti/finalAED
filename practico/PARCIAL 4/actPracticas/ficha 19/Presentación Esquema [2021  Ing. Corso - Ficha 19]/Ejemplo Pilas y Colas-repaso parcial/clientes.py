__author__ = 'Catedra AED'

class Cliente():
    def __init__(self, nom, acomp, trof, precio):
        self.nombre = nom
        self.acomp = acomp
        self.tipo_trofeo = trof
        self.precio_tot = precio

def write(reg):
    print('Nombre: ', reg.nombre)
    print('Cant. de acompañantes: ' , reg.acomp)
    print('Tipo de trofeo: ' , reg.tipo_trofeo)
    print('Precio total:  $' , reg.precio_tot)
