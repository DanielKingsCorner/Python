#HACE EL DESCUENTO A UN PRODUCTO
#Pedimos el dato al usuario
precioBase = float(input("¿Cuál es el precio de tu producto?: "))

#Calculamos el precio
descuento = precioBase *(36/100)
precioFinal = precioBase - descuento

#Imprimimos el precio final
print (f"Aplicando el descuento, el precio de tu producto es {precioFinal:.2f}")