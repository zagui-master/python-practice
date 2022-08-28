
import os
import messages.constantes as constantes
import accounds.accounds as accounds
import balances.balance as balance
accound = accounds
msg = constantes
balance = balance


def retirar():
    os.system("cls")
    print("-----------------------------------")
    print("        RETIRANDO DINERO")
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
            monto_a_retirar = float(input(msg.MONTO_A_RETIRAR))

            if(balance.saldo < monto_a_retirar):
                os.system("cls")
                print("----------------------------------")
                print(msg.SALDO_INSUFICIENTE)
                print(" Su cuenta tiene ", balance.saldo,
                      " y el retiro requiere ", monto_a_retirar)
                print("----------------------------------")
            else:
                balance.saldo = balance.saldo - monto_a_retirar
                os.system("cls")
                print("Se retiraron ", monto_a_retirar,
                      " de la cuenta ", numero_cuenta_de_usuario)
                print(msg.SALDO_ACTUAL, balance.saldo)
                return balance.saldo
    else:
        os.system("cls")
        print(msg.NUMERO_DE_CUENTA_NO_ENCONTRADO)
        print("-----------------------------------")
