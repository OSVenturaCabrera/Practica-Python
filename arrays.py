# =============================1=============================
# EJERCICIO 1: Crear lista de números
# =============================
# Crea una lista con 10 números ingresados por el usuario.
# Luego deberás imprimir la lista completa.
numeros = []  # Lista vacía para guardar los números

for i in range(10):  # Se repite 10 veces
    num = int(input(f"Ingrese el número {i+1}: "))  # Pedir número al usuario
    numeros.append(num)  # Agregar a la lista

print("La lista completa es:", numeros)


# =============================
# EJERCICIO 2: Acceso a elementos
# =============================
# Pide al usuario 5 palabras y guárdalas en una lista.
# Luego muestra:
# - La primera palabra
# - La última palabra
# - La palabra en la posición 3
palabras = []  # Lista vacía para guardar palabras

for i in range(5):  # Se repite 5 veces
    palabra = input(f"Ingrese la palabra {i+1}: ")
    palabras.append(palabra)

print("Primera palabra:", palabras[0])      # Primer elemento
print("Última palabra:", palabras[-1])     # Último elemento
print("Palabra en la posición 3:", palabras[2])  # Posición 3 (índice 2)


# =============================
# EJERCICIO 3: Modificación de lista
# =============================
# Crea una lista con 5 números cualquiera.
# Luego pide al usuario un nuevo número y reemplaza
# el número en la posición 2 con ese nuevo valor.
# Finalmente imprime la lista modificada.
lista = [10, 20, 30, 40, 50]  # Lista inicial
print("Lista original:", lista)

# Mostrar los índices disponibles
print("Posiciones disponibles para cambiar: 0, 1, 2, 3, 4")

# El usuario elige la posición
posicion = int(input("Elija la posición del número que quiere cambiar (0-4): "))

# Verificar que la posición esté dentro del rango
if 0 <= posicion < len(lista):
    nuevo_num = int(input("Ingrese el nuevo número: "))
    lista[posicion] = nuevo_num  # Reemplazar el valor en esa posición
    print("Lista modificada:", lista)
else:
    print("⚠ Error: posición fuera de rango.")

# =============================
# EJERCICIO 4: Recorrido de lista
# =============================
# Pide al usuario que ingrese 6 números.
# Guárdalos en una lista y luego recórrela con un ciclo "for"
# mostrando cada número multiplicado por 2.
numeros2 = []  # Lista vacía

for i in range(6):  # Se repite 6 veces
    n = int(input(f"Ingrese el número {i+1}: "))
    numeros2.append(n)

print("Números multiplicados por 2:")
for n in numeros2:
    print(n * 2)



# =============================
# EJERCICIO 5: Operaciones con listas
# =============================
# Pide al usuario que ingrese 7 números y guárdalos en una lista.
# Luego deberás calcular y mostrar:
# - La suma de todos los números
# - El número mayor
# - El número menor

numeros3 = []

for i in range(7):  # Se repite 7 veces
    n = int(input(f"Ingrese el número {i+1}: "))
    numeros3.append(n)

print("La suma de los números es:", sum(numeros3))   # Suma de todos
print("El número mayor es:", max(numeros3))          # Mayor de la lista
print("El número menor es:", min(numeros3))          # Menor de la lista