#Bucle en Reversa
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")