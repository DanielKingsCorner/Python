# #BUSCAR UN NÚMERO EN LA LISTA
lista = [1, -2, 3, 4, -5, 6]
entrada = int(input("Introduzca un número: "))

for num in lista:
    if entrada == num:
        print(f"{entrada} está dentro de la lista")

#GENERAR UNA LISTA DE CUADRADOS
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = []
for num in lista1:
    cuadrado = num ** 2
    lista2.append(cuadrado)
print(lista2)
#FORMA SIMPLIFICADA ---FALTA POR ACABAR---
# lista = []

# for num in range(1, 11):



#MENU INTERACTIVO
lista = []
while True:
    print("1. Ver lista")
    print("2. Agragar elemento")
    print("3. Salir")
    
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        if len.lista == 0:
            print("La lista está vacía, por favor introduzca un valor primero")
        else:
            print(lista)
    
    elif opcion == 2:
        aniadido = int(input("Añade un valor a la lista: "))
        lista.append(aniadido)

    elif opcion == 3:
        print("Adios")
        break

    else:
        print("Opción no válida. Intentalo de nuevo.")
