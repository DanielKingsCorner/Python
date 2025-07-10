#Variable donde se almacena el saldo
importe = float(0)
#Bucle que mientras sea verdad, entre en el 2 (siempre es True)
while True:
    print("1- Agua (1.00€)")
    print("2- Refresco (1.50€)")
    print("3- Zumo (2.00€)")
    print("4- Salir")
    #Control de errores de posibles datos no válidos
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError: print("El producto seleccionado no existe...")

    if opcion == 1:
        print("Ha seleccionado 'Agua': ")
        print("Por favor, inserte dinero")
        print(f"Cantidad actual: {importe:.2f}€")
        #Control de errores de posibles datos no válidos
        try:
            #Variable donde se guarda la cantidad de monedas que el usuario introduce
            ingreso = float(input("Introduzca monedas (0.50, 1.00, 2.00) o salir: "))
        except ValueError: print("La moneda introducida no es válida..")

        if ingreso == 0.50:
            importe = importe + 0.50
        if ingreso == 1.00:
            importe = importe + ingreso
        if ingreso == 2.00:
            importe = importe + ingreso
        #Print donde aparece la cantidad de saldo actualilzada
        print(f"Cantidad actual: {importe:.2f}€")
        resto = importe - 1
        if importe == 1.00:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Agua. Su cambio es: {resto:.2f}")
        if importe == 1.00:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Refresco. Su cambio es: {resto:.2f}")
        if importe == 2.00:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Agua. Su cambio es: {resto:.2f}")
        if importe < 1.00:
            print("Saldo insuficiente")

    if opcion == 2:
        print("Ha seleccionado 'Refresco': ")
        print("Por favor, inserte dinero")
        print(f"Cantidad actual: {importe:.2f}€")
        #Variable donde se guarda la cantidad de monedas que el usuario introduce
        ingreso = float(input("Introduzca monedas (0.50, 1.00, 2.00) o salir: "))
                 
        if ingreso == 0.50:
            importe = importe + 0.50
        if ingreso == 1.00:
            importe = importe + ingreso
            resto = importe - 1.00
        if ingreso == 2.00:
            importe = importe + ingreso
            resto = importe - 1.00  
        #Print donde aparece la cantidad de saldo actualilzada
        print(f"Cantidad actual: {importe:.2f}€")
        resto = importe - 1.50
        if importe == 1.50:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Refresco. Su cambio es: {resto:.2f}")
        if importe == 2.00:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Refresco. Su cambio es: {resto:.2f}")
        if importe < 1.50:
            print("Saldo insuficiente")

    if opcion == 3:
        print("Ha seleccionado 'Zumo': ")
        print("Por favor, inserte dinero")
        print(f"Cantidad actual: {importe:.2f}€")
        #Variable donde se guarda la cantidad de monedas que el usuario introduce
        ingreso = float(input("Introduzca monedas (0.50, 1.00, 2.00) o salir: "))
                 
        if ingreso == 0.50:
            importe = importe + 0.50
        if ingreso == 1.00:
            importe = importe + ingreso
            resto = importe - 1.00
        if ingreso == 2.00:
            importe = importe + ingreso
            resto = importe - 1.00  
        #Print donde aparece la cantidad de saldo actualilzada
        print(f"Cantidad actual: {importe:.2f}€")
        resto = importe - 2
        if importe == 2.00:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Refresco. Su cambio es: {resto:.2f}")
        if importe == 2.50:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Refresco. Su cambio es: {resto:.2f}")
        if importe == 3.00:
            importe = 0
            print(f"¡Compra exitosa! Aquí tiene su Refresco. Su cambio es: {resto:.2f}")
        if importe < 2.00:
            print("Saldo insuficiente")
    #Sale del programa
    if opcion == 4:
        print("Saliendo del programa...")
        break
                   

