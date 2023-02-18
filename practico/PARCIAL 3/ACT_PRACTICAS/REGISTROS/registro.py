
#1)----------- Carga---------------------------
class Proyecto:
    def __init__(self,numero,nombre,honorarios,tipo):
        self.numero = numero
        self.cliente = nombre
        self.honorarios = honorarios
        self.tipo = tipo

def mayor_que(min, mensaje):
    val = min
    while val <= min:
        val = int(input(mensaje))
        if val <= min:
            print('Error, valor incorrecto!')
    return val

def validacion_rango(mi,ma,mensaje):
    nro = mi -1
    while nro < mi or nro >ma:
        nro = int(input(f"{mensaje}: "))
        if nro < mi or nro > ma:
            print('Error, Valor incorrecto ')
    return nro

def carga_proyectos(n):
    v = []
    for i in range(n):
        numero = mayor_que(0, 'Ingrese <Numero> de proyectos: ')
        cliente = input('Ingrese <Nombre de cliente>: ')
        honorarios = mayor_que(0, 'INgrese <Honorarios>: ')
        tipo = validacion_rango(0,14,'Ingrese un tipo de proyecto [0-14]')
        r = Proyecto(numero,cliente,honorarios,tipo)
        v.append(r)
    return v

# 2) muestra-------------------------------------

def write(proyecto):  #esto devuelve una cadena o to_stirng el linea.format lo tabulea para que se vea mejor
    linea = '{:<0}\t{:<30}\t{:>10.2f}\t{:>5}' #esto devuelve la cadena formateada
    return linea.format(proyecto.numero, proyecto.cliente, proyecto.honorarios, proyecto.tipo)


def listar_proyectos(v):
    for proyecto in v:
        print(write(proyecto))   # proyecto variable aux que guarda cada uno de los proyectos y lo va mostrando



#3) acumular honorarios POR TIPOS y mostrar de menor a mayor, por eso es importante el acumulador con 15 componentes ya que los tipos van de 0 a 14
def acumular_honorarios(v):
    acumulador = [0] * 15
    for proyecto in  v:
        acumulador[proyecto.tipo] += proyecto.honorarios  #tiene en cuenta de que tipo y acumula son honorarios
    return acumulador

def menu():
    print()
    print('1. Cargar el arreglo de proyecto. ')
    print('2. Mostrar datos de proyecto. ')
    print('3. Montos de honorarios por tipos. ')
    print('4. Proyectos no tipo 4. ')
    print('5. Buscar proyecto de cliente. ')
    print('6. Salir. ')

    op = int(input('Ingrese una opcion: '))
    return op


