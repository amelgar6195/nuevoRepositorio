#Ejercicio uno confirmar si es mayor de Edad
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')

edad= int(input("Digite su edad "))
if edad< 18:
    print("Eres Menor de Edad Estudia")
else: print ("Eres Mayor de edad busca Trabajo")