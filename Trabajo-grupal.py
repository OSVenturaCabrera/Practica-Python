# =============================starlyn Resivido 1=============================     
# EJERCICIO 1: Suma de números
# =============================
# Pide al usuario que ingrese 5 números.
# Guarda los números en una lista y crea una función que calcule la suma de todos ellos.


# =============================
# EJERCICIO 2: Promedio de calificaciones
# =============================
# Pide al usuario la cantidad de calificaciones que desea ingresar.
# Guarda las calificaciones en un array.
# Crea una función que calcule el promedio y diga si está aprobado (>=70) o reprobado.


# =============================
# EJERCICIO 3: Factorial
# =============================
# Pide un número al usuario.
# Crea una función que calcule su factorial usando un bucle.
# Imprime el resultado.


# =============================
# EJERCICIO 4: Números pares e impares
# =============================
# Pide al usuario 10 números.
# Guarda los números en una lista.
# Crea una función que recorra la lista y devuelva dos listas: una con los pares y otra con los impares.
#starlyn
def separar_pares_impares(lista):
    pares = []
    impares = []
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

numero = []
for i in range(10):
    n = int(input(f'ingrese el numero {i+1}:'))
    numero.append(n)
 
pares, impares = separar_pares_impares(numero)
print('numeros pares', pares)
print('numeros impares', impares)


# =============================
# EJERCICIO 5: Número mayor de una lista
# =============================
# Pide al usuario que ingrese 6 números.
# Guárdalos en una lista.
# Crea una función que determine cuál es el número mayor de la lista y lo devuelva.


# =============================
# EJERCICIO 6: Tabla de multiplicar
# =============================
# Pide al usuario un número.
# Crea una función que genere y muestre la tabla de multiplicar de ese número usando un bucle.


# =============================
# EJERCICIO 7: Conteo de números positivos y negativos
# =============================
# Pide al usuario 8 números.
# Guarda los números en una lista.
# Crea una función que recorra la lista y cuente cuántos son positivos, negativos y ceros.


# =============================
# EJERCICIO 8: Juego de adivinar un número
# =============================
# Genera un número aleatorio entre 1 y 20.
# Pide al usuario que adivine el número usando un bucle.
# Indica si el número ingresado es mayor o menor hasta que acierte.
# Crea una función para validar cada intento.
