# ============================= Israel Ulloa Estevez =============================     

# Librerias que uso para hacer las cosas algo mas 'faciles'
import random # libreria para usar 'numeros pseudoaletorios'
import os # libreria para controlar la terminal
import time # libreria para el contralar el tiempo
os.system("cls") # para siempre limpiar la pantalla.

# EJERCICIO 1: Suma de números
# =============================
# Pide al usuario que ingrese 5 números.
# Guarda los números en una lista y crea una función que calcule la suma de todos ellos.

# def Suma_numeros():
#     cantidad = int(input("Cuantos numeros ingresaras? : ")) # cantidad de numeros
#     nums = [] # lista de numeros 'vacia'
#     for i in range(cantidad):
#         num = float(input(f"Ingresa el numero #{i+1}: ")) # numero del usuario en el indice 'i'
#         nums.append(num) # agregamos dicho numero a la lista 'vacia'
#     print("Los numeros ingresados son:\n")
#     # imprimo la lista de numeros
#     print(nums) 
#     # muestro la suma con la funcion 'sum' que es para sumar todos los datos de la lista.
#     print("La suma de los numeros es igual a :" , sum(nums))

# Suma_numeros() # prueba de la funcion.

# =============================
# EJERCICIO 2: Promedio de calificaciones
# =============================
# Pide al usuario la cantidad de calificaciones que desea ingresar.
# Guarda las calificaciones en un array.
# Crea una función que calcule el promedio y diga si está aprobado (>=70) o reprobado.


# ===========================
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

# # =============================
# # EJERCICIO 8: Juego de adivinar un número
# # =============================
# # Genera un número aleatorio entre 1 y 20.
# # Pide al usuario que adivine el número usando un bucle.
# # Indica si el número ingresado es mayor o menor hasta que acierte.
# # Crea una función para validar cada intento.

def Adivina_num():
    numero_minimo = 1 # inicial
    numero_maximo = 20 # maximo
    numero_desconocido = random.randint(numero_minimo, numero_maximo) # rango de numeros
    op = 0
    while op != numero_desconocido: # mientras sea diferente no acierta o se acaba
        os.system("cls") # limpiar pantalla
        print("Adivina el numero: ")
        print("==================================")
        op = int(input("Ingresa tu numero: ")) # numero del usuario
        if op < numero_desconocido: 
            # si es menor:
            print(f"Tu numero {op} es menor que '?', vuelve a intentarlo! ❌")
        elif op > numero_desconocido: 
            # si es mayor:
            print(f"Tu numero {op} es mayor que '?', vuelve a intentarlo! ❌")
        elif op == numero_desconocido: 
            # si acierta:
            print(f"Felicidades haz acertado tu numero fue {op} y el numero era {numero_desconocido} ✅")
        else:
            # si dio error por alguna razon 'X'
            print("Algo salio mal!!!!!!!!!!!!!!") 
        time.sleep(5) # tiempo de espera
