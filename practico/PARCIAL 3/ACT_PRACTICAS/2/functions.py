import random

'''V es un vector ya dimensionado, y en estos casos no usamos return porque se modifica directamente al vector
deberiamos usar return si buscamos generar un nuevo vector o recibir otro resultado'''

#---------------------------------generacion-------------------
def vector_whole_random(v,desde, hasta): #creacion de vector random con 9 componetes
    n = len(v)
    for i in range(n):
        v[i] = random.randint(desde,hasta)
    pass



#---------------ORDEN---------------- 1)
def selection_sort(v): #seleccion directa de menor a mayor
    n = len(v)
    # 1er ciclo se utiliza para considerar el elemento pivot en la pasada.
    for i in range(n-1):# Rango: 0 1 2
        # 2do ciclo se utiliza para comparar con los demás elementos del arreglo.
        for j in range(i+1, n): # Rango: 1 2 3 \ es i+1 porque no toma en cuneta el pivot
            if v[i] > v[j]: # v[i]=pivot v[j]:elem. actual con el cual estoy comparando.
               v[i] , v[j] = v[j] , v[i] # Intercambio.-
    pass


#2)

# Busqueda Binaria. | solo se puede usar con el vector ordenado de menor a mayor
def binary_search(v, x):
    izq, der = 0, len(v)-1
    # Con un ciclo while colocamos la condición de corte.-
    while izq <= der:
        #Indice central
        c = (izq + der)//2
        if v[c] == x:
            return c # c: indice del elemento central q coincide con el elem. buscado.
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    # Elemento buscado no se encuentra en el arreglo.
    return -1

def may_count(v,min): #usamos busqueda binaria para comenzar a contar apartir de ese numero, ya que anteriormente los ordenamos de menor a mayor
    pos = binary_search(v,min)
    if pos == -1:
        pos = 0
    n = len(v)
    c = 0
    for i in range(pos,n):
        if v[i] > min:
            c += 1
    return c
#3)
def prom(v):
    sum = 0
    n = len(v)
    for i in range(n):
        sum += v[i]
    prom = 0
    if n > 0 :
        prom = sum / n
    return prom

#4)
def less_count(v):
    menor = v[0]
    n = len(v)
    c = 1
    for i in range(1,n):
        if v[i] == menor:
            c += 1
        else:
            break  #utilizamos el break, para cuando detecte uno mayor no siga recorriendo
    return c

#contar menor con while
# def contar_menor_while(v):
#    menor = v[0]
#    n = len(v)
#    c = i = 1
#    while v[i] == menor and i < n:
#        c += 1[
#    return c

#5)
def new_v(v):
    new_vector = [v[0]]
    n = len(v)
    for i in range(1,n):  #en este caso no lo puedo empezar en cero, porque no tendere un casillero anterior
        if v[i] != v[i-1]:
            new_vector.append(v[i])
    return new_vector


