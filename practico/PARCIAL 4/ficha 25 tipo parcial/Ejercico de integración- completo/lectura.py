class Lectura:
    def __init__(self, codigo, estado_motor, estado_frenos, consumo_comb, descrip):
        self.cod = codigo
        self.est_mot = estado_motor
        self.est_fr = estado_frenos
        self.cons = consumo_comb
        self.desc = descrip

def display(lectura):
    print('Codigo:', lectura.cod, '\t')
    print(' - Estado motor:', lectura.est_mot, '\t')
    print(' - Estado freno:', lectura.est_fr, '\t')
    print(' - Consumo combustible', lectura.cons, '\t')
    print(' - Descripcion', lectura.desc)
