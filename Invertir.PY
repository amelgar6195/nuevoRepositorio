#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.
#Aaron Melgar
import os
os.system('cls' if os.name =='nt' else 'clear')

import os

def clear_screen():
    os.system('cls' if os.name =='nt' else 'clear')

def calculate_investment(cantidad, interes, años):
    return round(cantidad * (interes / 100 + 1) ** años, 2)

def main():
    clear_screen()
    print("Bienvenido al simulador de inversiones")
    print("1. Calcular inversión")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a invertir: "))
        interes = float(input("Ingrese el interés porcentual anual: "))
        años = int(input("Ingrese el número de años: "))
        capital_final = calculate_investment(cantidad, interes, años)
        print(f"Capital final: {capital_final}")
    elif opcion == "2":
        print("Gracias por utilizar el simulador. ¡Hasta la próxima!")
    else:
        print("Opción no válida. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()