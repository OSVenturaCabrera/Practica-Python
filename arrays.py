# ==========================================================
# EJERCICIO 1: Crear lista de números
# =============================
# Crea una lista con 10 números ingresados por el usuario.
# Luego deberás imprimir la lista completa.
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)
    
    print("La lista completa es " , numeros)

# =============================
# EJERCICIO 2: Acceso a elementos
# =============================
# Pide al usuario 5 palabras y guárdalas en una lista.
# Luego muestra:
# - La primera palabra
# - La última palabra
# - La palabra en la posición 3
Palabras = []

for i in range(5):
    Palabra = input(f"Ingrese la palabra {i+1}: ")
    Palabras.append(Palabra)


print("La primera palabra es:", Palabras[0])      
print("La última palabra es:", Palabras[-1])       
print("La palabra en la posición 3 es:", Palabras[2])

# =============================
# EJERCICIO 3: Modificación de lista
# =============================
# Crea una lista con 5 números cualquiera.
# Luego pide al usuario un nuevo número y reemplaza
# el número en la posición 2 con ese nuevo valor.
# Finalmente imprime la lista modificada.
Lista = [1, 2, 3, 4, 5]

print("Lista original ", Lista)
nuevo_Numero = int(input("ingrese un nuevo numero para remplazar la posicion 2 "))
Lista[1] = nuevo_Numero

print("Lista modificada ", Lista)

# =============================
# EJERCICIO 4: Recorrido de lista
# =============================
# Pide al usuario que ingrese 6 números.
# Guárdalos en una lista y luego recórrela con un ciclo "for"
# mostrando cada número multiplicado por 2.
lista = []

for i in range(6):
    num = int(input(f"Ingrese el número {i+1}: "))
    lista.append(num)

    print("Lista multiplicada x 2 ")
    for num in lista:
        print(num * 2)

# =============================
# EJERCICIO 5: Operaciones con listas
# =============================
# Pide al usuario que ingrese 7 números y guárdalos en una lista.
# Luego deberás calcular y mostrar:
# - La suma de todos los números
# - El número mayor
# - El número menor
Numeros = []


for i in range(7):
    num = int(input(f"Ingrese el número {i}: "))
    Numeros.append(num)
    
    
    
    print("La lista completa es " , Numeros)
    
    
    print("La suma de todos los numeros es ", sum(Numeros))


    mayor = max(Numeros)
    print("El numero mas grande es ", mayor)

    menor = min(Numeros)
    print("El numero mas pequeño es ", menor)