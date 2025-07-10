#ADIVINA EL NUMERO ALEATORIO

import random;

num = random.randint(1, 100)

while True:
    numUsuario = int(input("Adivina el número del 1 al 100: "))
    if numUsuario != num:
        if numUsuario < num:
            print(f"Es un número mayor a {numUsuario}")
        else: 
            print(f"Es un número menor a {numUsuario}")
    else:
        print(f"Correcto, el número es {num}")
        break   