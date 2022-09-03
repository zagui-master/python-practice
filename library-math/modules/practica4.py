import os

def calificacion():

    count = 0
    tareas = []

    porcentageExamen = 0.7
    porcentageLecciones = 0.2
    porcentageTarea = 0.1

    notaExamen = float(input("Ingrese la nota del examen... "))
    os.system("cls")
    notaLecciones = float(input("Ingrese la nota de las lecciones... "))

    while count != 3:
        count += 1
        os.system("cls")
        print("Ingrese la nota de tarea ", count)
        notaTareas = int(input("... "))
        tareas.append(notaTareas)

    sumaDeLasTareas = sum(tareas)

    notaFinalExamen = notaExamen * porcentageExamen
    notaFinalLecciones = notaLecciones * porcentageLecciones
    notaFinalTareas = sumaDeLasTareas * porcentageTarea

    notaFinal = notaFinalExamen + notaFinalLecciones + notaFinalTareas

    os.system("cls")
    print("La nota final Del Examen es : ", notaFinal)
