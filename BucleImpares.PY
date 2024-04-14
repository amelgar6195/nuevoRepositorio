#Bucle Impares 
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')
numero1 = int(input("Introduce un número entero positivo: "))
for i in range(1, numero1+1, 2):
    print(i, end=", ")