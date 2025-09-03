# =============================
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

# Aquí escribe la lógica para mostrar los datos y calcular lo pedido.


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

productos = {}  # diccionario vacío

n = int(input("¿Cuántos productos desea ingresar? "))

for i in range(n):
    nombre = input(f"Nombre del producto {i+1}: ")
    precio = float(input(f"Precio de {nombre}: "))
    cantidad = int(input(f"Cantidad de {nombre}: "))
    productos[nombre] = [precio, cantidad]

# Aquí escribe la lógica para recorrer el diccionario y calcular lo pedido.
