#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')

numero1 = float(input("¿Cantidad a invertir? "))
numero2 = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
for i in range(años):
    numero1 *= 1 + numero2 / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(numero1, 2)))