#Dice cual es el numero mayor
num1 = float(input("Introduzca el primer número: "))
num2 = float(input("Introduzca el segundo número: "))
num3 = float(input("Introduzca el tercer número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor")

elif num1 < num2 and num1 > num3:
    print(f"{num2} es el mayor")

elif num1 > num2 and num1 < num3:
    print(f"{num3} es el mayor")
