_author_ = 'Emilio'
#------------------------------EJEMPLO 0 REPASO------------------
def carga(v1):
    for i in range(len(v1)): # 0 1 2
        v1[i] = int(input('Ingrese una edad:'))

def posiciones_par(v1):
    for i in range(len(v1)):
        if i % 2 == 0:
            print('Las edades en posicion par son: ', v1[i])

#------------------EJEMPLO PARALELOS------------------
def read(nombres, sueldos, edades):
    n = len(nombres)
    for i in range(n):
        nombres[i] = input('Ingrese el nombre del empleado:')
        sueldos[i] = float(input('Ingrese el sueldo del empleado:'))
        edades [i] = int(input('Ingrese la edad del empleado:'))

def sort(nombres, sueldos, edades):
    n = len(nombres)
    for i in range(n-1):
        for j in range(i+1, n):
            if nombres[i] > nombres[j]:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                edades[i], edades[j] = edades[j], edades[i]
                sueldos[i], sueldos[j] = sueldos[j], sueldos[i]

'Mostrar nombres de empleados mayores a 21 con sueldo menor a 10000 ordenados alfabeticamente'
def mostrar_nombres(nombres, edades, sueldos):
    n = len(nombres)
    for i in range(n):
        if edades[i] > 21 and sueldos[i] < 10000:
            print(' Nombre de empleado:', nombres [i])
