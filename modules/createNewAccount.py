import os
import accounds.accounds as accounds
accound = accounds


def crear_cuenta():
    os.system("cls")
    print("-----------------------------------")
    print("     CREANDO NUEVA CUENTA")
    print("-----------------------------------")
    nombre_de_usuario = str(input("   Ingrese su nombre... "))
    numero_de_cuenta = int(input("   Ingrese su numero de cedula...  "))
    new_user = {"nombre de usuario": nombre_de_usuario,
                "numero de cuenta": numero_de_cuenta}
    os.system("cls")
    print("   Cuenata creada con exito")
    print("   Su numero de cuenta es = ", numero_de_cuenta)
    print("-----------------------------------")
    accound.cuentas_de_usuario.append(new_user)
    return accound.cuentas_de_usuario
