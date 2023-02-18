'''Cargar por teclado un conjunto de valores tales que todos ellos estén
comprendidos entre 0 y 99 (incluidos ambos). Se indica el fin de datos
con el número -1. Determinar cuantas veces apareció cada número.
'''

def test():  #NO USAR TEST 
 n = 100
 c = n * [0]
 num = int(input('Ingrese un valor entre 0 y 99 (con –1 corta): '))
 while num != -1:
  if 0 <= num < n:
    c[num] += 1
  else:
    print('Error... el número debía ser >= 0 y <', n)
  num = int(input('Ingrese otro valor entre 0 y 99 (con –1 corta): '))
 print('Resultados:')
 for i in range(n):
  if c[i] != 0:
   print('Número', i, '- Frecuencia de aparición', c[i])

if __name__ == '__main__':
 test()
