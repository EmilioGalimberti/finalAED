class pasaje:
    def __init__(self, pasaporte, nombre, codigo_destino, codigo_clase, monto):
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.codigo_destino = codigo_destino
        self.codigo_clase = codigo_clase
        self.monto = monto


def to_string(a):
    return 'Pasaporte:{:>12} Nombre: {:<20} Codigo Destino: {:>20} Codigo Clase: {:>16} Monto abonado $: {:>5}'.format(a.pasaporte, a.nombre, a.codigo_destino, a.codigo_clase, a.monto)
