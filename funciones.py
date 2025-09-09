# =============================starlyn Resivido 1=============================
# Funciones: Creación y uso de funciones en Python
# EJERCICIO 1
# =============================
# Crea una función llamada "saludar" que reciba un nombre como parámetro
# y muestre un saludo personalizado.
def saludar(nombre):
    print(f"Hola {nombre}, ¡bienvenido!")   


# =============================
# EJERCICIO 2
# =============================
# Crea una función llamada "es_par" que reciba un número
# y retorne True si es par o False si es impar.
def es_par(numero):
    return numero % 2 == 0



# =============================
# EJERCICIO 3
# =============================
# Crea una función llamada "sumar_lista" que reciba una lista de números
# y retorne la suma de todos los elementos.
def sumar_lista(lista):
    return sum(lista)


# =============================
# EJERCICIO 4
# =============================
# Crea una función llamada "promedio" que reciba 3 calificaciones
# y retorne el promedio.
def promedio(c1, c2, c3):
    return (c1 + c2 + c3) / 3


# =============================
# EJERCICIO 5
# =============================
# Crea una función llamada "es_vocal" que reciba una letra
# y retorne True si es una vocal, False si no lo es.
def es_vocal(letra):
    return letra.lower() in ['a', 'e', 'i', 'o', 'u']

# =============================
# EJERCICIO 6
# =============================
# Crea una función llamada "mayor" que reciba 2 números
# y retorne el mayor de los dos.
def mayor(n1, n2):
    return n1 if n1 > n2 else n2


# =============================
# EJERCICIO 7
# =============================
# Crea una función llamada "factorial" que reciba un número
# y retorne su factorial (ejemplo: 5! = 5*4*3*2*1).
def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
