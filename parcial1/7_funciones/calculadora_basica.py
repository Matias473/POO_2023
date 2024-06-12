"""
CALCULADORA NUMERO 1
entrada = True

while entrada:
    print("calculadora basica")
    print("\n")
    print("1-suma")
    print("2-resta")
    print("3-multiplicacion")
    print("4-division")
    print("5-salir")
    print("\n")
    eleccion = input("Elige la operacion que quieres realizar: ")

    if eleccion == "1" or eleccion == "+" or eleccion.upper() == "SUMA":
        n1 = float(input("Introduce el primer numero: "))
        n2 = float(input("Introduce el segundo numero: "))
        resultado = n1 + n2
        print(f"{n1} + {n2} = {resultado}")
    elif eleccion == "2" or eleccion == "-" or eleccion.upper() == "RESTA":
        n1 = float(input("Introduce el primer numero: "))
        n2 = float(input("Introduce el segundo numero: "))
        resultado = n1 - n2
        print(f"{n1} - {n2} = {resultado}")
    elif eleccion == "3" or eleccion == "*" or eleccion.upper() == "MULTIPLICACION":
        n1 = float(input("Introduce el primer numero: "))
        n2 = float(input("Introduce el segundo numero: "))
        resultado = n1 * n2
        print(f"{n1} * {n2} = {resultado}")
    elif eleccion == "4" or eleccion == "/" or eleccion.upper() == "DIVISION":
        n1 = float(input("Introduce el primer numero: "))
        n2 = float(input("Introduce el segundo numero: "))
        if n2 != 0:
            resultado = n1 / n2
            print(f"{n1} / {n2} = {resultado}")
        else:
            print("Error: Division por cero no es permitida.")
    elif eleccion == "5":
        entrada = False
    else:
        print("Opcion no valida. Por favor, elige una opcion valida.")
"""

#calculadora con funciones
from otras_funciones import *

def calculadora():
    while True:
        print("Calculadora básica \n")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir \n")
        eleccion = input("Elige la operación que quieres realizar: ")

        if eleccion in ["1", "2", "3", "4"]:
            n1 = float(input("Introduce el primer número: "))
            n2 = float(input("Introduce el segundo número: "))

            if eleccion == "1":
                print(f"{n1} + {n2} = {sumar(n1, n2)}")
            elif eleccion == "2":
                print(f"{n1} - {n2} = {restar(n1, n2)}")
            elif eleccion == "3":
                print(f"{n1} * {n2} = {multiplicar(n1, n2)}")
            elif eleccion == "4":
                print(f"{n1} / {n2} = {dividir(n1, n2)}")
        elif eleccion == "5":
            print("programa finalizado")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")

calculadora()
"""
#calculadora hecha en clase
import os
from otras_funciones import *

opcion = True    
while opcion:

    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion != "5":
       n1,n2 = solicitarNumeros()
       print(operacionAritmetica(n1, n2, opcion))
    else:
        opcion = False
        print("Ejecucion terminada")
"""