#Control de errores de posibles datos no válidos
try:
    #Variable donde se almacena el dato introducido por usuario
    nota = int(input("Introduce tu nota entre 0-100: "))
except ValueError: print("Error: El dato tiene que ser un número entero...")

if nota < 50:
    print("Tu nota es un: Suspenso")
elif nota >= 50 and nota < 69:
    print("Tu nota es un: Aprobado")
elif nota >= 70 and nota < 89:
    print("Tu nota es un: Notable")
elif nota >= 90 and nota <= 100:
    print("Tu nota es un: Sobresaliente")
else:
    #Otro control de errores para que el número introducido este entre 0 y 100
    print("Error: La calificación debe estar entre 0 y 100. ")