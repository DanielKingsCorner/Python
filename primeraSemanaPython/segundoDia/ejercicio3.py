#CALCULA EL AREA CON EL DATO DEL RADIO
pi = 3.14
r = float (input ("Introduce el radio que quieras: "))

area = pi*r**2
longitud = 2*pi*r

print (f"Si {r} es el radio, su area es: {area:.1f} y su longitud es: {longitud:.1f}")