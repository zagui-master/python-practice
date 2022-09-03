import os


def calcularCompra():
    count = 0
    valores = [5000, 10000, 20000]
    articulos = []
    resultados = []

    print("-----------------------------")
    print("Calcular monto de la compra")
    print("-----------------------------")
    print()

    while count != 3:
        count += 1
        print("Ingrese cantidad articulos Tipo ", count)
        articulo = int(input("... "))
        articulos.append(articulo)

    os.system("cls")
    print("Calculando...")

    imp1 = (articulos[0] * valores[0]) * 0.053
    imp2 = (articulos[1] * valores[1]) * 0.080
    imp3 = (articulos[2] * valores[2]) * 0.16

    prom_compra = (articulos[0] + articulos[1] + articulos[2]) // 3

    Tpi = \
        ((articulos[0] * valores[0]) + imp1) + \
        ((articulos[1] * valores[1]) + imp2) + \
        ((articulos[2] + valores[2]) + imp3)

    resultados.append(imp1)
    resultados.append(imp2)
    resultados.append(imp3)
    count = 0

    print("Resultados")

    for resultado in resultados:
        count += 1
        print("Total Impuestos de articulo ", count, " es: ", resultado, "Pesos colombianos")

    print("Total a pagar con impuestos  : ", Tpi, " pesos colombianos")
    print("Promedio de compra articulo  : ", prom_compra)
