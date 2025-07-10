#IMPRIME LOS NÚMEROS DEL 1 AL 30 PERO DEPENDIENDO DE SI ES MULTIPLO DE 3 Y 5 ESCRIBE OTRA COSA

for num in range(1, 31):
    if num % 3 == 0:
        print("Tres")

    if num % 5 == 0:
        print("Cinco")

    if num % 3 == 0 and num % 5 == 0:
        print("Tres y Cinco")

    else: 
        print(num)

#ENCONTRAR EL NÚMERO MAXIMO DE UNA LISTA SIN USAR FUNCIONES(EJEMPLO: .reverse .append etc...)
lista1 = [5, 8, 3, 7, 8, 9]

for num in range(5):
    dato = int(input("Introduce un número: "))
    if dato = 0:
        print()