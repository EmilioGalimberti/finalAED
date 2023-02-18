_author_='Emilio'
#partiendo de una lista vacia
#vector vacio
notas = []
#for i in range(1,21): Esto dice que recorre del 1 al 20 lo mismo seria poner for ir in range(20):
#Agrego 5 notas al vector
for i in range(5):
    x = int(input('ingrese una nota: '))
    notas.append(x)  #.append permite agregar x al vector
print('Termino la carfa de la lista!')
print(notas)

#partiendo de un vector con componetes definidas
n = int(input('ingrese la cantidad de notas que desea cargar'))
notas1 = n * [0] #vector de 4 componetes

#tambien se puede hacer n = len(notas1) y reemplazar n en el for

for i in range(len(notas1)): #len permite conocer el tama;o o cant de elementos de una variable list, lo mismo seria hacer for i in range(n) en este caso
    #cargar notas por teclado
    notas1[i] = int(input('cargue nota:'))
for i in range(len(notas1)):
    print('la nota1 en la posicion: ', str(i), 'es: ', notas1[i])
#recorre la lista de forma inversa, uso de indices negativos
for i in range(-1,(-len(notas1)-1),-1): # el primer -1 es de donde parto, el ultimo -1 es el incremento que es negativo, y si no coloco el -1 dsp del lens no hara
    print('recorremos al reves la lista notas1', notas1[i])

print(notas)
#elimino un elemento de la lista notas  \\ tambien de puede eliminar toda la lista con la funcion del
del notas[0]
print('eliminando el elemento que se encunetra en el indice 0 de la lista notas', notas)

# copia = numeros solo estoy asignado a copia la misma lista
# copia = numeros[:] estoy creando una nueva lista en copia, por lo tanto tendria dos listas
