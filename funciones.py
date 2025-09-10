# ============================= Israel Ulloa Estevez =============================
# Funciones: Creación y uso de funciones en Python

import os
os.system("cls")

# EJERCICIO 1
# =============================
# Crea una función llamada "saludar" que reciba un nombre como parámetro
# y muestre un saludo personalizado.

# funcion para saludar:
def saludar(nombre):
    print(f"Hola {nombre} ¿como estas hoy?")


# =============================
# EJERCICIO 2
# =============================
# Crea una función llamada "es_par" que reciba un número
# y retorne True si es par o False si es impar.

def Es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

# =============================
# EJERCICIO 3
# =============================
# Crea una función llamada "sumar_lista" que reciba una lista de números
# y retorne la suma de todos los elementos.

def Sumar_lista(numeros):
    return sum(numeros)


# =============================
# EJERCICIO 4
# =============================
# Crea una función llamada "promedio" que reciba 3 calificaciones
# y retorne el promedio.

def Promedio(n1, n2, n3):
    promedio = round(((n1 + n2 + n3) / 3), 2) # saco el promedio.
    return promedio


# =============================
# EJERCICIO 5
# =============================
# Crea una función llamada "es_vocal" que reciba una letra
# y retorne True si es una vocal, False si no lo es.

def Es_vocal(letra):
    vocales = ("a", "e", "i", "o", "u") # almaceno las vocales en una 'tupla'
    if letra in vocales: # evalua si dicha 'letra' esta dentro de la 'tupla'
        return True
    else:
        return False

# =============================
# EJERCICIO 6
# =============================
# Crea una función llamada "mayor" que reciba 2 números
# y retorne el mayor de los dos.

def Mayor(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Ambos numeros son iguales"

# =============================
# EJERCICIO 7
# =============================
# Crea una función llamada "factorial" que reciba un número
# y retorne su factorial (ejemplo: 5! = 5*4*3*2*1).

def factorial(num):
    if num == 0 or num == 1: 
        # evaluo primero si 'num' es 0 o 1 para devolver '1'.
        return 1
    elif num < 0: 
        # si es menor a 0 entonces devolvemos un mensaje de aviso.
        return 'Los numeros negativos no tienen factorial.'
    else:
        # llamo a la propia funcion pero con el parametro 'num - 1'.
        # a esto se le llama 'funcion recursiva' "Una funcion que se llama a si misma generando un 'bucle' de llamadas"
        return num * factorial(num - 1) 