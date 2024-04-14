#Si eres mayor de edad y ganas salario tienes que tributar si no no
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')

edad = int(input("Digita tu edad "))
ingresos = float(input("Digita tus ingresos totales mensuales "))

if edad >18 and ingresos >= 12000:
    print("Tienes que pagar impuestos")
else:
    print("No tienes que pagar impuestos no tienes pisto")

