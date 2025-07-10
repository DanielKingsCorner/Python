

importe = float(0)
while True:
    print("1- Añadir pedido")
    print("2- Ver pedido")
    print("3- Borrar pedido")
    print("4- Salir")   
    try:
        opcion = int(input("Introduce la opción que quieres hacer con tu pedido(1, 2, 3, 4): "))
    except ValueError: print("La opción introducida no es válida...")
    if opcion == 1:
        print("1- Baja Taco: 4.25€")
        print("2- Burrito: 7.50€")
        print("3- Bowl: 8.50€")
        print("4- Nachos: 11.00€")
        print("5- Quesadilla: 8.50€")
        print("6- Super Burrito: 8.50€")
        print("7- Super Quesadilla: 9.50")
        print("8- Taco: 3.00€")
        print("9- Tortilla Salad: 8.00€")
        try:
            pedido = int(input("Indica que comida quieres añadir al carro(1, 2, 3, 4, 5, 6, 7, 8, 9): "))
        except ValueError: print("La opción introducida no es válida...")
        if pedido == 1:
            importe += 4.25
            sumaImporte = importe
        elif pedido == 2:
            importe += 7.50
            sumaImporte = importe
        elif pedido == 3:
            importe += 8.50
            sumaImporte = importe
        elif pedido == 4:
            importe += 11.00
            sumaImporte = importe
        elif pedido == 5:
            importe += 8.50
            sumaImporte = importe
        elif pedido == 6:
            importe += 8.50
            sumaImporte = importe
        elif pedido == 7:
            importe += 9.50
            sumaImporte = importe
        elif pedido == 8:
            importe += 3.00
            sumaImporte = importe
        elif pedido == 9:
            importe += 8.00
            sumaImporte = importe

    elif opcion == 2:
        if importe == 0:
            print("No hay nada en el carro")
        else:
            print(f"{importe}€")
            
    elif opcion == 3:
        importe = 0

    elif opcion == 4:
        print("Saliendo del programa...")
        break