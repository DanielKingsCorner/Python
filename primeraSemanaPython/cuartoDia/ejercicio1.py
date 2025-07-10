#Añade un descuento por edades
# Declaramos la variable
edad = int(input("¿Qué edad tienes?: "))
#Si tiene 2 o menos años
if (edad <= 2):
    print("Al ser menor de 3 años es gratis")
#Si tiene entre 3 y 12
elif (edad >=3 and edad <=12):
    print("Al estar entre 3 y 12 años se aplica la tarifa niño")
#Si no se cumple ninguna de las dos condiciones anteriores
else: print("Al ser mayor de 12 años se aplica al tarifa de adulto")