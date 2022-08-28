import os
import messages.constantes as constantes
import accounds.accounds as accounds
import balances.balance as balance
accound = accounds
msg = constantes
balance = balance


def trasnferir():
    os.system("cls")
    print("-----------------------------------")
    print("     TRANSFIRIENDO DINERO")
    print("-----------------------------------")
    numero_cuenta_de_usuario = int(input(msg.INGRESE_NUMERO_DE_LA_CUENTA))
    print("-----------------------------------")

    if(numero_cuenta_de_usuario in accound.cuentas_de_usuario):
        if(balance.saldo <= 0):
            os.system("cls")
            print("----------------------------------")
            print(msg.CUENTA_SIN_FONDOS)
            print("----------------------------------")
        else:

            print("----------------------------------")
            numero_de_cuenta = int(input(msg.INGRESE_NUMERO_DE_CUENTA_DESTINO))
            print("----------------------------------")

            monto_a_transferir = float(input(msg.MONTO_A_TRANSFERIR))

            if(balance.saldo < monto_a_transferir):
                os.system("cls")
                print("----------------------------------")
                print(msg.SALDO_INSUFICIENTE)
                print(" Su cuenta tiene ", balance.saldo,
                      " y la transferecia requiere ", monto_a_transferir)
                print("----------------------------------")
            else:
                balance.saldo = balance.saldo - monto_a_transferir
                os.system("cls")
                print("----------------------------------")
                print("  Se transfirio ", monto_a_transferir,
                      " a la cuenta ", numero_de_cuenta)
                print(msg.SALDO_ACTUAL, balance.saldo)
                print("----------------------------------")
                return balance.saldo
    else:
        os.system("cls")
        print(msg.NUMERO_DE_CUENTA_NO_ENCONTRADO)
        print("-----------------------------------")
