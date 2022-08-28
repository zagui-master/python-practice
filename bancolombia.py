'''
Realizar un programa que realice el registro de un cliente, el registro de una cuenta 
de ahorros, consignación de dinero a la cuenta, retiro de dinero de la cuenta y 
consulta de saldo. (utilizar funciones).
'''


import messages.constantes as constantes

from modules.createNewAccount import crear_cuenta
from modules.checkBalance import consultar_saldo
from modules.withdrawals import retirar
from modules.deposit import depositar
from modules.transfer import trasnferir

from modules.screen_messages.initialMessage import msgInicial
from modules.screen_messages.finalMessage import mensaje_final
from modules.screen_messages.menu import menu

msg = constantes

msgInicial()
menu()
opcion = int(input(msg.INGRESE_OPCION))

while (opcion != 6):

    if(opcion == 1):
        crear_cuenta()

    if(opcion == 2):
        consultar_saldo()

    if(opcion == 3):
        retirar()

    if(opcion == 4):
        depositar()

    if(opcion == 5):
        trasnferir()

    menu()
    opcion = int(input("   Ingrese la opcion... "))

mensaje_final()
