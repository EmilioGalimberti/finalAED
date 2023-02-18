import random


# Por cada deportista se tienen los siguientes datos: número identificador (un entero), nombre
#del deportista (una cadena de caracteres), un número para indicar el deporte que practica (un entero entre 0 y 49),
#para indicar (por ejemplo): 0: atletismo, 1: natación, etc.), un código indicador del tipo beca que tiene ese deportista
#(un número entre 0 y 9 para indicar (por ejemplo): 0: completa, 1: media beca, 2: solo cobertura de gastos, etc.), y el
#monto que se paga a ese deportista por su beca o colbertura (un número flotante).

NOMBRES = ["EDUARDO","JOSE","MATIAS","DANIEL","JERE","RAFA"]
DEPORTES = ["FUTBOL","TENIS","BASQUET","VOLEY","ATELTISMO","NATACION"]
BECA = ["COMPLETA","MEDIA BECA","SOLO COBERTURA","70 %"]


class Deportista():
    def __init__(self,ident,nom,dep,cod,monto):
                self.ident = ident
                self.nom = nom
                self.dep = dep
                self.cod = cod
                self.monto = monto


def to_string(reg):
    return "  |Numero de identifacicion : " + str(reg.ident) + \
            "  |Nombre : " + reg.nom + \
            "  |Deporte practicado : " + str(reg.dep) + \
            "  |Codigo beca : " + str(reg.cod) + \
            "  |Monto total : " + str(reg.monto)


def crear_aleatorio():
    ident = random.randint (0,100)
    nom = random.choice(NOMBRES)
    dep = random.randint(0,49)
    cod = random.randint(0,9)
    monto = round(random.uniform(0,1000),2)
    return Deportista(ident,nom,dep,cod,monto)

def principal():

    reg = crear_aleatorio()
    print(to_string(reg))


if __name__ == '__main__':
    principal()











