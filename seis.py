'''
Realizar un programa que me permita obtener el factorial de un número entero
ingresado por teclado.
'''

from math import factorial

entrada = int(input("Ingrese un numero... "))
resultado = factorial(entrada)
print("El factorial del numero ", entrada, " es ", resultado)
