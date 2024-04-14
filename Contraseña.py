#Segungo Programa Introduce la contraeña
#Aaron melgar

import time

import os
os.system('cls' if os.name =='nt' else 'clear')

llave="1234"
contra=(input("Introduce la contraeña "))
if llave==contra.lower():
    print("Contraseña Correcta ganaste 1millon de Dolares")
else:
    print("Contraseña incorrecta Explotaras en 5 segundos")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
