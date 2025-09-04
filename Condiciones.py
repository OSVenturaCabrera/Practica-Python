#En esta Practica vamos a resolver los siguientes ejercicios utilizando condicionales en Python: Starlyn
#----------------------------------------------------------------------------------------------

#Ejercicio 1: Par o impar
#------------------------------------

print("Par o impar")  # Muestra el título del ejercicio

num = int(input("Ingresa un número: "))  # Pide un número entero al usuario

if num % 2 == 0:  # Verifica si el número dividido entre 2 da resto 0
    print(num, "El número es par.")  # Si el resto es 0, es par
else:  # Si no se cumple la condición anterior
    print(num, "El número es impar.")  # Es impar

# Ejercicio 2: Mayor de edad
#------------------------------------

print ('Mayor de edad')  # Muestra el título del ejercicio
edad = int(input("Ingresa tu edad: "))  # Pide la edad al usuario
if edad >= 18:  # Verifica si la edad es mayor o igual a 18
    print("Eres mayor de edad.")  # Si es mayor o igual a 18, es mayor de edad
else:  # Si no se cumple la condición anterior
    print("Eres menor de edad.")  # Si es menor de 18, es menor de edad

# Ejercicio 3: Comparar dos números
#------------------------------------

print('comparar dos numeros') # Muestra el título del ejercicio
a = int(input('ingresa el primer numero: ')) # Pide un número entero al usuario
b = int(input('ingresa el segundo numero: ')) # Pide un número entero al usuario
if a > b: # Verifica si el primer número es mayor que el segundo
    print(a, 'es mayor que', b) # Si el primer número es mayor, lo indica
elif a < b: # Verifica si el primer número es menor que el segundo
    print(a, 'es menor que', b) # Si el primer número es menor, lo indica
else: # Si no se cumple ninguna de las condiciones anteriores
    print(a, 'es igual que', b) # Si es igual, lo indica

# Ejercicio 4: Calificación con letra
#------------------------------------

print("Calificación con letra")  # Muestra el título del ejercicio

nota = int(input("Ingresa tu calificación (0-100): "))  # Pide la calificación en número

if nota >= 90:  # Si la nota es 90 o más
    print("Calificación: A")  # Excelente
elif nota >= 80:  # Si está entre 80 y 89
    print("Calificación: B")  # Muy buena
elif nota >= 70:  # Si está entre 70 y 79
    print("Calificación: C")  # Aprobado
else:  # Si es menor a 60
    print("Calificación: F")  # Reprobado

# Ejercicio 5: Cajero automático básico
#------------------------------------

print("Cajero automático básico")  # Muestra el título del ejercicio

saldo = 50000  # Establece un saldo inicial en la cuenta
print("Tu saldo actual es:", saldo)  # Muestra el saldo inicial

opcion = int(input("Elige una opción: 1- Depositar, 2- Retirar, 3- Consultar saldo: "))  # Menú de opciones

if opcion == 1:  # Si eligió depositar
    deposito = int(input("Ingresa la cantidad a depositar: "))  # Pide el monto
    saldo += deposito  # Suma el depósito al saldo
    print("Has depositado", deposito, "tu nuevo saldo es:", saldo)  # Muestra el nuevo saldo
elif opcion == 2:  # Si eligió retirar
    retiro = int(input("Ingresa la cantidad a retirar: "))  # Pide el monto a retirar
    if retiro <= saldo:  # Verifica si hay suficiente saldo
        saldo -= retiro  # Resta el retiro al saldo
        print("Has retirado", retiro, "tu nuevo saldo es:", saldo)  # Muestra el nuevo saldo
    else:  # Si no hay suficiente dinero
        print("Fondos insuficientes.")  # Mensaje de error
elif opcion == 3:  # Si eligió consultar saldo
    print("Tu saldo actual es:", saldo)  # Muestra el saldo
else:  # Si eligió una opción no válida
    print("Opción no válida.")  # Mensaje de error