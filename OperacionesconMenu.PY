#Operaciones con Menu
#Aaron Melgar


import os
os.system('cls' if os.name =='nt' else 'clear')

import math

def menu():
    print("1. Multiplicar")
    print("2. Dividir")
    print("3. Raíz cuadrada")
    print("4. Número binario")
    print("5. Potencia")
    print("6. Binario de un número")
    opcion = int(input("Elige una opción: "))
    return opcion

def operaciones(opcion, numero):
    if opcion == 1:
        n2 = int(input("Introduce otro número: "))
        print("El resultado de la multiplicación es: ", numero * n2)
    elif opcion == 2:
        n2 = int(input("Introduce otro número: "))
        print("El resultado de la división es: ", numero / n2)
    elif opcion == 3:
        print("La raíz cuadrada de", numero, "es: ", math.sqrt(numero))
    elif opcion == 4:
        print("El número binario de", numero, "es: ", bin(numero))
    elif opcion == 5:
        n2 = int(input("Introduce la potencia: "))
        print("El resultado de la potencia es: ", pow(numero, n2))
    elif opcion == 6:
        print("El binario de", numero, "es: ", format(numero, 'b'))

numero = int(input("Introduce un número: "))
opcion = menu()
operaciones(opcion, numero)
