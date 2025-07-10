#Dice que numero es par
#Declaramos variables
num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

if num1 %2 == 0 and num2 %2 == 0:
    print(f"{num1} y {num2} son pares")

elif num1 %2 == 0 and num2 %2 == 1:
    print(f"Solo {num1} es par")

elif num1 %2 == 1 and num2 %2 == 0:
    print(f"Solo {num2} es par")

elif num1 %2 == 1 and num2 %2 == 1:
    print("Ningún numero es par")


