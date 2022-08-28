'''
Realizar una aplicación para el control de elementos tecnológicos de una 
Universidad en la cual se registre, el tipo de dispositivo, marca, color, referencia, 
ubicación y responsable del mismo. Finaliza cuando el número de la referencia sea
CERO (0). Mostrar la información por pantalla.
'''

import os

dispositivos = []

tipo_de_dispositivo = input("-Tipo de dispositivo = ")
marca = input("-Marca = ")
color = input("-Color = ")
referencia = int(input("-Referencia = "))
ubicacion = input("-Ubicación = ")
responsable = input("-Responsable = ")
os.system("cls")

new_dispositivo = {"dispositivo": tipo_de_dispositivo, "marca": marca, "color": color,
                   "referencia": referencia, "ubicacion": ubicacion, "responsable": responsable}
dispositivos.append(new_dispositivo)


while referencia != 0:
    tipo_de_dispositivo = input("-Tipo de dispositivo = ")
    marca = input("-Marca = ")
    color = input("-Color = ")
    referencia = int(input("-Referencia = "))
    ubicacion = input("-Ubicación = ")
    responsable = input("-Responsable = ")
    os.system("cls")

    dispositivo = {"dispositivo": tipo_de_dispositivo, "marca": marca, "color": color,
                   "referencia": referencia, "ubicacion": ubicacion, "responsable": responsable}
    dispositivos.append(dispositivo)


for dispositivo in dispositivos:
    print("*********************************")
    print("-Dispositivo = ", dispositivo["dispositivo"])
    print("-Marca = ", dispositivo["marca"])
    print("-Color = ", dispositivo["color"])
    print("-Referencia = ", dispositivo["referencia"])
    print("-Ubicacion = ", dispositivo["ubicacion"])
    print("-Responssable = ", dispositivo["responsable"])
    print("*********************************")
