#TE HACE UN MENÚ DEPENDIENDO DE TU EDAD Y DE SI ERES MIEMBRO Y TE HACE UN DESCUENTO
print("¿A qué grupo perteneces?")
print("1- Niño (0-12 años)")
print("2- Adulto (13-64 años)")
print("3- Jubilado (65 años o más)")

opcion = int(input("Introduzca el número del grupo al que pertenece(1, 2, 3): "))
miembroMin = input("¿Tiene una membresía?(si, no): ").lower()
#miembroMin = miembro.lower()

if opcion == 1:
    if miembroMin == "si":
        print("Tienes que pagar", 5 - (5 * 15 / 100))
    else:
        print("Tienes que pagar 5€")
elif opcion == 2:
    if miembroMin == "si":
        print("Tienes que pagar", 10 - (10 * 15 / 100))
    else:
        print("Tienes que pagar 10€")
elif opcion == 3:
    if miembroMin == "si":
        print("Tienes que pagar", 8 - (8 * 15 / 100))
    else:
        print("Tienes que pagar 8€")
else:
    print("Opción no válida")

#edad = (input("Introduzca su edad: "))
#miembro = bool(input("¿Tiene una membresía?: "))
#miembroMin = miembro.lower
#precioNinio = 5
#precioJubilado = 8
#precioAdulto = 10

#if miembroMin == "si":

#edad <= 12:
#    print("Pagas 5€")

#elif edad >= 65:
#    print("Pagas 8€")

#elif edad > 12 and edad < 65:
#    print("Pagas 10€")