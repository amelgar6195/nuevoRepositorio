#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética  (3+22⋅5)2 .
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')

print(((3 + 2) / (2 * 5)) ** 2)

respuesta = input("¿Te gustó el programa? (si/no): ")
if respuesta.lower() == "si":
    print("💓")