# ============================= Israel Ulloa Estevez =============================

import os
os.system("cls")

# EJERCICIO 1: Lista de números
# =============================
# Pedir al usuario que ingrese 5 números y guardarlos en una lista.
# Después deberás encontrar:
# - El número mayor
# - El número menor
# - El promedio de los números

# numeros = []  # lista vacía para guardar los números

# for i in range(5):
#     num = int(input(f"Ingrese el número {i+1}: "))
#     numeros.append(num)

# Aquí escribe la lógica para mayor, menor y promedio.

# numeros_ordenados = sorted(numeros) # ordeno la lista de menor a mayor.
# numero_mayor = numeros_ordenados[-1] # 'indice -1' para mostrar el ultimo numero que sera el mayor.
# numero_menor = numeros_ordenados[0] # 'indice 0' para mostrar el primer numero que sera el menor.
# # sumamos primero todos los nuemros y luego lo 
# # dividimos por la cantidad de nuemros en la lista.
# Promedio = ((sum(numeros)) / len(numeros)) 

# resultados:
# logica = (numeros, numeros_ordenados, numero_mayor, numero_menor, Promedio)
# for i in logica:
#     print(i)

# ===================================
# EJERCICIO 2: Diccionario de estudiantes
# ===================================
# El usuario ingresa el nombre de varios estudiantes con sus calificaciones.
# Guardar esos datos en un diccionario.
# Luego deberás mostrar:
# - Todos los estudiantes con sus calificaciones
# - El promedio de las calificaciones
# - El estudiante con la nota más alta

# estudiantes = {}  # diccionario vacío

# cantidad = int(input("¿Cuántos estudiantes desea registrar? "))

# for i in range(cantidad):
#     nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
#     nota = float(input(f"Ingrese la calificación de {nombre}: "))
#     estudiantes[nombre] = nota

# # Aquí escribe la lógica para mostrar los datos y calcular lo pedido.

# # Mostrando a 'Todos los estudiantes con sus calificaciones' 
# os.system("cls")
# for llave, valor in estudiantes.items(): # descubri que el 'items' es para ambos valores
#     print(f"\n- Estudiante: {llave}, Calificacion: {valor}")

# # Mostrando el 'El promedio de las calificaciones'
# promedio = round((sum(estudiantes.values()) / len(estudiantes)), 2)
# print('\nEl promedio de las notas es igual a : ' , promedio , "%") # muestro el promedio.

# # Mostrando el 'El estudiante con la nota más alta'
# # hice dos variables en este caso una para el 'nombre' y para el 'valor'.
# mayor_nota = -1
# mejor_estudiante = ""
# # hice un bucle para buscar la nota mas alta:
# for nombre, nota in estudiantes.items():
#     if nota > mayor_nota:   # si encontramos una nota más grande
#         mayor_nota = nota
#         mejor_estudiante = nombre
# print("\nEl estudiante con mejor nota fue :", mejor_estudiante, "con nota", mayor_nota)


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
    os.system("cls")
    nombre = input(f"\n- Nombre del producto {i+1}: ")
    precio = float(input(f"- Precio de {nombre}: $"))
    cantidad = int(input(f"- Cantidad de {nombre}: "))
    productos[nombre] = [precio, cantidad]

# Aquí escribe la lógica para recorrer el diccionario y calcular lo pedido.

# mostrando el 'El inventario completo':
for producto, info in productos.items(): # desempaco la clave y el valor del diccionario de datos:
    precios, cantidad = info # desempaco nuevamente pero para los "precios y la cantidad" de los productos.
    print(f"\nProducto: {producto}, \nPrecio: ${precios}, Cantidad: {cantidad}")

# mostrando el 'El valor total del inventario':
valor = 0
for info in productos.values(): # tomo solo los valores de 'precio y cantidad' de 'productos'
    precio = info[0] # hago que precio sea igual al 'precio' == info[0]
    cantidad = info[1] # hago lo mismo con la cantidad sea igual al 'cantidad' == info[1]
    valor += precio * cantidad # multiplico y sumo la cantidad al valor del invenntario.
print(f"El Inventario es igual a : ${valor}")


# mostrando el 'El producto más costoso en total (precio * cantidad)':
Producto_costoso = ""
Precio_costoso = 0
for producto, info in productos.items():
    precios = info[0] # tomo los precios x
    cantidades = info[1] # tomo las cantidades x
    precio_total = precios * cantidades # multiplico la cantidad y el precio y los guardo en una variable
    if precio_total > Precio_costoso:
        Producto_costoso = producto # asigno el nombre de dicho producto
        Precio_costoso = precio_total # asigno el precio a dicha variable
    else:
        Producto_costoso = Producto_costoso # sino mantengo dicho nombre
        Precio_costoso = Precio_costoso # igualmente para el producto que se mantendra igual
# muestro el precio x la cantidad de productos totales:
print(f"El producto mas costoso fue: {Producto_costoso} y su valor es unos ${Precio_costoso}")
