#Productos separados por lineas de una canasta
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')


cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))