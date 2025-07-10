#EJERCICIO 1

# Diccionario inicial
producto = {
    "nombre": "Teclado",
    "precio": 25.50,
    "stock": 15
}

# 1. Mostrar todos los valores
print("Valores del diccionario:")
for valor in producto.values():
    print(valor)

# 2. Aumentar el stock en 10 unidades
producto["stock"] += 10

# 3. Agregar nueva clave "categoria"
producto["categoria"] = "Periféricos"

# 4. Imprimir claves y valores
print("\nDatos actualizados del producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

#EJERCICIO 2

# Diccionario inicial
empleados = {
    "emp01": {"nombre": "Laura", "salario": 2500, "cargo": "Diseñadora"},
    "emp02": {"nombre": "Carlos", "salario": 3000, "cargo": "Programador"},
    "emp03": {"nombre": "Elena", "salario": 2800, "cargo": "Tester"}
}

# 1. Imprimir todos los nombres
print("Nombres de los empleados:")
for datos in empleados.values():
    print(datos["nombre"])

# 2. Obtener el cargo de emp02 usando .get()
cargo_emp02 = empleados.get("emp02", {}).get("cargo")
print(f"\nCargo de emp02: {cargo_emp02}")

# 3. Aumentar el salario de emp03 en 200
empleados["emp03"]["salario"] += 200

# 4. Eliminar emp01 usando .pop()
empleado_eliminado = empleados.pop("emp01", None)

# 5. Mostrar diccionario actualizado
print("\nEmpleados actualizados:")
for emp_id, datos in empleados.items():
    print(f"{emp_id}: {datos}")

#EJERCICIO 3

# Diccionario inicial
estudiantes = {
    "A001": {"nombre": "Ana", "notas": [7, 8.5, 9]},
    "A002": {"nombre": "Luis", "notas": [6.5, 7, 8]},
    "A003": {"nombre": "Pedro", "notas": [8, 9, 10]}
}

# 1. Calcular promedio y agregar clave "promedio"
for datos in estudiantes.values():
    promedio = sum(datos["notas"]) / len(datos["notas"])
    datos["promedio"] = round(promedio, 2)

# 2. Mostrar estudiantes con promedio >= 8
print("Estudiantes con promedio mayor o igual a 8:")
for datos in estudiantes.values():
    if datos["promedio"] >= 8:
        print(f"{datos['nombre']} - Promedio: {datos['promedio']}")

# 3. Eliminar estudiantes con promedio < 7
claves_a_eliminar = [clave for clave, datos in estudiantes.items() if datos["promedio"] < 7]
for clave in claves_a_eliminar:
    estudiantes.pop(clave)

# 4. Agregar nuevo estudiante por input
nombre_nuevo = input("Introduce el nombre del nuevo estudiante: ")
notas_nuevas = []
for i in range(3):
    nota = float(input(f"Ingrese nota {i+1}: "))
    notas_nuevas.append(nota)
promedio_nuevo = round(sum(notas_nuevas) / 3, 2)

# Añadir al diccionario con ID A004
estudiantes["A004"] = {"nombre": nombre_nuevo, "notas": notas_nuevas, "promedio": promedio_nuevo}

# 5. Mostrar diccionario final con nombres y promedios
print("\nResumen final de estudiantes:")
for datos in estudiantes.values():
    print(f"{datos['nombre']} - Promedio: {datos['promedio']}")
