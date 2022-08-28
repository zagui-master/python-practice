'''
Realizar un programa que permita determinar de una serie de números ingresados 
cuales corresponde a celular. Finaliza al digitar 0.
'''

from ast import parse


print("Ingrese 10  de numeros ")
entrada = int(input(".... "))
invertir = str(entrada)

while len(invertir) != 0:
    if len(invertir) == 10:
        if invertir[0] == "3":
            print("El numero ", invertir, " es un numero de celular")
            break
    else:
        print("Ingrese 10  de numeros ")
        entrada = int(input(".... "))
