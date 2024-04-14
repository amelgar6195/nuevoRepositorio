#Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
if paga > 3000:
    print("Tu paga es", paga, "Cuida tu trabajo")
elif paga > 15000:
    print("Tu paga es", paga, "Ganas mínimo, búscate otro trabajo")
else:
    print("Tu paga es", paga)
