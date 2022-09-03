from math import *
import os


def areaPerimetro():
    count = 0
    lados = []

    while count != 3:
        count += 1
        os.system("cls")
        print("Ingrese la medida del lado ", count)
        lado = float(input("... "))
        lados.append(lado)

    t = (lados[0] + lados[1] + lados[2]) / 2
    s = sqrt((t * (t - lados[0])) * (t - lados[1]) * (t - lados[2]))

    os.system("cls")
    print("Calculo : ", round(s))


