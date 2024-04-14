#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')

nombre = input("¿Cómo te llamas? ")
n = int(input("Introduce un número entero: "))
emoji = "\U0001F600"  # Emoji de cara sonriente

for _ in range(n):
    print(f"{nombre} {emoji}")