#TE DICE DEPENDIEDO DEL CLIMA Y LOS GRADOS LO QUE TE TIENES QUE PONER
try:
    temperatura = int(input("Introduzca la temperatura actual: "))
except ValueError: print("La temperatura tiene que ser un número entero")

clima = (input("Introduzca el tiempo actual (soleado o lluvioso): "))

climaMinusculas = clima.lower()   


if clima.lower == "soleado" and temperatura > 20:
    print("Tienes que ponerte camiseta y pantalones cortos")

elif clima.lower == "soleado" and temperatura <= 20:
    print("Tienes que ponerte chaqueta ligera")

elif clima.lower == "lluvioso" and temperatura > 15:
    print("Tienes que ponerte chaqueta impermeable")

elif clima.lower == "lluvioso" and temperatura <= 15:
    print("Tienes que ponerte abrigo y paragüas")

else:
    print("Información del clima no reconocida")