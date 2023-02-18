#1. Operaciones de orden con 3 nros.
#Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es el resto de la división de los dos primeros.

a = int(input(">> INGRESE UN NUMERO: "))
b = int(input(">> INGRESE UN NUMERO: "))
c = int(input(">> INGRESE UN NUMERO: "))

if a > b and a > c :
    if b>c:
        print("Lo numeros orednados de mayor a menor serian: ", a , b , c)
        resto = a % b
        if c == resto:
            print("El tercero es el resto de la división de los dos primeros.")
        else:
            print("El tercero NO es el resto de la división de los dos primeros.")
    else:
        print("Los numeros orednados de mayor a menor serian: ", a , c , b)
        resto = a % c
        if b == resto:
            print("El tercero es el resto de la división de los dos primeros.")
        else:
            print("El tercero NO es el resto de la división de los dos primeros.")
elif b>c:
    if a>c:
        print("lo numeros orednados de mayor a menor serian: ", b , a , c)
        resto = b % a
        if c == resto:
            print("El tercero es el resto de la división de los dos primeros.")
        else:
            print("El tercero NO es el resto de la división de los dos primeros.")
    else:
        print("lo numeros orednados de mayor a menor serian: ", b , c , a)
        resto = b % c
        if a == resto:
            print("El tercero es el resto de la división de los dos primeros.")
        else:
            print("El tercero NO es el resto de la división de los dos primeros.")
elif a > b:
    print("lo numeros orednados de mayor a menor serian: ", c , a , b)
    resto = a % c
    if b == resto:
        print("El tercero es el resto de la división de los dos primeros.")
    else:
        print("El tercero NO es el resto de la división de los dos primeros.")
else:
    print("lo numeros orednados de mayor a menor serian: ", c , b , a)
    resto = c % b
    if a == resto:
            print("El tercero es el resto de la división de los dos primeros.")
    else:
            print("El tercero NO es el resto de la división de los dos primeros.")



# otra forma de sacar

# Primero: ordenar los dos primeros numeros...
if a > b:
 men, may = b, a
else:
 men, may = a, b
# Segundo: ordenar los tres numeros...
if c > may:
 med, may = may, c
else:
 if c > men:
    med = c
 else:
    med, men = men, c
# Visualización de los resultados ordenados...
print('Menor:', men)
print('Medio:', med)
print('Mayor:', may)


