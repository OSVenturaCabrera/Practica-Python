# =============================
# Ejercicios básicos de Python Emil
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
# --------------------------------
nombre = input ("Whats is your name ?")
print ("Hello " + nombre)

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------
edad = input ("How old are you ?")
print ("Youre are " + edad + " Years old ")

# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------
print ("Estas en el ejercicio 3: Nombre y la Edad.")
Nombre = input ("Cual es tu nombre ? ")
Edad = input ("Cual es tu edad ? ")
print ("Hola " + nombre + " tienes " + edad + " de edad ")
# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------
print ("SUMA DE DOS NUMEROS")
num1 = int (input ( "Introduce el primer numero: "))
num2 = int ( input ( "Introduce el segundo numero: "))
suma = num1 + num2
print ( "La suma es:" + str (suma))
# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------
print ("EJERCICIO DE MULTIPLICACION")
num1 = int (input ("Introduce el primer numero: "))
num2 = int (input ("Introduce el segundo numero: "))
Multiplicacion = num1 * num2
print (f"La multiplicacion es:  {Multiplicacion}") # vaina q me dio brega eta degracia
# --------------------------------
# Ejercicio 6: Resta
# --------------------------------
print("EJERCICIO DE RESTA")
num1 = int ( input ( "Introduce el primer numero: "))
num2 = int ( input ( "Introduce el segundo numero: "))
resta = num1 - num2
print (f"La resta es: {resta}") 
# --------------------------------
# Ejercicio 7: Concatenación de cadenas
print ("EJERCICIO 7")
cadena1 = input ("Primera palabra: ")
cadena2 = input ("segunda palabra: ")
print (f"La concatetacion es: {cadena1} { cadena2}")
# --------------------------------

# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------
print ("Ejercicio 8 REPETIR TEXTO")
tex1 = input ("Introduce el texto a repetir:")
veces = int ( input ( "Cuantas veces lo repetiras ?: "))

for i in range (veces): #Siempre necesitara un numero entero.
 print (tex1) #Mi ultimo ejercicio por la noche de hoy.
# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------
print ("Ejercicio 9: Area de un rectangulo") #Tuve que hacerla de nuevo porque la confundi con triangulo
lado = float(input("Introduce la medida del lado: "))
base = float(input("Introduce la medida de la base: "))
area = lado * base 

print (f"El area del rectangulo es: {area}")

# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------
print ("Ejercicio 9: area de un triangulo")
base = float( input("Introduce la medida de la base:"))
altura = float( input("Introduce la medida de la altura:"))
area = base * altura /2

print (f"El area es: {area}")
# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------
print ("Ejercicio 11: metros a centimetros: ") #Un metro son 100 centimetros
metros = float ( input ("Introduce la cantidad de metros a convertir: "))
centimetros = metros * 100

print (f"{metros} Metro es el equivalente a {centimetros} centimetros: ")
# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------
print ("Ejercicio 12: Convertir dolares a peso")
dolar = float(input("Que cantidad de dolar quieres convertir ?: "))
peso = dolar * 58

print (f"{dolar} Son {peso} Dominicano")
# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------
print ("Ejercicio 13: Saludo personalizado")
Nombre = input ("Cual es tu nombre ?")
print ("Hola " + Nombre + " Que Dios te bendiga")
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
