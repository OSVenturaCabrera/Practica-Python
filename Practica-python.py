# ============================= Starlyn Academy =============================
# Curso: Introducción a la Programación con Python  
# Ejercicios básicos de Python
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
# --------------------------------
nombre = input("Ingresa tu nombre: ")  # Guardamos el nombre escrito por el usuario
print("Hola " + nombre)  # Mostramos un saludo con el nombre

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------
edad = input("Ingresa tu edad: ")  # Guardamos la edad como texto
print("Tienes " + edad + " años")  # Mostramos la edad concatenada en una frase

# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------
nombre = input("Ingresa tu nombre: ")  # Se pide el nombre
edad = input("Ingresa tu edad: ")  # Se pide la edad
print("Hola " + nombre + ", tienes " + edad + " años")  # Se imprimen nombre y edad en un solo mensaje

# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------
n1 = int(input("Ingresa el primer número: "))  # Se pide el primer número y se convierte a entero
n2 = int(input("Ingresa el segundo número: "))  # Se pide el segundo número y se convierte a entero
print("La suma es:", n1 + n2)  # Se suma n1 y n2, y se muestra el resultado

# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------
n1 = int(input("Ingresa el primer número: "))  # Primer número entero
n2 = int(input("Ingresa el segundo número: "))  # Segundo número entero
print("La multiplicación es:", n1 * n2)  # Se multiplica n1 por n2

# --------------------------------
# Ejercicio 6: Resta
# --------------------------------
n1 = int(input("Ingresa el primer número: "))  # Primer número entero
n2 = int(input("Ingresa el segundo número: "))  # Segundo número entero
print("La resta es:", n1 - n2)  # Se resta n2 a n1

# --------------------------------
# Ejercicio 7: Concatenación de cadenas
# --------------------------------
texto1 = input("Escribe la primera palabra: ")  # Se pide un primer texto
texto2 = input("Escribe la segunda palabra: ")  # Se pide un segundo texto
print("Concatenación:", texto1 + " " + texto2)  # Se concatenan los dos textos con un espacio en medio

# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------
texto = input("Escribe un texto: ")  # Se pide un texto
veces = int(input("¿Cuántas veces quieres repetirlo?: "))  # Se pide cuántas veces repetirlo
print((texto + " ") * veces)  # Se repite el texto con un espacio al final, la cantidad indicada

# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------
base = float(input("Ingresa la base del rectángulo: "))  # Se pide la base (número decimal)
altura = float(input("Ingresa la altura del rectángulo: "))  # Se pide la altura (número decimal)
print("Área del rectángulo:", base * altura)  # Fórmula: base * altura

# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------
base = float(input("Ingresa la base del triángulo: "))  # Base del triángulo
altura = float(input("Ingresa la altura del triángulo: "))  # Altura del triángulo
print("Área del triángulo:", (base * altura) / 2)  # Fórmula: (base * altura) / 2

# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------
metros = float(input("Ingresa la cantidad en metros: "))  # Se pide la cantidad en metros
print("Equivalente en centímetros:", metros * 100)  # Se multiplica por 100 (1 m = 100 cm)g

# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------
dolares = float(input("Ingresa la cantidad en dólares: "))  # Se pide la cantidad en dólares
tasa = 58  # Definimos la tasa de cambio: 1 dólar = 58 pesos dominicanos
print("Equivalente en pesos dominicanos:", dolares * tasa)  # Se multiplica dólares por t

# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------
nombre = input("Ingresa tu nombre: ")  # Se pide el nombre
hora = input("¿Qué hora del día es (mañana, tarde, noche)?: ")  # Se pide el momento del día
print("¡Buenas " + hora + ", " + nombre + "!")  # Se imprime un saludo personalizado
# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------
numero = int(input("Ingresa un número: "))  # Se pide un número entero
print("El cuadrado es:", numero ** 2)  # Se eleva al cuadrado usando **

# --------------------------------
# Ejercicio 15: Promedio de tres números
# --------------------------------

# --------------------------------
# Ejercicio 16: Perímetro de un cuadrado
# --------------------------------

# --------------------------------
# Ejercicio 17: Conversor de temperatura
# Celsius a Fahrenheit
# Fórmula: F = C * 9/5 + 32
# --------------------------------

# --------------------------------
# Ejercicio 18: Calcular sueldo semanal
# --------------------------------

# --------------------------------
# Ejercicio 19: Suma de edades
# --------------------------------

# --------------------------------
# Ejercicio 20: Mini encuesta
# --------------------------------
