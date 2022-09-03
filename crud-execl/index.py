from datetime import datetime
import os
from module import filterItem
from module import readItem
from module import updateItem
from module import addItem
from module import deleteItem

filter = filterItem
read = readItem
update = updateItem
add = addItem
delete = deleteItem

rutaExcel = "C:/Users/Administrador/Desktop/Bugs_crud.xlsx"


datosActualizados = {"titulo": "", "descripcion": "", "estado": "", "fecha inicio": "", "fecha finalizacion": ""}

while True:

    print("Indique la accion que desea realizar")
    print("  [1] Consultar")
    print("  [2] Actualizar")
    print("  [3] Crear nueva tarea")
    print("  [4] Borrar")
    accion = input("Escriba la opcion... ")
    os.system("cls")

    if not (accion == "1") and not (accion == "2") and not (accion == "3") and not (accion == "4"):
        print("Comando invalido por favor elija una opcion valida")

    elif accion == "1":
        opc_consulta = ""
        print("Indique la tarea que desea consultar: ")
        print("  [1] Todas las taeras")
        print("  [2] En espera")
        print("  [3] En ejecucion")
        print("  [4] Por aprovar")
        print("  [5] Finalizada")
        opc_consulta = input("Escriba la tarea que desea consultar...  ")

        if opc_consulta == "1":
            print()
            print()
            print("** Consultando todas las tareas **")
            read.leer(rutaExcel, "todo")

        elif opc_consulta == "2":
            print()
            print()
            print("** Consultando tareas en espera **")
            read.leer(rutaExcel, "En espera")

        elif opc_consulta == "3":
            print()
            print()
            print("** Consultando tareas en ejecucion **")
            read.leer(rutaExcel, "En ejecucion")

        elif opc_consulta == "4":
            print()
            print()
            print("** Consultando tareas por aprobar **")
            read.leer(rutaExcel, "Por aprobar")

        elif opc_consulta == "5":
            print()
            print()
            print("** Consultando tareas finalizadas **")
            read.leer(rutaExcel, "Finalizadas")

    elif accion == "2":
        datosActualizados = {"titulo": "", "descripcion": "", "estado": "", "fecha inicio": "",
                             "fecha finalizacion": ""}

        print("** Actualizar datos")
        print()
        id_Actualizar = int(input("Indique el Id de la tarea que desae actualizar"))
        print()
        print("** Nuevo titulo **")
        print("** Nota : si no desea actualizar el titlulo solo oprima la tecla ENTER **")
        datosActualizados["titulo"] = input("Indique el nuevo titulo de la tarea")
        print()
        print("** Nueva descripcion **")
        print("** Nota : si no desea actualizar la descripcion solo oprima la tecla ENTER")
        datosActualizados["descripcion"] = input("Indique la nueva descripcion de la tarea")
        print()
        print("** Nuevo estado **")
        print("  [2] En espera")
        print("  [3] En ejecucion")
        print("  [4] Por aprovar")
        print("  [5] Finalizada")
        print("** Nota : si no desea actualizar el estadom solo aprima la tecla ENTER **")
        estadoNuevo = input("Indique el nuevo estado de la tarea")

        if estadoNuevo == "2":
            datosActualizados["estado"] = "En espera"

        elif estadoNuevo == "3":
            datosActualizados["estado"] = "En ejecucion"

        elif estadoNuevo == "4":
            datosActualizados["estado"] = "Por aprobar"

        elif estadoNuevo == "5":
            datosActualizados["estado"] = "Finalizada"
            datosActualizados["fecha finalizacion"] = str(now.day) + "/ " + str(now.month) + "/" + str(now.year)

        now = datetime.now()
        datosActualizados["fecha inicio"] = str(now.day) + "/ " + str(now.month) + "/" + str(now.year)
        update.actualizar(rutaExcel, id_Actualizar, datosActualizados)
        print()

    elif accion == "3":
        datosActualizados = {"titulo": "", "descripcion": "", "estado": "", "fecha inicio": "",
                             "fecha finalizacion": ""}

        print("** Crear nueva tarea **")
        print()
        datosActualizados["** Titulo **"] = input("Indique el titulo de la tarea")
        print()

        print()
        datosActualizados["** Descripcion **"] = input("Indique la descripcion de la tarea")
        print()

        datosActualizados["estado"] = "En espera"
        now = datetime.now()
        datosActualizados["fecha inicio"] = str(now.day) + "/ " + str(now.month) + "/" + str(now.year)
        datosActualizados["fecha finalizacion"] = ""
        add.agregar(rutaExcel, datosActualizados)

    elif accion == "4":
        print("")
        print("** Eliminar tarea **")
        iden = int(input("Indique el Id de la tarea que desea eliminar... "))
        delete.borrar(rutaExcel, iden)
