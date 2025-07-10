#CAJERO AUTOMÁTICO
saldoInicial = 2000

while True:
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar dinero")
    print("4. Salir")
    
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        ingreso = int(input("¿Cuánto dinero quieres ingresar?: "))
        saldoInicial += ingreso #A saldoInicial se le suma el ingreso y se actualiza la cantidad de saldoInicial
    
    elif opcion == 2:
        retiro = int(input("¿Cuánto dinero quieres retirar?: "))
        if retiro < saldoInicial:
            saldoInicial -= retiro #A saldoInicial se le resta el ingreso y se actualiza la cantidad de saldoInicial
        else:
            print("Saldo insuficientes")
    
    elif opcion == 3:
        print(f"Saldo actual: {saldoInicial}")

    elif opcion == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intentalo de nuevo.")
