# ============================= ORlin=============================
# EJERCICIO 1: Crear lista de números
# =============================
# Crea una lista con 10 números ingresados por el usuario.
# Luego deberás imprimir la lista completa.
print("Lista de 10 numero")
Numero = {}

for i in range(10):
    num = int(input(f"Ingresa el numero {i+1}: "))
    Numero[i] = num 

print("LISTA DE NUMERO", )
for num in Numero.items():
    print(f"{num}")
# =============================
# EJERCICIO 2: Acceso a elementos
# =============================
# Pide al usuario 5 palabras y guárdalas en una lista.
# Luego muestra:
# - La primera palabra
# - La última palabra
# - La palabra en la posición 3
print("EJERCICIO 2: Acceso a elementos")
print("------------------------------------------")
palabras = {}


for i in range(5):
    num = str(input(f"Dame una palabra {i+1}: "))
    palabras[i] = num 

print("------------------------------------------")
print("Aqui estan sus palabra de acuerdo al mandato")
print("------------------------------------------")
print(f"La primera palabra es: {palabras[0]}")
print(f"La ultima palabra es: {palabras[4]}")
print(f"La palabra de posicion 3 es: {palabras[3]}")

# =============================
# EJERCICIO 3: Modificación de lista
# =============================
# Crea una lista con 5 números cualquiera.
# Luego pide al usuario un nuevo número y reemplaza
# el número en la posición 2 con ese nuevo valor.
# Finalmente imprime la lista modificada.
Numero = [0,0,2,0,0]
print("=========================================================")
print("Modifica el numero 2")
print("=============================")
print(f"{Numero}")
print("Ingrasa el numero que quieres modificar el la pocision 3")
print("=============================")
num = int(input("Ingresa numero: "))

Numero[2] = num
print("=============================")
print("Lista modificada")
print(f"{Numero}")
print("=========================================================")

print("EJERCICIO 4: Recorrido de lista")
print("=============================")
print("Pide al usuario que ingrese 6 números.")
print("Guárdalos en una lista y luego recórrela con un ciclo for")
print("mostrando cada número multiplicado por 2.")
Numero = []
print("==================================================")  
print("===============Ingresa Los Numeros================")  

for i in range(6):
    num = int(input(f"El Numero {i+1}: "))
    Numero.append(num)

print("=============================")  
print("Los Numero Multiplicado por 2")
for num in Numero:
    multi = num * 2
    print(f"{num} * 2 = {multi}")
    print("-----------------------------")  
print("Fin del programa")


# =============================
# EJERCICIO 5: Operaciones con listas
# =============================
# Pide al usuario que ingrese 7 números y guárdalos en una lista.
# Luego deberás calcular y mostrar:
# - La suma de todos los números
# - El número mayor
# - El número menor
print("=============================")
print("EJERCICIO 5: Operaciones con listas")
print("=============================")

Numero = []
for i in range(7):
    Num = int(input(f"Numero {i+1}: "))
    print("=============================")
    Numero.append(Num)

suma = sum(Numero)
Mayor = max(Numero)
Menor = min(Numero)

print(f"El Numero Mayor es: {Mayor}")
print("=============================")
print("=============================")
print(f"El Numero Menor es: {Menor}")
print("=============================")
print("=============================")
print(f"La suma de Todos los Numero es: {suma}")
print("=============================")
