#Escoger si desea que realize la operacion Raiz cuadrada,potencia o binario de el numero solicitato
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')

import math

numero = float(input("Introduce un número: "))
operacion = input("¿Qué operación deseas realizar? (raiz/potencia/binario): ")

if operacion == "raiz":
    print(f"La raíz cuadrada de {numero} es {math.sqrt(numero)}")
elif operacion == "potencia":
    potencia = int(input("¿A qué potencia deseas elevar el número?: "))
    print(f"{numero} elevado a la {potencia} es {math.pow(numero, potencia)}")
elif operacion == "binario":
    print(f"El valor binario de {numero} es {bin(int(numero))}")
else:
    print("Operación no válida")
