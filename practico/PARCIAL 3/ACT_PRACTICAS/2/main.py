#
# Desarrollar un programa que permita procesar el puntaje obtenido por un participante en una prueba olimpica de gimnasia.
# Para ellos generar un vector de 9 elementos, represeantando cada miembro del jurado. Por cada celda, generar un valor
# aleatorio entre 0 y 10 (inclusive) que indicará la puntuación recibida.
# A continuacion informar:
# 1) Los tres mejores puntajes recibidos
# 2) Indicar cuantos jueces calificaron con mas de 6
# 3) Indicar el puntaje promedio que obtuvo la gimnasta
# 4) Indique cuantas veces se repitio la menor nota
# 5) Genere un nuevo vector, tal que no admita notas repetidas
#

from functions import *



print('Ingrese el puntaje de los 9 jueces')
#---------------------------------generacion-------------------
points = [0]* 9
vector_whole_random(points,0,10)

print('puntajes del deportista')
print(points)
#---------------ORDEN---------------- 1)

selection_sort(points)
print('Los mejores puntajes obtenidos son: ',end='')
print(points[-1],points[-2],points[-3])

# 2)
may = may_count(points, 6)
print(may, 'jueces puntuaron mas de 6')

#3)
prom = prom(points)
print('Puntaje promedio: ',prom)

#4)
print('La menor nota es ', points[0])
print('Se repite ', less_count(points))

#5)
print('puntaje sin repeticiones')
sin_repeticiones = new_v(points)
print(sin_repeticiones)
n = len(sin_repeticiones)
for i in range(n):
    print(sin_repeticiones[i])

