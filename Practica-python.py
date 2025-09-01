# =============================
# Ejercicios básicos de Python Israel
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
def Hola_nombre():
    """Pide y muestra el nombre del usuario"""
    print("Mostrar el Nombre del usuario:")
    # aqui pedi el nombre por la funcion 'input'
    saludo = input("Hola, como te llamas? ")
    print("Hola " + saludo) # muestro el mensaje

# --------------------------------

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------

def Edad_user():
    """Pide y muestra la edad del usuario"""
    print("Mostrar la edad del usuario:")
    # vuelvo a pedir un valor en un 'input' dentro de un 'int'
    # 'int' es para hacer la conversion de 'string a int'
    edad = int(input("Ingrese su edad: "))
    print(f"Tienes unos {edad} años de edad")

# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------

def Nombre_y_Edad():
    """Pide y muestra el nombre y la edad del usuario"""
    print("Mostrar Nombre_y_Edad:")
    # en esta parte yo reutilizo el codigo 
    # ya existente para hacer una sola funcion.
    Hola_nombre()
    Edad_user()

# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------

def Suma():
    """Pide y suma dos numeros ingresados por el usuario :)"""
    print("Suma de numeros:")
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 + num2
    print(f"resultado: {num1} + {num2} = {r}")

# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------

def Multiplicacion():
    """Pide y multiplica dos numeros ingresados por el usuario"""
    print("Multiplicacion de numeros:")
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 * num2
    print(f"resultado: {num1} x {num2} = {r}")

# --------------------------------
# Ejercicio 6: Resta
# --------------------------------

def Resta():
    """Pide y resta dos numeros ingresados por el usuario"""
    print("Resta de numeros:")
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 - num2
    print(f"resultado: {num1} - {num2} = {r}")

# --------------------------------
# Ejercicio 7: Concatenación de cadenas
# --------------------------------

def Concatenar():
    """Funcion para unir las cadenas de texto"""
    print("Concatenar texto:")
    txt1 = input("Ingresa tu primer texto: ")
    txt2 = input("Ingresa tu primer texto: ")
    c = txt1 + txt2
    print(c) # caso 1
    print(txt1 + txt2) # caso 2
    print(txt1, txt2) # caso 3
    print(f"{txt1} {txt2}") # caso 4

# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------

def Repetir_texto():
    """Repite un texto por una cantidad determinada"""
    print("Repetir texto:")
    texto = input("Ingresa tu texto a repetir: ")
    cantidad = int(input("Cuantas veces quieres repetirlo? "))
    for i in range(cantidad):
        print(i+1, "- " , texto)
    print("Se ha repetido '" , texto , "'" ,  cantidad , "veces")

# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------

def Area_rectángulo():
    """la formula del area de un rectangulo siempre sera "Base x Altura" y ya"""
    print("Area de un Rectángulo:")
    Base = float(input("Ingrese la Base de su rectángulo: "))
    Altura = float(input("Ingrese la Altura de su rectángulo: "))
    Area = Base * Altura
    print("Base:", Base)
    print("Altura:", Altura)
    print("El Area de tu Rectangulo es igual a:" , Area)

# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------

def Area_triangulo():
    """ la formula del area de un triángulo siempre sera "(Base x Altura) ÷ 2" y ya."""
    print("Area de un triángulo:")
    Base = float(input("Ingrese la Base de su rectángulo: "))
    Altura = float(input("Ingrese la Altura de su rectángulo: "))
    Area = float((Base * Altura) / 2) # hice una conversion para los decimales, en dado caso.
    print("Base:", Base)
    print("Altura:", Altura)
    print("El Area de tu Rectangulo es igual a:" , Area)


# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------

def Metros_a_centímetros():
    """Convierte Metros a Centimetros, La formula para caulcula M a C es 
    "M * 100", ya que en cada metro hay 100 centimetros."""
    print("Metros a centímetros")
    Metros = float(input("Ingrese la cantidad de metros a convertir: "))
    Centimetros = Metros * 100
    print(f"Si tenemos unos {Metros} metros, entonces hay {Centimetros} centimetros")

# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------

def dolares_a_pesos():
    """Convierte una cantidad de dolares 
    a su equivalente a pesos dominicanos."""
    print("Conversor de dólares a pesos")
    # le pongo 'int' en vez de float porque el ejericio dice '58' 
    # osea un numero entero, asi que por esa razon no uso 'float' para numeros decimales.
    dolar = int(input("Cuantos dolares tienes? : "))
    pesos = dolar * 58
    print(f"Si tienes unos {dolar} dolares")
    print(f"Entonces posees unos {pesos} pesos.")

# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------

def Saludo_personal():
    """Muestra un saludo personalizado por el propio usuario....."""
    print("Saludo personalizado")
    # aqui no se si tengo que pedir el nombre nuevamente, asi que lo interprete asi al final :V
    saludo_propio = input("Ingresa un saludo personalizado para que te lo envie: \n")
    print(saludo_propio)

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

# Multiplicacion()

# Resta()

# Concatenar()

# Repetir_texto()

# Area_rectángulo()

# dolares_a_pesos()

Saludo_personal()