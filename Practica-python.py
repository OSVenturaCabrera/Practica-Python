<<<<<<< HEAD
# ============================= Starlyn Academy =============================
# Curso: Introducción a la Programación con Python  
# Ejercicios básicos de Python
=======
# =============================
# Ejercicios básicos de Python Emil
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
# --------------------------------
<<<<<<< HEAD
nombre = input("Ingresa tu nombre: ")  # Guardamos el nombre escrito por el usuario
print("Hola " + nombre)  # Mostramos un saludo con el nombre
numero = int (10)
prom = float (2)
caract = str ("30")
=======
nombre = input ("Whats is your name ?")
print ("Hello " + nombre)
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------
<<<<<<< HEAD
edad = input("Ingresa tu edad: ")  # Guardamos la edad como texto
print("Tienes " + edad + " años")  # Mostramos la edad concatenada en una frase
numero = int (10)
prom = float (2)
caract = str ("30")
=======
edad = input ("How old are you ?")
print ("Youre are " + edad + " Years old ")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------
<<<<<<< HEAD
nombre = input("Ingresa tu nombre: ")  # Se pide el nombre
edad = input("Ingresa tu edad: ")  # Se pide la edad
print("Hola " + nombre + ", tienes " + edad + " años")  # Se imprimen nombre y edad en un solo mensaje
numero = int (10)
prom = float (2)
caract = str ("30")

=======
print ("Estas en el ejercicio 3: Nombre y la Edad.")
Nombre = input ("Cual es tu nombre ? ")
Edad = input ("Cual es tu edad ? ")
print ("Hola " + nombre + " tienes " + edad + " de edad ")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86
# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------
<<<<<<< HEAD
n1 = int(input("Ingresa el primer número: "))  # Se pide el primer número y se convierte a entero
n2 = int(input("Ingresa el segundo número: "))  # Se pide el segundo número y se convierte a entero
print("La suma es:", n1 + n2)  # Se suma n1 y n2, y se muestra el resultado
numero = int (10)
prom = float (2)
caract = str ("30")

# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------
n1 = int(input("Ingresa el primer número: "))  # Primer número entero
n2 = int(input("Ingresa el segundo número: "))  # Segundo número entero
print("La multiplicación es:", n1 * n2)  # Se multiplica n1 por n2
numero = int (10)
prom = float (2)
caract = str ("30")

# --------------------------------
# Ejercicio 6: Resta
# --------------------------------
n1 = int(input("Ingresa el primer número: "))  # Primer número entero
n2 = int(input("Ingresa el segundo número: "))  # Segundo número entero
print("La resta es:", n1 - n2)  # Se resta n2 a n1
numero = int (10)
prom = float (2)
caract = str ("30")

=======
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
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86
# --------------------------------
# Ejercicio 7: Concatenación de cadenas
print ("EJERCICIO 7")
cadena1 = input ("Primera palabra: ")
cadena2 = input ("segunda palabra: ")
print (f"La concatetacion es: {cadena1} { cadena2}")
# --------------------------------
texto1 = input("Escribe la primera palabra: ")  # Se pide un primer texto
texto2 = input("Escribe la segunda palabra: ")  # Se pide un segundo texto
print("Concatenación:", texto1 + " " + texto2)  # Se concatenan los dos textos con un espacio en medio
numero = int (10)
prom = float (2)
caract = str ("30")

# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------
<<<<<<< HEAD
texto = input("Escribe un texto: ")  # Se pide un texto
veces = int(input("¿Cuántas veces quieres repetirlo?: "))  # Se pide cuántas veces repetirlo
print((texto + " ") * veces)  # Se repite el texto con un espacio al final, la cantidad indicada
numero = int (10)
prom = float (2)
caract = str ("30")
=======
print ("Ejercicio 8 REPETIR TEXTO")
tex1 = input ("Introduce el texto a repetir:")
veces = int ( input ( "Cuantas veces lo repetiras ?: "))
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

for i in range (veces): #Siempre necesitara un numero entero.
 print (tex1) #Mi ultimo ejercicio por la noche de hoy.
# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------
<<<<<<< HEAD
base = float(input("Ingresa la base del rectángulo: "))  # Se pide la base (número decimal)
altura = float(input("Ingresa la altura del rectángulo: "))  # Se pide la altura (número decimal)
print("Área del rectángulo:", base * altura)  # Fórmula: base * altura
numero = int (10)
prom = float (2)
caract = str ("30")
=======
print ("Ejercicio 9: Area de un rectangulo") #Tuve que hacerla de nuevo porque la confundi con triangulo
lado = float(input("Introduce la medida del lado: "))
base = float(input("Introduce la medida de la base: "))
area = lado * base 

print (f"El area del rectangulo es: {area}")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------
<<<<<<< HEAD
base = float(input("Ingresa la base del triángulo: "))  # Base del triángulo
altura = float(input("Ingresa la altura del triángulo: "))  # Altura del triángulo
print("Área del triángulo:", (base * altura) / 2)  # Fórmula: (base * altura) / 2
numero = int (10)
prom = float (2)
caract = str ("30")
=======
print ("Ejercicio 9: area de un triangulo")
base = float( input("Introduce la medida de la base:"))
altura = float( input("Introduce la medida de la altura:"))
area = base * altura /2
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

print (f"El area es: {area}")
# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------
<<<<<<< HEAD
metros = float(input("Ingresa la cantidad en metros: "))  # Se pide la cantidad en metros
print("Equivalente en centímetros:", metros * 100)  # Se multiplica por 100 (1 m = 100 cm)g
=======
print ("Ejercicio 11: metros a centimetros: ") #Un metro son 100 centimetros
metros = float ( input ("Introduce la cantidad de metros a convertir: "))
centimetros = metros * 100
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

print (f"{metros} Metro es el equivalente a {centimetros} centimetros: ")
# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------
<<<<<<< HEAD
dolares = float(input("Ingresa la cantidad en dólares: "))  # Se pide la cantidad en dólares
tasa = 58  # Definimos la tasa de cambio: 1 dólar = 58 pesos dominicanos
print("Equivalente en pesos dominicanos:", dolares * tasa)  # Se multiplica dólares por t
=======
print ("Ejercicio 12: Convertir dolares a peso")
dolar = float(input("Que cantidad de dolar quieres convertir ?: "))
peso = dolar * 58
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

print (f"{dolar} Son {peso} Dominicano")
# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------
<<<<<<< HEAD
nombre = input("Ingresa tu nombre: ")  # Se pide el nombre
hora = input("¿Qué hora del día es (mañana, tarde, noche)?: ")  # Se pide el momento del día
print("¡Buenas " + hora + ", " + nombre + "!")  # Se imprime un saludo personalizado
# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------
numero = int(input("Ingresa un número: "))  # Se pide un número entero
print("El cuadrado es:", numero ** 2)  # Se eleva al cuadrado usando **
=======
print ("Ejercicio 13: Saludo personalizado")
Nombre = input ("Cual es tu nombre ?")
print ("Hola " + Nombre + " Que Dios te bendiga")
# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------
print ("Ejercico 14: numero al cuadrado")
num1 = int (input("Introduce el numero: "))
num1 = num1 * num1
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

print (f"El resultado es {num1}")
# --------------------------------
# Ejercicio 15: Promedio de tres números
# --------------------------------
<<<<<<< HEAD
n1 = float(input("Ingresa el primer número: "))  # Primer número
n2 = float(input("Ingresa el segundo número: "))  # Segundo número
n3 = float(input("Ingresa el tercer número: "))  # Tercer número
print("El promedio es:", (n1 + n2 + n3) / 3)  # Fórmula: suma de los 3 dividido entre 3
=======
print ("Ejercicio 15: Promedio de 3 numeros")
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
num3 = float(input("Introduce el tercer numero: "))
promedio = (num1 + num2 + num3)/3
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

print (f"El promedio es {promedio}")
# --------------------------------
# Ejercicio 16: Perímetro de un cuadrado
# --------------------------------
<<<<<<< HEAD
lado = float(input("Ingresa la medida de un lado del cuadrado: "))  # Longitud de un lado
print("Perímetro del cuadrado:", lado * 4)  # Fórmula: lado * 4
=======
print("Ejercicio 16: perimetro cuadrado")
lado = float(input("Introduce la longitud de un lado del cuadrado: "))
perimetro = 4 * lado

print(f"El perímetro del cuadrado es: {perimetro}")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 17: Conversor de temperatura
# Celsius a Fahrenheit
# Fórmula: F = C * 9/5 + 32
# --------------------------------
<<<<<<< HEAD
celsius = float(input("Ingresa la temperatura en °C: "))  # Se pide la temperatura en Celsius
fahrenheit = celsius * 9/5 + 32  # Se aplica la fórmula de conversión
print("Equivalente en °F:", fahrenheit)  # Se muestra el resultado en Fahrenheit
=======
print("Ejercicio 17: Conversor de temperatura")
celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = celsius * 9/5 + 32

print(f"{celsius}°C equivalen a {fahrenheit}°F")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 18: Calcular sueldo semanal
# --------------------------------
<<<<<<< HEAD
horas = float(input("Horas trabajadas en la semana: "))  # Se pide la cantidad de horas trabajadas
pago_hora = float(input("Pago por hora: "))  # Se pide el pago por hora
print("Sueldo semanal:", horas * pago_hora)  # Se multiplica horas por pago_hora
=======
print("Ejercicio 18: Calcular sueldo semanal")
hora = float(input("Introduce las horas trabajadas en la semana: "))
pago = float(input("Introduce el pago por hora: "))

sueldo_por_semana = hora * pago

print(f"El sueldo semanal es: {sueldo_por_semana}")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 19: Suma de edades
# --------------------------------
<<<<<<< HEAD
edad1 = int(input("Edad de la primera persona: "))  # Se pide la primera edad
edad2 = int(input("Edad de la segunda persona: "))  # Se pide la segunda edad
print("La suma de edades es:", edad1 + edad2)  # Se suman ambas edades
=======
print("Ejercicio 19: Suma de edades")
edad1 = int(input("Introduce la primera edad: "))
edad2 = int(input("Introduce la segunda edad: "))
Ambas_edades = edad1 + edad2

print(f"La suma de las edades es: {Ambas_edades}")
>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86

# --------------------------------
# Ejercicio 20: Mini encuesta
# --------------------------------
<<<<<<< HEAD
nombre = input("¿Cómo te llamas?: ")  # Se pide el nombre
edad = input("¿Cuántos años tienes?: ")  # Se pide la edad
color = input("¿Cuál es tu color favorito?: ")  # Se pide el color favorito
print("Resumen de encuesta -> Nombre:", nombre, "| Edad:", edad, "| Color favorito:", color)  # Se muestra el resumen
=======
print("Ejercicio 20: Mini encuesta")

marca = input("¿Que carro te gusta? ")
modelo = input("Que modelo ?")
color_favorito = input("¿Cuál es tu color favorito? ")

marca = "bmw"
if marca == "bmw":
 print ("ESO E DE HOMBRE")
print(f"Modelo: {modelo}")
print (f"Color favorito: {color_favorito}") #PA CURAME



>>>>>>> f2c606399d93250b4490e9a6740544ca69061c86
