# ============================= Israel Ulloa Estevez =============================

import random # para usar numeros 'pseudoaleatorios', otra vez :v

# EJERCICIO 1: Crear lista de números
# =============================
# Crea una lista con 10 números ingresados por el usuario.
# Luego deberás imprimir la lista completa.

def lista_nums():
    # cantidad de numeros
    cantidad = int(input("Cuantos nuemros tendra tu lista? : "))
    nums = [] # lista de numeros 'vacia'
    for i in range(cantidad): # repetimos en base a la 'cantidad'
        # pedimos un nuemros en el indice 'i'
        num = float(input(f"Ingresa tu numero #{i+1} : "))
        nums.append(num) # agregamos el numero 'i' en la lista 'vacia'
    print("Tu lista es:" , nums) # imprimimos la lista.

# lista_nums() # prueba de funcion #1

# =============================
# EJERCICIO 2: Acceso a elementos
# =============================
# Pide al usuario 5 palabras y guárdalas en una lista.
# Luego muestra:
# - La primera palabra
# - La última palabra
# - La palabra en la posición 3

def Elementos():
    # cantidad de elementos:
    cantidad = 5
    lista = [] # lista 'vacia'
    for i in range(cantidad): # repetimos en base a la 'cantidad'
        # pedimos un elemntos en el indice 'i' al usuario
        elemento = str(input(f"Ingresa tu palabra #{i+1} : "))
        lista.append(elemento) # agregamos el elemento 'i' en la lista 'vacia'
    print("Tu lista es:" , lista) # imprimimos la lista.
    # - Moestramos la primera palabra:
    primer_elemento = lista[0]
    print("Tu primera palabra fue :" , primer_elemento)
    # - Moestramos la última palabra:
    ultimo_elemento = lista[-1]
    print("Tu ultima palabra fue :" , ultimo_elemento)
    # - Moestramos la palabra en la posición 3:
    tercer_elemento = lista[round((cantidad / 2))]
    print("Tu tercera palabra fue :" , tercer_elemento)

# Elementos() # prueba de funcion #2

# =============================
# EJERCICIO 3: Modificación de lista
# =============================
# Crea una lista con 5 números cualquiera.
# Luego pide al usuario un nuevo número y reemplaza
# el número en la posición 2 con ese nuevo valor.
# Finalmente imprime la lista modificada.

def Modificar():
    # cantidad de numeros
    cantidad = 5
    nums = [] # lista de numeros 'vacia'
    for i in range(cantidad): # repetimos en base a la 'cantidad'
        # pedimos un nuemros en el indice 'i'
        num = random.randint(1,20) # de 1 a 20 tomara 5 numeros.
        nums.append(num) # agregamos el numero 'i' en la lista 'vacia'
    print("Tu lista es:" , nums) # imprimimos la lista.
    # pedimos al usuario el numero nuevo para 
    # remplazar el del indice '2' con este:
    nuevo_num = float(input("Ingresa un nuevo numero : "))
    # remplazo el indice '1' que es el 2 por el nuevo numero
    nums[1] = nuevo_num 
    print("Tu nueva lista es:" , nums) # imprimimos la lista.

# Modificar() # prueba de funcion #3 

# =============================
# EJERCICIO 4: Recorrido de lista
# =============================
# Pide al usuario que ingrese 6 números.
# Guárdalos en una lista y luego recórrela con un ciclo "for"
# mostrando cada número multiplicado por 2.

def Recorrdio():
    # cantidad de numeros
    cantidad = 6
    nums = [] # lista de numeros 'vacia'
    for i in range(cantidad): # repetimos en base a la 'cantidad'
        # pedimos un nuemros en el indice 'i'
        num = float(input(f"Ingresa tu numero #{i+1} : "))
        nums.append(num) # agregamos el numero 'i' en la lista 'vacia'
    # cliclo para mostrar los 'nums por 2':
    for i in range(cantidad):
        print("Tu lista es:" , nums[i] * 2) # imprimimos la lista.

# Recorrdio() # probando la funcion


# =============================
# EJERCICIO 5: Operaciones con listas
# =============================
# Pide al usuario que ingrese 7 números y guárdalos en una lista.
# Luego deberás calcular y mostrar:
# - La suma de todos los números
# - El número mayor
# - El número menor

def Operacion_nums():
    # cantidad de numeros
    cantidad = 7
    nums = [] # lista de numeros 'vacia'
    for i in range(cantidad): # repetimos en base a la 'cantidad'
        # pedimos un nuemros en el indice 'i'
        num = float(input(f"Ingresa tu numero #{i+1} : "))
        nums.append(num) # agregamos el numero 'i' en la lista 'vacia'
    # Mostrar los siguientes elementos:
    lista_ordenada = Burble_sort(nums) # lista ordenada
    print(f"\nLista de elementos ordenados : " , lista_ordenada)
    print("\nLa suma de los numeros de tu lista es :" , sum(lista_ordenada)) # - La suma de todos los números
    print("\nEl numero mayor de la lista es :" , max(lista_ordenada))
    print("\nEl numero menor de la lista es :" , min(lista_ordenada))

# hice una funcion para ordenar la lista y sacar 
# el numero mayor y el menor de todos
def Burble_sort(lista):
    cantidad = len(lista) # cantidad de elemntos de la lista
    for j in range(cantidad -1, 0, -1):
        for i in range(j):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return lista


# Operacion_nums() # probando la funcion