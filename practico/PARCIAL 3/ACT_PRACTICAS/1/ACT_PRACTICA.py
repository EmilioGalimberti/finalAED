'''Desarrollar un programa que perimta cargar por teclado un vecto de n elementos y luego:
1)informar cuantas veces se repite en el vector el ultimo numero ingresado
2)Genere un nuevo vector, conteniendo solo los elementos menors al primer valor ingresado'''

def mayor_que(valor, mensaje):
     n = valor - 1
     while n <= valor:
        n = int(input(mensaje))
        if n <= valor:
            print('Error: VALOR INCORRECTO')
     return n


def load_vector(n):
    v = [0] * n
    for i in range(n):  #el range ya devuelve n-1 por lo tanto tiene el cuenta el 0, es lo mismo range(0,n-1)
            v[i] = int(input('ingrese elemento ['+str(i+1)+'] :'))
    return v

# 1)
def accountant_latest_repeated(v):
    latest = v[-1]  # ultimo = v[len(v-1]
    c_repeated = 0
    for i in v:
        if i == latest:
            c_repeated += 1
    return c_repeated - 1

#2)
def less_than_first(v):
    aux_vector = []
    first = v[0]  # ultimo = v[-1]
    for i in v:
        if i < first:
            aux_vector.append(i) #append agrego elementos a la lista
    return aux_vector


def main():
    n = mayor_que(0, 'Ingrese cantidad de elementos del arreglo (> a [0] por favor): ')
    vector = load_vector(n)
    accountant_repeated = accountant_latest_repeated(vector)
    new_vector = less_than_first(vector)
    #salidas
    print('Total de elementos iguales a '+str(vector[-1])+' ultimo: ',accountant_repeated)
    print('Lista de elementos menores a '+str(vector[0])+' primero: ', new_vector)
    pass

if __name__== "__main__":
    main()
