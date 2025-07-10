# #CONTADOR SIMPLE
contador = 1
while contador <= 10:
    print(contador)
    contador = contador + 1
    

# #SUMA ACUMULATIVA
num = int(input("Introduzca un número para sumar: "))
suma = 0

while num != 0:
    suma = suma + num
    num = (int(input("Introduzca un número para sumar: ")))
print(suma)

#VALIDACIÓN DE ENTRADA
contraseniaCorrecta = 123
contrasenia = int(input("Introduce tu contraseña (Solo están permitidos carácteres númericos): "))

while contrasenia != contraseniaCorrecta:
    contrasenia = int(input("Introduce tu contraseña (Solo están permitidos carácteres númericos): "))

print("Contraseña correcta")