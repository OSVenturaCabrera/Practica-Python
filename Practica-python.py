# =============================
# Ejercicios básicos de Python Mawtiun
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
# --------------------------------
print("ejercicio 1")
print("Hola, ¿cómo te llamas?")
nombre = input()
print("¡Hola " + nombre + "!")

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------
print("ejercicio 2")
print("hola, Introduce tu edad")
edad = input()
print("tu edad es " +  edad)
# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------
print("ejercicio 3")
print("hola introduce tu nombre y edad")
nombre = input()
edad = input()
print("tu nombre es " + nombre + "y tu edad es " + edad)
# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------
print("ejercicio 4")
print("introduce dos valores a sumar")
numero1 = int(input("Escribe el primer numero "))
numero2 = int(input("Escribe el segundo numero "))

resultado = numero1 + numero2
print("el resultado es " , resultado)
# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------
print("ejercicio 5")
print("introduce dos valores a multiplicar")
numero1 = int(input("Escribe el primer numero "))
numero2 = int(input("Escribe el segundo numero "))

resultado = numero1 * numero2
print("el resultado es " , resultado)
# --------------------------------
# Ejercicio 6: Resta
# --------------------------------
print("ejercicio 6")
print("introduce dos valores a restar")
numero1 = int(input("Escribe el primer numero "))
numero2 = int(input("Escribe el segundo numero "))

resultado = numero1 - numero2
print("el resultado es " , resultado)
# --------------------------------
# Ejercicio 7: Concatenación de cadenas
# --------------------------------
print("ejercicio 7")
print("introduce dos palabras")
texto1 = input("Escribe la primera palabra ")
texto2 = input("Escribe la segunda palabraa ")

resultado = texto1  + texto2
print("tu palabra es " , resultado)
# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------
print("ejercicio 8")
texto = input("Ingrese un texto" )
repetimos = int(input("cuantas veces lo repetimos?"))

for i in range(repetimos):
    print(f"{i+1}. {texto}")
# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------
print("ejercicio 9")
Base = int(input("introduce el valor de la base " ))
Altura = int(input("introduce el valor de la altura " ))
Area = Base * Altura
print("tu Area es de un tamaño de " , Area)
# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------
print("ejercicio 10")
Base = int(input("introduce el valor de la base " ))
Altura = int(input("introduce el valor de la altura " ))
Area = (Base * Altura) / 2
print("tu Area es de un tamaño de " , Area)
# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------
print("ejercicio 11")
metros = float(input("ingrese los metros "))
centimetros = metros * 100
print(f"{metros} metros equivalen a {centimetros} centímetros")
# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------
print("ejercicio 12")
dolar = float(input("ingrese el numero de dolares "))
Pesos = dolar * 63
print(f"{dolar} equivalen a {Pesos} Pesos")
# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------
print("Ejercicio 13")
nombre = input("como te llamas? ")
print("Un saluda a " + nombre + " la kbra de kbras🐐🐐🐐🐐🐐🐐🐐🐐")

# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------
print("ejercicio 14")
numero = int(input("Ingresa tu numero "))
resultado = numero * numero
print("tu numero multiplicado al cuadrado es" , resultado)
# --------------------------------
# Ejercicio 15: Promedio de tres números
# --------------------------------
print("ejercicio 15")
numero1 = int(input("Ingresa tu  primer numero "))
numero2 = int(input("Ingresa tu  segundo numero "))
numero3 = int(input("Ingresa tu  tercer numero "))
resultado = numero1 * numero2 * numero3 / 3
print("tu promedio es de " , resultado)
# --------------------------------
# Ejercicio 16: Perímetro de un cuadrado
# --------------------------------
print("ejercicio 16")
lado = int(input("Ingresa el tamaño del lado "))
resultado = lado * 4
print("tu promedio es de " , resultado)
# --------------------------------
# Ejercicio 17: Conversor de temperatura
# Celsius a Fahrenheit
# Fórmula: F = C * 9/5 + 32
# --------------------------------
print("ejercicio 17")
C = float(input("ingrese la temperatura Celsius "))
F = C * 9/5 + 32
print(f"{C} celcius equivalen a {F} Fahrenheit")
# --------------------------------
# Ejercicio 18: Calcular sueldo semanal
# --------------------------------
print("ejercicio 18")
Horas = int(input("Ingresa el numero de horas trabajadas"))
sueldo = Horas * 110 * 6
print("tu sueldo a la semana es de ", sueldo) 
# --------------------------------
# Ejercicio 19: Suma de edades
# --------------------------------
print("ejercicio 19")
print("introduce dos valores a sumar")
Edad1 = int(input("Escribe la Edad numero 1 "))
Edad2 = int(input("Escribe la Edad numero 2 "))

resultado = Edad1 + Edad2
print("La suma de las edades es " , resultado)
# --------------------------------
# Ejercicio 20: Mini encuesta
# --------------------------------
print("ejercicio 20")
print("hola, Ahora seras participe de una pequeña encuesta")
nombre = input("Cual es tu nombre? ")
print("Muy Bien")
edad = input("Cual es tu edad? ")
print("Muy Bien")
Hobby = input("Cual es tu Hobby? ")
print("Muy Bien")
print("tu Nombre es " + nombre + " tu Edad es " + edad + " y tu Hobby es " , Hobby)
print("Muy Bien Perfecto Muchas Gracias❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")