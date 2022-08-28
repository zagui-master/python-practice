import os
import messages.constantes as constantes
import accounds.accounds as accounds
import balances.balance as balance
accound = accounds
msg = constantes
balance = balance


def consultar_saldo():
    os.system("cls")
    print("-----------------------------------")
    print("       CONSULTANDO SALDO ")
    print("-----------------------------------")
    numero_cuenta_de_usuario = int(input(msg.INGRESE_NUMERO_DE_LA_CUENTA))

    for cuenta in accound.cuentas_de_usuario:
        if(cuenta["numero de cuenta"] == numero_cuenta_de_usuario):
            print("-----------------------------------")

            '''
        if(numero_cuenta_de_usuario in accound.cuentas_de_usuario):
            os.system("cls")
            print("-----------------------------------")
            print("   Su saldo actual es = ", balance.saldo)
            print("-----------------------------------")
            return balance.saldo
        else:
            os.system("cls")
            print(msg.NUMERO_DE_CUENTA_NO_ENCONTRADO)
            print("-----------------------------------")
            '''
