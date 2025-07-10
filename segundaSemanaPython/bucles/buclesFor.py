# #IMPRIMIR ELEMENTOS DE UNA LISTA
frutas = ["naranja", "cereza", "manzana"]

for i in frutas:
    print(i)

# #TABLA DE MULTIPLICAR
num = int(input("Introduce un número para ver su tabla de multiplicación del 1-10: "))

for multiplo in range(-1, 10):
    multiplo = multiplo + 1
    print(f"{num} * {multiplo} = {num * multiplo}")

#CUENTA ELEMENTOS POSTIVOS
lista = [1, -2, 3, 4, -5, 6]
contador = 0

for numero in lista:
    if numero >= 0:
        contador = contador + 1
print(f"{contador} números positivos")
