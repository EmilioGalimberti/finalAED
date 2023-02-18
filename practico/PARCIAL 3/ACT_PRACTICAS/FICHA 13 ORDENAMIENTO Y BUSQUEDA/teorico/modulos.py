_author_ = 'Emilio'

#Arreglos en funcion de manejo de listas

def carga(v1):  #v1 parametro formal que necesita
    for i in range(len(v1)):
        v1[i] = int(input('Ingrese un número:'))            #no necesita un return porque solo se modifico en la misma lista del principal




#ordenamiento seleccion directa, de menor a mayor
def selection_sort(v):
    n = len(v) # n = 4
    # 1er ciclo se utiliza para considerar el elemento pivot en la pasada.
    for i in range(n-1):# Rango: 0 1 2
        # 2do ciclo se utiliza para comparar con los demás elementos del arreglo.
        for j in range(i+1, n): # Rango: 1 2 3 \ es i+1 porque no toma en cuneta el pivot
            if v[i] > v[j]: # v[i]=pivot v[j]:elem. actual con el cual estoy comparando.
               v[i] , v[j] = v[j] , v[i] # Intercambio.-


# Busqueda Secuencial -> Algoritmo se usa cuando el vector no esta ordenado.
def linear_search(v, x):
    for i in range(len(v)):
        if x == v[i]:# Consulto si el valor de "x" es igual al componente almacenado en la posición i.
            return i # Retorna el indice en donde se encontró el elemento x.-
    return -1 # El -1 es un indicador de que el elemento no lo encontré.

# Busqueda Binaria. | solo se puede usar con el vector ordenado de menor a mayor
def binary_search(v1, x):
    izq, der = 0, len(v1)-1
    # Con un ciclo while colocamos la condición de corte.-
    while izq <= der:
        #Indice central
        c = (izq + der)//2
        if v1[c] == x:
            return c # c: indice del elemento central q coincide con el elem. buscado.
        if x < v1[c]:
            der = c - 1
        else:
            izq = c + 1
    # Elemento buscado no se encuentra en el arreglo.
    return -1
