
def creacimientoPoblacional():

    years = [5, 10, 20]

    print("Ingrese el numero de habitantes actual")
    numeroDeHabitantes = int(input("... "))

    for year in years:

        poblacionTotal = round(numeroDeHabitantes*(1+0.0208)**year)

        print("---------------------------------------------")
        print("En ", year, " años el numero de habitanes es:")
        print("Numero de habitantes ", poblacionTotal)
        print("---------------------------------------------")
        print()