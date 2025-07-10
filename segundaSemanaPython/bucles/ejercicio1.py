# QUE LA TEMPERATURA NO SEA MENOR A -273.15ºC (EL CERO ABSOLUTO)
temperatura = float(input("Introduzca una temperatura: "))

while temperatura < -273.15:
    print(f"{temperatura}ºC es una temperatura incorrecta")
    temperatura = float(input("Introduzca una temperatura: "))
print("Temperatura correcta")