class Reserva:
    def __init__(self, codigo, nombre,edad, tipo,invitados,monto):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.invitados = invitados
        self.monto = monto


def convertir_a_reserva(linea):
    dato = linea[:-1] #linea sin enter   #toma una linea de texto y elimino el \n
    #largo = len(dato)
    #campos = []
    #inicio = 0
    campos = dato.split(',')   #a dato hace split, que por separador tiene la coma, y devuelve un vector campos  , corta los pedazos de cadena entre las y devolvemelo en un registro
    #for i in range(largo):

        #if dato[i] == ",":  esto hace split
        #    campo = dato[inicio, i-1]
        #    campos.append(campo)        #devuelve el vector
        #    inicio = i+1

    return Reserva(campos[0], campos[1],int(campos[2]),int(campos[3]),int(campos[4]),float(campos[5])) #hace el registro

def to_string(reserva): #permite mostrar el registro
    tipos_servicio = ('salón ',' salón y animación ',' salón, animación y comida niños ', 'salón, animación, comida niños y sorpresitas') #para mostrar los tipos en ves de un numerp
    plantilla = '{}|{}|{}|{}|{}|{}'
    return plantilla.format(reserva.codigo,reserva.nombre,reserva.edad,reserva.tipo,reserva.invitados,reserva.monto)

def convertir_a_texto(reserva):
    plantilla = '{},{},{},{},{},{}\n'
    return plantilla.format(reserva.codigo,reserva.nombre,reserva.edad,reserva.tipo,reserva.invitados,reserva.monto)
