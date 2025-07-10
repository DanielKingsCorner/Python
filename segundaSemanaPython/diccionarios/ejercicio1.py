producto = { 
    "nombre": "Teclado",
    "precio": 25.50,
    "stock": 15
}

#MUESTRA TODOS LOS VALORES DE PRODUCTO
for elemento in producto:
    print(producto[elemento])

#AUMENTA EL VALOR DE STOCK 10
producto['stock'] += 10
print(producto)

#AGREGAR UNA NUEVA CLAVE A PRODUCTO
producto['categoria'] = "Periféricos"
print(producto)

#Imprime todas las claves y valores usando un bucle
for elemento1, elemento2 in producto.items():
    print(elemento1, elemento2)