#Precios de Entrada de un Negocio
#Aaron Melgar


import os
os.system('cls' if os.name =='nt' else 'clear')
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "Lempiras.")