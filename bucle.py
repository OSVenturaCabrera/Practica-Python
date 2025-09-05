# starlyn Resivido 1
#---------------------------------------------------------------------------------------------- 
# Bucle: Repetición de tareas utilizando bucles en Python
#----------------------------------------------------------------------------------------------

# Ejercicio 1: Contar del 1 al 10
#------------------------------------
print("contar del 1 al 10")
for i in range (1 , 11):
    print(1)

# Ejercicio 2: Suma de los primeros n números
#------------------------------------
print("Suma de los primeros n numenos")
n= int(input("ingresa un numero "))
suma=0
for i in range (1, n + 1):
    suma += i 
print ("la suma de los primeros", n, "numeros es:", suma)

# Ejercicio 3: Tabla de multiplicar
#------------------------------------
print("tabla de multiplicar")
num = int(input("ingresar un numero para ver su tabla"))
for i in range(1, 11):
    print(num, 'x', i ,'=' , num * 1)

# Ejercicio 4: Adivina el número
#------------------------------------
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