# =============================starlyn Resivido 1=============================
# EJERCICIO 1: Lista de números
# =============================
# Pedir al usuario que ingrese 5 números y guardarlos en una lista.
# Después deberás encontrar:
# - El número mayor
# - El número menor
# - El promedio de los números

numeros = []  # lista vacía para guardar los números

for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

mayor = max(numeros)
menor = min(numeros)
promedio = sum (numeros) / len(numeros)

print("resurtados: ")
print('numeros ingresados: ', numeros)
print('numero mayor: ', mayor)
print('numero menor: ', menor)
print('promedio de los numeros: ',promedio )

# Aquí escribe la lógica para mayor, menor y promedio.


# ===================================
# EJERCICIO 2: Diccionario de estudiantes
# ===================================
# El usuario ingresa el nombre de varios estudiantes con sus calificaciones.
# Guardar esos datos en un diccionario.
# Luego deberás mostrar:
# - Todos los estudiantes con sus calificaciones
# - El promedio de las calificaciones
# - El estudiante con la nota más alta

estudiantes = {}  # diccionario vacío

cantidad = int(input("¿Cuántos estudiantes desea registrar? "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la calificación de {nombre}: "))
    estudiantes[nombre] = nota

# Mostrar estudiantes con sus notas
print("LISTA DE ESTUDIANTES")
for nombre, nota in estudiantes.items():
    print(f"{nombre}: {nota}")

# Promedio
promedio_notas = sum(estudiantes.values()) / len(estudiantes)

# Estudiante con la nota más alta
mejor_estudiante = max(estudiantes, key=estudiantes.get)

print("RESULTADOS EJERCICIO 2")
print("Promedio de calificaciones:", promedio_notas)
print("Mejor estudiante:", mejor_estudiante, "con nota", estudiantes[mejor_estudiante])


# Aquí escribe la lógica para mostrar los datos y calcular lo pedido.

#starlyn
# ===================================
# EJERCICIO 3: Inventario con diccionarios y listas
# ===================================
# Crear un diccionario de productos donde:
# - La clave sea el nombre del producto
# - El valor sea una lista con [precio, cantidad]
# Al final deberás mostrar:
# - El inventario completo
# - El valor total del inventario
# - El producto más costoso en total (precio * cantidad)

productos = {}

n = int(input("¿Cuántos productos desea ingresar? "))

for i in range(n):
    nombre = input(f"Nombre del producto {i+1}: ")
    precio = float(input(f"Precio de {nombre}: "))
    cantidad = int(input(f"Cantidad de {nombre}: "))
    productos[nombre] = [precio, cantidad]

# Mostrar inventario completo
print("INVENTARIO COMPLETO")
for nombre, datos in productos.items():
    print(f"{nombre} -> Precio: {datos[0]}, Cantidad: {datos[1]}")

# Calcular valor total del inventario
valor_total = sum(precio * cantidad for precio, cantidad in productos.values())

# Producto más costoso en total
producto_costoso = max(productos, key=lambda x: productos[x][0] * productos[x][1])
valor_costoso = productos[producto_costoso][0] * productos[producto_costoso][1]

print("RESULTADOS EJERCICIO 3")
print("Valor total del inventario:", valor_total)
print("Producto más costoso:", producto_costoso, "con valor total de", valor_costoso)

# Aquí escribe la lógica para recorrer el diccionario y calcular lo pedido.
