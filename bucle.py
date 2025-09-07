#============================= Israel Ulloa Estevez =============================
#---------------------------------------------------------------------------------------------- 
# Bucle: Repetición de tareas utilizando bucles en Python
#----------------------------------------------------------------------------------------------

import os # libreia para comandos de consola
import random # libreria para nuemros aleatorios
import time # libreria para manejar el tiempo en los programas

# Ejercicio 1: Contar del 1 al 10
#------------------------------------

def Contar_1_hasta_10():
    """Esta Funcion cuenta los primeros 10 numeros naturales del 1 al 10, con bucles For y While:"""
    os.system("cls")
    print("Cual bucle deseas utilizar: ")
    print("1. Bucle For")
    print("2. Bucle While")
    op = int(input("Entrada: "))
    os.system("cls")
    match op:
        case 1:
            print("1. Bucle For")
            # Con Bucle For
            for i in range(10):
                # +1 porque los indices en programacion inician en 0, NO EN 1
                print("Numuero es : " , (i+1))
        case 2:
            print("2. Bucle While")
            # Con Bucle While
            num = 0
            while num <= 10:
                print("Numuero es : " , num)
                num += 1

# Ejercicio 2: Suma de los primeros n números
#------------------------------------

def Sumar_n_Numeros():
    """Esta funcion muestra la suma de los pirmeros 'n' numeros ingresados por el usuario."""
    os.system("cls")
    n = int(input("Ingresa la cantidad de N numeros que deseas sumar: "))
    sum_n = 0
    for i in range(n):
        aux = sum_n
        sum_n += i # sumamos cada valor de "i" 1,2,3,5,7 ... hasta llegar a 'n'
        aux = sum_n
        print(f"{aux} + {i+1} = {aux + i+1}'")
    print(f"La suma de los {n} primeros numeros es {sum_n+n}")

# Ejercicio 3: Tabla de multiplicar
#------------------------------------

def Tabla_multiplicar():
    """Muestra la tabla de multplicar de dicho que el usuario ingrese."""
    print("Tabla de Multiplicar: ")
    n = int(input("Ingresa el numero 'n' para mostrar su tabla de multiplicar: "))
    for i in range(10): # 10 numeros
        # el +1 es para mostrarle al usuario 1,2,3... pero sin el seria 0,1,2
        print(f"{n} x {i+1} = {n*(i+1)}") # mostramos el resultado y lo repetimos unas 10 veces.

# Ejercicio 4: Adivina el número
#------------------------------------

# El Ejercicio que mas me ha gustado hasta ahora, mi favorito!!
def Adivina_numero():
    """Esta Funcion simula una adivinansa en la cual el usuario 
    establece un rango 'inicial y final' para luego adivinar 
    dicho numero, y contar cuantos intentos hizo el usuario."""
    # Nota no usen 'float' porque sera mucho mas dificil por no decir 
    # casi que "imposible" para el usuario adivinar un 'numero decimal exacto'
    # en un rango extremadamente alto como lo son los 'nuemros deimales'.
    # Ejemplo: 4.6, 7.9, 3.3, 1.10, 8.99, 10.5 etc. 
    num_inicial = int(input("Ingresa un numero para el rango Inicial: "))
    num_final = int(input("Ingresa un numero para el rango Final: "))
    num_desconocido = random.randint(num_inicial, num_final)
    op = 0 # literalmente NADA, para que siempre sea verdadera la condicion:
    while op != num_desconocido:
        op = int(input(f"\nIngresa un numero que puede estar dentro del rango de ({num_inicial} - {num_final}) : "))
        if op < num_desconocido:
            print(f"{op} es menor que el numero '?', espera y vuelve a intentarlo.❌\n")
            time.sleep(5)
        elif op > num_desconocido:
            print(f"{op} es mayor que el numero '?', espera y vuelve a intentarlo.❌\n")
            time.sleep(5)
        elif op == num_desconocido:
            print(f"\nFelicidades, {op} es igual a {num_desconocido}")
            print("Ganaste el Juego 🎉🤗✅")

# Ejercicio 5: Verificar si un número es primo
#------------------------------------

def verificar_primo():
    # Este 'num' es el numero del Usuario.
    num = int(input("Ingresa un numero para saber si es Primo o no: "))
    # si es 1 o menor que eso lo mandamos como falso
    if num <= 1:
        return print(f"{num} no es primo. ❌")
    # se inicia en 2 porque se debe dividir siempre por todo menos el 1 y el mismo numero:
    for i in range(2, num):
        if num % i == 0:
            return print(f"{num} no es primo. ❌")
    return print(f"{num} es primo. ✅ haha.")

# Contar_1_hasta_10()
# Sumar_n_Numeros()
# Tabla_multiplicar()
# Adivina_numero()
# verificar_primo()