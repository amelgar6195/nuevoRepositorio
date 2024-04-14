#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
#Aaron Melgar

import os

while True:
    os.system('cls' if os.name =='nt' else 'clear')
    n = int(input("Introduce un número entero: "))
    if n % 2 == 0:
        print("El número " + str(n) + " es par")
    else:
        print("El número " + str(n) + " es impar")

    opcion = input("Presiona 1 para continuar o 0 para salir: ")
    if opcion == '0':
        break
