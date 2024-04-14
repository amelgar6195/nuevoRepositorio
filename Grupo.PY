#Grupo al que perteneses
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')

nombre = input("¿Cómo te llamas? ")
sexo = input("¿Cuál es tu sexo (M o H)? ")
if sexo == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)