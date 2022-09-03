
def areaYVolumenTotalTrianfulo():

    print("---Datos para encontrar el volumen---")
    longitud = int(input("Ingrese la longitud... "))
    ancho = int(input("Ingrese el ancho... "))
    altura = int(input("Ingrese la altura... "))
    print("----------------------------------------")

    print("---Datos para encontrar el area total---")
    areaLateral = int(input("Ingrese el area lateral... "))
    areaBase = int(input("Ingrese el area de la base... "))
    print("----------------------------------------")

    areaTotal = areaLateral + 2 * areaBase
    volunenTotal = longitud * ancho * altura

    print("El volumen total es : ", volunenTotal)
    print("El area total es : ", areaTotal)