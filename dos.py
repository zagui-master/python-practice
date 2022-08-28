'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados.
'''

print("Ingrese muneros al azar")
entrada = int(input("... "))
arrayNumeros = []
arrayNumeros.append(entrada)

while entrada != 0:
    print("Ingrese muneros al azar")
    entrada = int(input("... "))
    arrayNumeros.append(entrada)


suma = sum(arrayNumeros)
print("La suma de todos los numero es ", suma)
print("Fin del programa")
