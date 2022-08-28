import os
import messages.constantes as constantes
import accounds.accounds as accounds
import balances.balance as balance
accound = accounds
msg = constantes
balance = balance


def depositar():
    os.system("cls")
    print("-----------------------------------")
    print("  DEPOSITANDO DINERO A LA CUENTA")
    print("-----------------------------------")
    numero_cuenta_de_usuario = int(input(msg.INGRESE_NUMERO_DE_LA_CUENTA))
    print("-----------------------------------")
    if(numero_cuenta_de_usuario in accound.cuentas_de_usuario):
        monto = float(input(msg.INGRESE_MONTO_A_DEPOSITAR))
        print("----------------------------------")
        balance.saldo = monto + balance.saldo
        os.system("cls")
        print("Se deposito ", monto,
              " a la cuenta ", numero_cuenta_de_usuario)
        print(msg.SALDO_ACTUAL, balance.saldo)
        return balance.saldo
    else:
        os.system("cls")
        print(msg.NUMERO_DE_CUENTA_NO_ENCONTRADO)
        print("-----------------------------------")
