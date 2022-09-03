from math import *


def cilindroAreaYVolumen():

    radio = int(input("Ingrese el radio del cindro... "))
    altura = int(input("Ingrese la altura del cilindro... "))

    areaTotal = round((2 * pi * radio * altura) + 2 * pi * pow(radio, 2))

    volumen = round(pi * pow(radio, 2) * altura)

    print("El area total del cilindro es : ", areaTotal)
    print("El volumen total del cilinidro es : ", volumen)
