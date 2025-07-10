#EL USUARIO INTRODUCE NUMEROS QUE METE EN UNA LISTA Y LE DA LA VUELTA
lista1 = []


for _ in range(5):
    dato = int(input("Introduce un número: "))
    lista1.append(dato)

lista1.reverse()

print(lista1)