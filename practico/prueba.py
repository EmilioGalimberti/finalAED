def producto(a, b):
     if a == 0 or b == 0:
         return 0
     return  a + producto(a, b-1)

print(producto(1, 5))

