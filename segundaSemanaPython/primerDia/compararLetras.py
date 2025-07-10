#COMPARA LA PRIMERA LETRA Y LA ÚLTIMAdani
num1 = input("Dime el primer nombre: ").lower()
num2 = input("Dime el segundo nombre: ").lower()

if num1[0] == num2[0]:
    print("La primera letra de ambos nombres coincide")

else:
    print("La primera letra de ambos nombres no coincide")

if num1[-1] == num2[-1]:
    print("La última letra de ambos nombres coincide")

else:
    print("La última letra de ambos nombres no coincide")