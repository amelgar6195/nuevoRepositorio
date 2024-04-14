#Imprimier en pantalla todos los años cumplidos
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')
Edad = int(input("¿Cuántos años tienes? "))
for i in range(Edad):
    print("Has cumplido " + str(i+1) + " años")
