#HACE UN TRIÁNGULO CON ASTERISCOS CON LA ALTURA QUE SE INTRODUCE
altura = int(input("Introduce la altura del triángulo: "))

for num in range(1, altura):
    asterisco = "*" *(2 * num -1)
    multiplicacion = asterisco  * altura
print(multiplicacion)