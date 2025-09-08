# =============================  ORlin  =============================
# EJERCICIO 1: Lista de números
# =============================
# Pedir al usuario que ingrese 5 números y guardarlos en una lista.
# Después deberás encontrar:
# - El número mayor
# - El número menor
# - El promedio de los números
print("EJERCICIO 1: Lista de números")
numeros = []  # lista vacía para guardar los números

for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Aquí escribe la lógica para mayor, menor y promedio.
mayor = max(numeros)
menor = min(numeros)
promedio = sum (numeros) / len(numeros)

print("resurtados: ")
print('numeros ingresados: ', numeros)
print('numero mayor: ', mayor)
print('numero menor: ', menor)
print(f'promedio de los numeros:', promedio)

# ===================================
# EJERCICIO 2: Diccionario de estudiantes
# ===================================
# El usuario ingresa el nombre de varios estudiantes con sus calificaciones.
# Guardar esos datos en un diccionario.
# Luego deberás mostrar:
# - Todos los estudiantes con sus calificaciones
# - El promedio de las calificaciones
# - El estudiante con la nota más alta

print("Ejercicio 2: Actividad de logica. Dicionario de estudiantes")
estudiantes = {}  # diccionario vacío

cantidad = int(input("¿Cuántos estudiantes desea registrar? "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingrese la calificación de {nombre}: "))
    estudiantes[nombre] = nota

# Aquí escribe la lógica para mostrar los datos y calcular lo pedido.
print("Lista de estudiante: ")
for nombres, nota in estudiantes.items():
    print(F"{nombres}: {nota}")

promedio_notas = sum(estudiantes.values()) / len(estudiantes)
print("Promedio: ", promedio_notas)

estudiante_mejor = max(estudiantes, key = estudiantes.get) 
#estudiante_mejor2 = max(estudiantes.values())

print("El mejor: ", estudiante_mejor)

# ===================================
print("EJERCICIO 3: Inventario con diccionarios y listas")
print("======================================================")
print(" Crear un diccionario de productos donde: ")
print(" - La clave sea el nombre del producto")
print(" - El valor sea una lista con [precio, cantidad]")
print(" Al final deberás mostrar:")
print(" - El inventario completo")
print(" - El valor total del inventario")
print(" - El producto más costoso en total (precio * cantidad)")
print("======================================================")
print("=====================================================")
productos = {} #vacío

n = int(input("¿Cuántos productos desea ingresar? "))

for i in range(n):
    print("=====================================================")
    nombre = input(f"Nombre del producto {i+1}: ")
    precio = float(input(f"Precio de {nombre}: "))
    cantidad = int(input(f"Cantidad de {nombre}: "))
    productos[nombre] = [precio, cantidad]
print("==================================================================")
print("===============Lista de Prodcutos====================")
for nombre, datos in productos.items():
    print(f"Producto: {nombre} Precio: {datos[0]} Cantidad: {datos[1]}")

# Calcular valor total del inventario
valor_total = sum(precio * cantidad for precio, cantidad in productos.values())

# Producto más costoso en total
producto_costoso = max(productos, key=lambda x: productos[x][0] * productos[x][1])
valor_costoso = productos[producto_costoso][0] * productos[producto_costoso][1]


print("==================================================================")
print("El valor total del inventario")
print("========================Valor=====================================")
print(f"El Valor Total es: {valor_total}")
print("===================================================================")
print("====================================================================")
print("====================================================================")
print("El producto más costosol")
print("========================Producto====================================")
print("===================================================================")
print(f"{producto_costoso}: {valor_costoso}")
print("====================================================================")
print("=================================================================")
print("========================Fin del programa=========================")
