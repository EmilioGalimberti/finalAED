from registro import  *
#1
import random


def validarMayor(mensaje):
    n = -1
    while n <= -1:
        n = int(input(mensaje))
        if n <= -1:
            print('Error, ingrese un numero de registros valido')
        return n

def addInOrder(reg, linea):
    izq, der = 0, len(reg) - 1
    pos = len(reg)
    while izq <= der:
        c = (izq + der) // 2
        # Lo unico que cambia es segun en que se ordena
        if reg[c].historiaClinica == linea.historiaClinica:
            pos = c
            break
        if reg[c].historiaClinica > linea.historiaClinica:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    reg[pos:pos] = [linea]



def cargaRegistro(n, v):
    nombres = 'Joaquin', 'Pablo', 'Emilio'
    descripcionesDiagnosticos = "Neumonía bilateral causada por COVID 19.", 'Neumonía bilateral causada por OMICRON.'
    for i in range(n):
        # ver ene este caso como se le podria agregar caracterese a la histrocia clinica
        historiaClinica = random.randint(1,5)
        nombre = random.choice(nombres)
        descripcioneDiagnostico = random.choice(descripcionesDiagnosticos)
        monto = random.randint(1, 100)
        tipoPlanCobertura = random.randint(1, 15)
        tipFarmaco = random.randint(1, 10)
        x = Paciente(historiaClinica, nombre, descripcioneDiagnostico, monto, tipoPlanCobertura, tipFarmaco)
        addInOrder(v, x)
    return  v

#2
def displayRegistro(v):
    for i in v:
        print(to_string(i))
