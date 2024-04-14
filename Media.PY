#Media de cada Numero
#Aaron Melgar

import os
os.system('cls' if os.name =='nt' else 'clear')

def media(sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample. 
    """
    return sum(sample)/len(sample)

print(media([1, 2, 3, 4, 5]))
print(media([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))