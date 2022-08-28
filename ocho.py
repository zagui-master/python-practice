'''
Realizar una aplicación que le permita a un parqueadero registrar los vehículo por 
la placa que ingresan, el tiempo de duración en horas y el cobro respectivo por el 
tiempo del servicio (valor X hora $1.000 ). Finaliza al digitar la letra N, (No desea 
continuar).
'''
import os


VALOR_HORA = 1000
vehiculos = []

print("Parqueadero la 10")
print("¿ Desea agregar un vehiculo ? ")
print("-Si = s ")
print("-No = n")
option = str.lower((input("... ")))
os.system("cls")


while option == "s":
    numero_de_placa = (input("_Ingrese la palca del vehiculo.... "))
    tiempo = float(
        input("_Ingres el tiempo que estara en el parqueadero... "))

    new_vehiculo = {"placa": numero_de_placa,
                    "tiempo": tiempo, "deuda": tiempo*VALOR_HORA}
    vehiculos.append(new_vehiculo)

    print("¿ Desea agregar un vehiculo ? ")
    print("Si = s ")
    print("No = n")
    option = str.lower((input("... ")))
    os.system("cls")


if(len(vehiculos) != 0):
    for vehiculo in vehiculos:
        print("*************************")
        print("-Placa = ", vehiculo["placa"])
        print("-Tiempo = ", vehiculo["tiempo"])
        print("-Total a pagar = ", vehiculo["deuda"])
        print("*************************")
