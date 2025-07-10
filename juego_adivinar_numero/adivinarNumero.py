# Elige algo aleatorio
import random;
# Te permite interactuar con el sistema operativo
import os;
# Sirve para manipular el tiempo
import time;


# ADIVINA EL NÚMERO
def MostrarBienvenidaAN():
    print("===============================================")
    print("  ¡Bienvenido al Juego de Adivinar el Número!  ")
    print("===============================================")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Tu objetivo es adivinarlo. Te daré pistas.")
    print("               ¡Mucha suerte!             ")
    print("")

def seleccionDificutad():
    while True:
        print("Opciones de dificultad:")
        print("1- Fácil")
        print("2- Intermedio")
        print("3- Difícil")

        try:
            eleccionDificultad = int(input("Introduce el número de la dificultad deseada: "))
        
            if eleccionDificultad == 1:
                print("Has seleccionado la dificultad Fácil (10 intentos)")
                return 10
            elif eleccionDificultad == 2:
                print("Has seleccionado la dificultad Intermedio (5 intentos)")
                return 5
            elif eleccionDificultad == 3:
                print("Has seleccionado la dificultad Difícil (3 intentos)")
                return 3
            else:
                print("La opción seleccionada no existe... Introduce una de las opciones 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")

def partidaAN():
    numeroSecreto = random.randint(1, 100)
    intentosRestantes = seleccionDificutad()

    while intentosRestantes > 0:
        try:
            numeroUsuario = int(input("¿Qué número crees que es el correcto?: "))
            if numeroUsuario == numeroSecreto:
                print("¡Correcto!, has acertado")
                break
            else:
                print("Ohhh, no es correcto... Vuelve a intentarlo")
                intentosRestantes -= 1
            if numeroUsuario < numeroSecreto:
                print(f"El número es mayor a {numeroUsuario}")
            else:
                print(f"El número es menor a {numeroUsuario}")
            print(f"Te quedan {intentosRestantes} intentos.")
            if intentosRestantes == 0:
                print(f"¡Oh no! Te quedaste sin intentos. El número secreto era {numeroSecreto}.")

        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")


# AHORCADO CLÁSICO

def obtenerPalabra():
    # Lista de palabras posibles
    palabras = [
    "leon", "tigre", "elefante", "jirafa", "canguro",
    "delfin", "aguila", "serpiente", "tortuga", "rinoceronte",
    "hipopotamo", "zorro", "buho", "camaleon", "lobo",
    "oso", "cebra", "pulpo", "pinguino", "murcielago", 
    "gato", "perro", "leopardo", "ballena", "siluro"
]
    return random.choice(palabras)

def mostrarProgreso(palabra, letrasAdivinadas):
    # Muestra la palabra con letras adivinadas y guiones bajos
    progreso = [letra if letra in letrasAdivinadas else "_" for letra in palabra]
    print("Palabra: " + " ".join(progreso))

def jugarAhorcado():
    palabraSecreta = obtenerPalabra()
    letrasAdivinadas = set()
    intentosRestantes = 6  # Puedes ajustar la dificultad

    print("🎩 ¡Bienvenido al Ahorcado! Adivina el animal secreto.")

    while intentosRestantes > 0:
        mostrarProgreso(palabraSecreta, letrasAdivinadas)
        print(f"Letras usadas: {', '.join(sorted(letrasAdivinadas))}")
        print(f"Te quedan {intentosRestantes} intentos.")

        letra = input("Introduce una letra: ").lower()
        if len(letra) != 1 or not letra.isalpha():
            print("❗ Ingresa solo una letra válida.")
            continue
        if letra in letrasAdivinadas:
            print("🔁 Ya has usado esa letra. Prueba con otra.")
            continue

        letrasAdivinadas.add(letra)

        if letra in palabraSecreta:
            print("✅ ¡Bien! Has acertado una letra.")
        else:
            print("❌ Esa letra no está en la palabra.")
            intentosRestantes -= 1

        # Verificar si el jugador ha ganado
        if all(letra in letrasAdivinadas for letra in palabraSecreta.lower()):
            mostrarProgreso(palabraSecreta, letrasAdivinadas)
            print("🎉 ¡Felicidades! Has adivinado la palabra correctamente.")
            break

    else:
        print(f"💀 Has perdido. La palabra era: {palabraSecreta}")


# JUEGO OPERACIONES MATEMÁTICAS

def seleccionarDificultad():
    print("Selecciona nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")

    while True:
        opcion = input("Elige la dificultad: ")
        if opcion in ("1", "2", "3"):
            return int(opcion)
        print("❗ Opción no válida.")

def generarPregunta(dificultad):
    if dificultad == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operaciones = ["+", "-"]
    elif dificultad == 2:
        num1 = random.randint(10, 50)
        num2 = random.randint(10, 50)
        operaciones = ["+", "-", "*"]
    else:
        num1 = random.randint(20, 100)
        num2 = random.randint(1, 20)
        operaciones = ["+", "-", "*", "/"]

    operacion = random.choice(operaciones)
    pregunta = f"{num1} {operacion} {num2}"
    if operacion == "/":
        respuesta = round(num1 / num2, 2)
    else:
        respuesta = eval(pregunta)
    return pregunta, respuesta

def jugarRetoMatematico():
    dificultad = seleccionarDificultad()
    puntaje = 0
    totalPreguntas = 5

    print("🧮 ¡Comienza el Reto Matemático!")

    for i in range(totalPreguntas):
        pregunta, respuesta = generarPregunta(dificultad)
        print(f"Pregunta {i + 1}: ¿Cuánto es {pregunta}?")

        try:
            respuesta_usuario = float(input("Tu respuesta: "))
        except ValueError:
            print("❗ Entrada no válida. Se contará como incorrecta.")
            continue

        if abs(respuesta_usuario - respuesta) < 0.01:
            print("✅ ¡Correcto!")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta era {respuesta}")

    print(f"🎯 Resultado final: {puntaje}/{totalPreguntas} aciertos")
    if puntaje == totalPreguntas:
        print("🏆 ¡Perfecto! ¡Eres una máquina de calcular!")
    elif puntaje >= 3:
        print("👏 ¡Bien hecho! Sigue practicando.")
    else:
        print("📘 No te rindas. ¡La práctica hace al maestro!")


# JUEGO DE SIMON DICE

def mostrarSecuenciaSimon(secuencia):
    for color in secuencia:
        print(f"Simón dice: {color}")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla

def obtenerRespuestaSimon(longitud):
    respuesta = []
    for i in range(longitud):
        color = input(f"Ingrese el color #{i + 1}: ").lower()
        respuesta.append(color)
    return respuesta

def jugarSimonDice():
    colores = ['rojo', 'azul', 'verde', 'amarillo']
    secuencia = []
    ronda = 1

    print("\n🔴🟡🟢🔵 ¡Bienvenido a Simón Dice!")
    print("Repite la secuencia de colores.")

    while True:
        print(f"\n--- Ronda {ronda} ---")
        secuencia.append(random.choice(colores))
        mostrarSecuenciaSimon(secuencia)
        respuesta = obtenerRespuestaSimon(len(secuencia))

        if respuesta != secuencia:
            print("❌ ¡Fallaste! Fin del juego.")
            print(f"Llegaste a la ronda {ronda}")
            break
        else:
            print("✅ ¡Correcto!")
            ronda += 1
            time.sleep(1)




def mostrarMenu():
    while True:
        # Limpia la pantalla de la terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════════════════╗")
        print("║             MENÚ DE MINIJUEGOS EN PYTHON           ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║  1. Adivina el Número                              ║")
        print("║  2. Ahorcado Clásico                               ║")
        print("║  3. Reto Matemático                                ║")
        print("║  4. Juego de Memoria                               ║")
        print("║  5. Simón Dice                                     ║")
        print("║  6. Piedra, Papel o Tijera                         ║")
        print("║  7. Número Mayor o Menor                           ║")
        print("║  8. Trivia de Cultura General                      ║")
        print("║  0. Salir del juego                                ║")
        print("╚════════════════════════════════════════════════════╝")


        opcion = input("👉 Introduce el número del juego que deseas jugar: ")

        if opcion == "1":
            MostrarBienvenidaAN()
            partidaAN()
            input("Pulsa Enter para volver al menú... ")
        elif opcion == "2":
            jugarAhorcado()
            input("Pulsa Enter para volver al menú... ")
        elif opcion == "3":
            jugarRetoMatematico()
            input("Pulsa Enter para volver al menú... ")
        elif opcion == "4":
            
            input("Pulsa Enter para volver al menú... ")
        elif opcion == "5":
            jugarSimonDice()
            input("Pulsa Enter para volver al menú... ")

        elif opcion == "0":
            print("\n¡Gracias por jugar! 👋")
            break
        else:
            print("\nEsa opción todavía no está disponible. ¡Muy pronto! 🚧")
            # Pausa la ejecución del programa por la cantidad de segundos especificada
            time.sleep(2)

if __name__ == "__main__":
    mostrarMenu()