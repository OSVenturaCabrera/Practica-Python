# =============================
# Ejercicios básicos de Python Israel
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
def Hola_nombre():
    # aqui pedi el nombre por la funcion 'input'
    saludo = input("Hola, como te llamas? ")
    print("Hola " + saludo) # muestro el mensaje

# --------------------------------

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------

def Edad_user():
    # vuelvo a pedir un valor en un 'input' dentro de un 'int'
    # 'int' es para hacer la conversion de 'string a int'
    edad = int(input("Ingrese su edad: "))
    print(f"Tienes unos {edad} años de edad")

# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------

def Nombre_y_Edad():
    # en esta parte yo reutilizo el codigo 
    # ya existente para hacer una sola funcion.
    Hola_nombre()
    Edad_user()

# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------

def Suma():
    print("Suma de numeros:")
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 + num2
    print(f"resultado: {num1} + {num2} = {r}")

# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------

def Multiplicacion():
    print("Multiplicacion de numeros:")
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 * num2
    print(f"resultado: {num1} + {num2} = {r}")

# --------------------------------
# Ejercicio 6: Resta
# --------------------------------

# --------------------------------
# Ejercicio 7: Concatenación de cadenas
# --------------------------------

# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------

# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------

# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------

# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------

# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------

# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------

# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------

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


# # Pruebas:
# Hola_nombre()

# Edad_user()

# # nombre y edad funcionan perfectamente como 1 :)
# Nombre_y_Edad()

# Suma()

Multiplicacion()