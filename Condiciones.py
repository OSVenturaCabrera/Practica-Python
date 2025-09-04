#------------ORlin-----------------
#En esta Practica vamos a resolver los siguientes ejercicios utilizando condicionales en Python: 
#----------------------------------------------------------------------------------------------

#Ejercicio 1: Par o impar
#------------------------------------
num = int(input("Ingresa un numero: "))
if num % 2:
    print("Es impar")
else:
    print("Es par")
# Ejercicio 2: Mayor de edad
#------------------------------------
nun = int(input("Ingresa tu edad: "))
if nun >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

# Ejercicio 3: Comparar dos números
#------------------------------------
num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))

if num1 > num2:
    print("el numero: " + str(num1) + " es mayor que: " + str(num2))
elif num1 == num2:
    print("son iguales")
else:
    print("el numero: " + str(num2) + " es mayor que: " + str(num1))

# Ejercicio 4: Calificación con letra
#------------------------------------
nota = float(input("Nota: "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >=70:
    print("C")
else:
    print("F")

# Ejercicio 5: Cajero automático básico
#------------------------------------
print("1: depositar 2: Retirar 3: consultar")
num1 = int(input("Digite un numero: "))
if num1 == 1:
    print("gracias por retirar")
elif num1 == 1:
    print("gracias por depositar")
elif num1 == 3:
    print("gracias por consultar")
else:
    print("Error")
