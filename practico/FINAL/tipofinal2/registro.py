class Paciente:
    def __init__(self, historiaClinica, nombre, descripcionDiagnostico, monto, tipoPlanCobertura, tipofarmaco):
        self.historiaClinica = historiaClinica
        self.nombre = nombre
        self.descripcionDiagnostico = descripcionDiagnostico
        self.monto = monto
        self.tipoPlanCobertura = tipoPlanCobertura
        self.tipofarmaco = tipofarmaco

def to_string(info):
    r = ''
    r += '{:<30}'.format('Numero de Historia clinica: ' + str(info.historiaClinica))
    r += '{:<35}'.format('Nombre: ' + info.nombre)
    r += '{:<40}'.format('Descripcion: ' + info.descripcionDiagnostico)
    r += '{:<25}'.format('Monto: ' + str(info.monto))
    r += '{:<25}'.format('Tipo de plan de cobertura: ' + str(info.tipoPlanCobertura))
    r += '{:<15}'.format('Tipo de farmaco recetado: ' + str(info.tipofarmaco))
    return r
