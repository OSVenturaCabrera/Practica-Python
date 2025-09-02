# =============================
# Ejercicios básicos de Python ORlin
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
# --------------------------------
print("Ejercicio 1: Hola nombre")
nombre = input("¿Cuál es tu nombre? ")
print("Klk " + nombre)
# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------
print("Ejercicio 2: Edad en un mensaje")
edad = input("Cuale es tu edad para no darte una galleta")
print("Como tienes " + edad + "años, no te doy una galleta")
# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------
print("Ejercicio 3: Nombre y edad juntos")
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")  
print('hola ' + nombre + ' tienes ' + edad + ' años')
# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------
print("Ejercicio 4: Suma de dos números")
num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: ")) 
suma = num1 + num2
print("La suma es: " + str(suma))
# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------
print('Ejercicio 5: Multiplicación')
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
multi = num1 * num2
print("La multiplicacion es: " + str(multi))

# --------------------------------
# Ejercicio 6: Resta
# --------------------------------
print("Ejercicio 6: Resta")
num1 = int(input("Dame un número: "))
num2 = int(input("Dame otro número: "))     
resta = num1 - num2
print("La resta es: " + str(resta))

# --------------------------------
# Ejercicio 7: Concatenación de cadenas
# --------------------------------
print("Ejercicio 7: Concatenación de cadenas")
cadena1 = input("Dame una cadena: ")
cadena2 = input("Dame otra cadena: ") 
Contatenacion = cadena1 + cadena2
print("La concatenacion es: " + Contatenacion)
# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------
print("Ejercicio 8: Repetición de texto")
texto = input("Dame un texto: ")
veces = int(input("Cuantas veces Quieres que se repita: "))
Repe = texto * veces
print(Repe)

# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------
print("Ejercicio 9: Área de un rectángulo")
base = input("Cual es la base: ")
altu = input("Altura: ")
area =  base * altu
print("EL area es: " + str(area))
# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------
print("Ejercicio 10: Area de un triangulo")
base = int(input("Base: "))
Altura = int(input("Altura: "))
area = (base * Altura) / 2
print("El area es: " + str(area))
# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------
print("Ejercicio 11: Metros a centímetros")
metro = float(input("metros: "))
centi = metro * 100
print("Los centimetros son: " + str(centi))
# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------
print("Ejercicio 12")
dolar = float(input("Dolares: "))
peso = dolar * 58
print("son: " + str(peso))
# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------
print("Ejercicio 13: Saludo personalizado")
nombre = input("Cual es tu nombre: ")
print("Hola " + nombre + ", bienvenido al grupo de Pyhton.")
# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------
print("Ejercicio 14: Numero al cuadrado")
num = int(input("Dame un numero: "))
cuadrado = num ** 2 #Este ejercicio lo hice con el auto clompletar de VSCode
print("El numero al cuadrado es: " + str(cuadrado))
# --------------------------------
# Ejercicio 15: Promedio de tres números
# --------------------------------
print("Ejercicio 15: Promedio de tres números")
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))       
num3 = float(input("Numero 3: "))
promedio = (num1 + num2 + num3) / 3
print("El promedio es: " + str(promedio))
# --------------------------------
# Ejercicio 16: Perímetro de un cuadrado
# --------------------------------
print("Ejercicicio 16")
lado = float(input("Lado del cuadrado: "))
ORlin = lado * 4
print("El perimetro es: " + str(ORlin))
# --------------------------------
# Ejercicio 17: Conversor de temperatura
# Celsius a Fahrenheit
# Fórmula: F = C * 9/5 + 32
# --------------------------------
print("Ejercicio 17")
c = int(input("Celsius: "))
f = c * 9/5 + 32
print("Fahrenheit: " + str(f))
# --------------------------------
# Ejercicio 18: Calcular sueldo semanal
# --------------------------------
print("Ejercicio 18")
Sueldo = int(Input("Sueldo"))
semana = sueldo / 4
print("El sueldo semanal es: " + str(semana))
# --------------------------------
# Ejercicio 19: Suma de edades
# --------------------------------
print("Ejercicio 19")
edad1 = int(input("Edad 1: "))      
edad2 = int(input("Edad 2: "))
suma_edades = edad1 + edad2         
print("La suma de las edades es: " + str(suma_edades))

# --------------------------------
# Ejercicio 20: Mini encuesta
# --------------------------------
