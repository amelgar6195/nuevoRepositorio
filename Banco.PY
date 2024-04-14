#Banco 
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')


saldo = 10000

while True:
    print("\nBienvenido al Banco")
    print("1. Depositar saldo")
    print("2. Retirar saldo")
    print("0. Salir")
    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print(f"Depósito exitoso. Saldo actual: {saldo}")
    elif opcion == 2:
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Saldo actual: {saldo}")
        else:
            print("Fondos insuficientes.")
    elif opcion == 0:
        print("Gracias por utilizar nuestros servicios.")
        break
    else:
        print("Opción no válida.")