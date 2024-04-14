#Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')
numero1 = float(input("Introduce el dividendo: "))
numero2= float(input("Introduce el divisior: "))
if numero2 == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(numero1/numero2)