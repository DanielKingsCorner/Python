# #COMPOSICIÓN SECUENCIAL
# #Ejercicio 1
nombre = input("Introduce tu nombre: ")

print(f"Hola {nombre}. Encantado de conocerte")

# #Ejercicio 2
a = float(input("Introduce la longitud del lado a del rectángulo: "))
b = float(input("Introduce la longitud del lado b del rectángulo: "))
area = a * b

print(area)

# #Ejercicio 3
horas = int(input("Introduce el número de horas: "))
suma = horas * 60

print(suma)

# #COMPOSICIÓN CONDICIONAL
# #Ejercicio 1
num = int(input("Introduce un número: "))

if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} no es par")

# #Ejercicio 2
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"{num1} es el número mayor")
else:
    print(f"{num2} es el número mayor")

# #Ejercicio 3
contraseñaCorrecta = "python123"
contraseña = float(input("Introduce la contraseña: "))

if contraseñaCorrecta == contraseña:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# #Ejercicio 4
num1 = float(input("Introduce la longitud del primer lado: "))
num2 = float(input("Introduce la longitud del segundo lado: "))
num3 = float(input("Introduce la longitud del tercer lado: "))

if num1 == num2 and num2 == num3:
    print("Es un triángulo equilátero")
elif num1 == num2 or num2 == num3:
    print("Eltriángulo es isósceles")
else:
    print("El triángulo es escaleno")

# #COMPOSICIÓN ITERATIVA
#Ejercicio 1
for num in range(1, 6):
    print(num)

#Ejercicio 2
contador = 10
while contador > 0:
    print(contador)
    contador = contador - 1

# #Ejercicio 3
num = int(input("Introduzca un número para sumar: "))
suma = 0
contador = 1

while contador <= num:
    suma = suma + contador
    contador = contador + 1

print(suma)

#Ejercicio 4
mensaje = input("Introduce un mensaje: ")
contador = int(input("Introduce el número de veces que se repite el mensaje: "))


while contador >= 1:
    print(mensaje)
    contador = contador - 1

#Ejercicio 5
import random;

num = random.randint(1, 10)

while True:
    numUsuario = int(input("Adivina el número del 1 al 10: "))
    if numUsuario != num:
        if numUsuario < num:
            print(f"Es un número mayor a {numUsuario}")
        else: 
            print(f"Es un número menor a {numUsuario}")
    else:
        print(f"Correcto, el número es {num}")
        break      

#COMPOSICIÓN MODULAR
#Ejercicio 1
def saludar(nombre):
    print(f"¡Hola, {nombre}! Espero que tengas un gran día")

saludar("Daniel")

# #Ejercicio 2
def sumar(num1, num2):
    return num1 + num2

resultado = sumar(5, 3)
print(f"La suma de 5 y 3 es: {resultado}")

# #Ejercicio 3
def imprimir_n_veces(mensaje, veces):
    while veces >= 1:
        print(mensaje)
        veces = veces - 1

imprimir_n_veces("Hola", 4)

#Ejercicio 4
def es_mayor_de_edad(edad):
    return edad >= 18

edadUsuario = int(input("Introduce tu edad: "))
if es_mayor_de_edad(edadUsuario):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejercicio Integrador
#Pomedio de notas
def calcular_promedio(listaNotas):
    return sum(listaNotas) / len(listaNotas)

def obtener_calificacion_texto(promedio):
    if promedio < 5:
        return "Suspenso"
    elif 5 <= promedio < 7:
        return "Aprobado"
    elif 7 <= promedio < 9:
        return "Notable"
    else:
        return "Sobresaliente"

def main():
    try:
        materias = int(input("Ingresa el número de materias: "))
        if materias <= 0:
            raise ValueError("El número de materias tiene que ser positivo")

        lista_notas = []
        for i in range(materias):
            while True:
                try:
                    nota = float(input(f"Ingresa la calificación de la materia {i+1}: "))
                    if nota < 0 or nota > 10:
                        raise ValueError("La calificación tiene que estar entre 0 y 10")
                    lista_notas.append(nota)
                    break
                except ValueError as err:
                    print(f"Entrada inválida: {err}. Intentalo nuevamente")

        promedio = calcular_promedio(lista_notas)
        calificacion_texto = obtener_calificacion_texto(promedio)

        print(f"\nEl promedio de calificaciones es: {promedio:.2f}")
        print(f"Calificación final: {calificacion_texto}")

    except ValueError as err:
        print(f"Error: {err}")

if nombre == "main":
    main()