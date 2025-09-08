#============================= Orlin =============================
#---------------------------------------------------------------------------------------------- 
# Bucle: Repetición de tareas utilizando bucles en Python
#----------------------------------------------------------------------------------------------

# Ejercicio 1: Contar del 1 al 10
#------------------------------------
print("Ejercicio 1: Contar del 1 al 10")
for i in range(0,10):
    print("===================================")
    print(f"Numero: {i+1}")
print("===============Fin del programa===============")

# Ejercicio 2: Suma de los primeros n números
#------------------------------------

print("Ejercicio 2: Suma de los primeros n números")
print("========================================================================")
Numeros = []
num = int(input("Cuanto Numero quieres sumar: ej. Los 1o Primeros. "))
num2 = num + 1
for i in range(0, num2):
    Numeros.append(i)
    print(f"Numero: {i+1}")
    print("===============")

suma = sum(Numeros)
print(f"=======================La Suma del 1 al {num}=========================")
print(f" Es: {suma} ")
print("===========================fin del Progrma===============================")

# Ejercicio 3: Tabla de multiplicar
#------------------------------------
print("Ejercicio 3: Tabla de multiplicar")
print("==================================")
num = int(input("Cual Numero tu quieres multiplicar: "))
for i in range(1,13):
    multi = num * i
    print(f"============ {num} * {i} es: {multi}")
    i = i + 1
# Ejercicio 4: Adivina el número
#------------------------------------

import os # libreria para usar comandos de la consola 'ejemplo: cls'
os.system("cls")
print("Adivina el número")
import random

numero_secreto = random.randint(1, 20)  # número aleatorio entre 1 y 20
intento = 0
while True:
    intento = int(input("Adivina un número entre 1 y 20: "))
    if intento == numero_secreto:
        print("Ese es el número correcto ", numero_secreto)
        break
    elif intento < numero_secreto:
        print("Muy bajo")
    else:
        print("Muy alto")

# Ejercicio 5: Verificar si un número es primo
#------------------------------------
print("Verificar si un número es primo")
num = int(input("Ingresa un número: "))
es_primo = True

if num < 2:
    es_primo = False
else:
    for i in range(2, int(num ** 0.5) + 1):  # solo se verifica hasta la raíz cuadrada
        if num % i == 0:
            es_primo = False
            break

if es_primo:
    print(num, "Es un número primo.")
else:
    print(num, "NO es un número primo.")