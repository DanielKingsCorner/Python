empleados = { 
    "emp01": {"nombre": "Laura", "salario": 2500, "cargo": "Diseñadora"}, 
    "emp02": {"nombre": "Carlos", "salario": 3000, "cargo": "Programador"}, 
    "emp03": {"nombre": "Elena", "salario": 2800, "cargo": "Tester"} 
}

#IMPRIME TODOS LOS NOMBRES DE LOS EMPLEADOS
for persona in empleados.values():
    print(persona["nombre"])

#USANDO EL METODO .get() PARA QUE ME DIGA EL CARGO DE UN EMPLEADO EN ESPECÍFICO
print(empleados.get("emp02")["cargo"])

#USAR .update() PARA AUMENTAR EL SALARIO DE UNA KEY EN CONCRETO
empleados["emp03"].update({"salario": empleados["emp03"]["salario"] + 200})
print(empleados.get("emp03")["salario"])