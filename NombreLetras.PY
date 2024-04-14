#Cuantas letras tiene tu nombre
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')

nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")