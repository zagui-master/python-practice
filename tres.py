'''
Steps

1-Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir
listado, 3-finalizar programa.

2-A continuación, el usuario debe poder
seleccionar una opción (1, 2 ó 3).

3-Si elige una opción incorrecta, informarle
del error.

4-El menú se debe volver a mostrar luego de ejecutada cada
opción,permitiendo volver a elegir.

Si elige las opciones 1 ó 2 se imprimirá
un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el
programa finalizará.
'''

import os


def optionOneOPtiotwo():
    print("****************************")
    print("Texto de refencia")
    print("****************************")


def menu():
    print("-------    Menu    -------")
    print("  Comenzar programa  = 1")
    print("  Imprimir listado   = 2")
    print("  Finalizar programa = 3")
    print("--------------------------")


def graciasPorUsarnosMsg():
    print("Gracias por usarnos")


def opcionNoValidaMsg():
    print("**************************************")
    print("  La opcion ", opcion, "no es valida")
    print("**************************************")


''''Muestra el menu'''
menu()
opcion = int(input(".... "))
os.system("cls")

while opcion == 1 or opcion == 2:
    os.system("cls")
    optionOneOPtiotwo()
    menu()
    opcion = int(input(".... "))

if opcion == 3:
    os.system("cls")
    graciasPorUsarnosMsg()

while opcion <= 0 or opcion > 3:
    os.system("cls")
    opcionNoValidaMsg()
    menu()
    opcion = int(input(".... "))

    while opcion == 1 or opcion == 2:
        os.system("cls")
        optionOneOPtiotwo()
        menu()
        opcion = int(input(".... "))

    if opcion == 3:
        os.system("cls")
        graciasPorUsarnosMsg()
        break
