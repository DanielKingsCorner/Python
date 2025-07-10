#Control de errores de posibles datos no válidos
try:
    num = int(input("Introduce un número entero positivo para hacer su tabla de multiplicar: "))
except ValueError: print("Error: El dato tiene que ser un número entero...")

#Bucle que va sumando 1 hasta llegar a 10
for multiplo in range(-1, 10):
    multiplo = multiplo + 1
    print(f"{num} x {multiplo} = {num * multiplo}")