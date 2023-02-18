# Recordadr porque el self, y el init
class Proyecto:
    def __init__(self, numeroIdentificacion, nombre, descripcion, monto, areaAplicacion, tipoProyecto):
        self.numeroIdentificacion = numeroIdentificacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.monto = monto
        self.areaAplicacion = areaAplicacion
        self.tipoProyecto = tipoProyecto

def to_string(info):
    r = ''
    r += '{:<30}'.format('Numero de identidicacion: ' + str(info.numeroIdentificacion))
    r += '{:<35}'.format('Nombre: ' + info.nombre)
    r += '{:<40}'.format('Descripcion: ' + info.descripcion)
    r += '{:<25}'.format('Monto: ' + str(info.monto))
    r += '{:<25}'.format('Area de aplicacion: ' + str(info.areaAplicacion))
    r += '{:<15}'.format('Tipo proyecto: ' + str(info.tipoProyecto))
    return r
