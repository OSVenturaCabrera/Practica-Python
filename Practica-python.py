# =============================
# Ejercicios básicos de Python Israel
# Variables, print() e input()
# =============================

# --------------------------------
# Ejercicio 1: Hola nombre
# Pide el nombre al usuario y lo muestra con un saludo
def Hola_nombre():
    """Pide y muestra el nombre del usuario"""
    titulo = str("Mostrar el Nombre del usuario:")
    print(titulo)
    edad = int(19) # No se usa la varible, solo es para mostrar un 'Entero o Int'
    # Los dijitos del numero 'PI' son infinitos y no siguen ningún 
    # patrón repetitivo, ya que 'PI' es un número 'irracional' y los 'irracionales' 
    # son numeros que no se pueden ser expresados de una forma normal logicamente hablando. :v
    temperatura = float(3.1415926535) 
    # aqui pedi el nombre por la funcion 'input'
    saludo = input("Hola, como te llamas? ")
    print("Hola " + saludo) # muestro el mensaje

# --------------------------------

# --------------------------------
# Ejercicio 2: Edad en un mensaje
# --------------------------------

def Edad_user():
    """Pide y muestra la edad del usuario"""
    mensaje = str("Mostrar la edad del usuario:")
    print(mensaje)
    # vuelvo a pedir un valor en un 'input' dentro de un 'int'
    # 'int' es para hacer la conversion de 'string a int'
    edad = int(input("Ingrese su edad: "))
    altura = float(3.3)
    print(f"Tienes unos {edad} años de edad")

# --------------------------------
# Ejercicio 3: Nombre y edad juntos
# --------------------------------

def Nombre_y_Edad():
    """Pide y muestra el nombre y la edad del usuario"""
    otro_titulo = str("Mostrar Nombre_y_Edad:")
    # los enteros pueden ser numeros "naturales" 
    # positivos incluyendo los negativos.
    otro_entero = int(2) 
    # los decimales son numeros que posen una parte "real (3)" y otra "decimal (.5)"
    otro_decimal = float(3.5)
    # en esta parte yo reutilizo el codigo 
    # ya existente para hacer una sola funcion.
    Hola_nombre()
    Edad_user()

# --------------------------------
# Ejercicio 4: Suma de dos números
# Nota: convertimos a int para poder sumar
# --------------------------------

def Suma():
    """Pide y suma dos numeros ingresados por el usuario :)"""
    variable = str("Suma de numeros:")
    flotante = float(6.6)
    print(variable)
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 + num2
    print(f"resultado: {num1} + {num2} = {r}")

# --------------------------------
# Ejercicio 5: Multiplicación
# --------------------------------

def Multiplicacion():
    """Pide y multiplica dos numeros ingresados por el usuario"""
    var = str("Multiplicacion de numeros:")
    num3 = float(0.33)
    print(var)
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 * num2
    print(f"resultado: {num1} x {num2} = {r}")

# --------------------------------
# Ejercicio 6: Resta
# --------------------------------

def Resta():
    """Pide y resta dos numeros ingresados por el usuario"""
    print("Resta de numeros:")
    con_punto = float(8.4)
    num1 = int(input("Ingrese su primer numero: "))
    num2 = int(input("Ingrese su segundo numero: "))
    r = num1 - num2
    resutado = str(f"resultado: {num1} - {num2} = {r}")
    print(resutado)

# --------------------------------
# Ejercicio 7: Concatenación de cadenas
# --------------------------------

def Concatenar():
    """Funcion para unir las cadenas de texto"""
    print("Concatenar texto:")
    txt1 = input("Ingresa tu primer texto: ")
    txt2 = input("Ingresa tu primer texto: ")
    c = txt1 + txt2
    print(c) # caso 1
    print(txt1 + txt2) # caso 2
    print(txt1, txt2) # caso 3
    caso4 = str(f"{txt1} {txt2}")
    i = int(0)
    float(1.1)
    print(caso4) # caso 4

# --------------------------------
# Ejercicio 8: Repetición de texto
# --------------------------------

def Repetir_texto():
    """Repite un texto por una cantidad determinada"""
    print("Repetir texto:")
    input_user = str("Ingresa tu texto a repetir: ")
    texto = input(input_user)
    o = float(7.1) # no se usa
    cantidad = int(input("Cuantas veces quieres repetirlo? "))
    for i in range(cantidad):
        print(i+1, "- " , texto)
    print("Se ha repetido '" , texto , "'" ,  cantidad , "veces")

# --------------------------------
# Ejercicio 9: Área de un rectángulo
# --------------------------------

def Area_rectángulo():
    """la formula del area de un rectangulo siempre sera "Base x Altura" y ya"""
    print("Area de un Rectángulo:")
    Base = float(input("Ingrese la Base de su rectángulo: "))
    Altura = float(input("Ingrese la Altura de su rectángulo: "))
    Area = int(Base * Altura)
    print("Base:", Base)
    print("Altura:", Altura)
    r = str("El Area de tu Rectangulo es igual a:" , Area)
    print(r)

# --------------------------------
# Ejercicio 10: Área de un triángulo
# --------------------------------

def Area_triangulo():
    """ la formula del area de un triángulo siempre sera "(Base x Altura) ÷ 2" y ya."""
    print("Area de un triángulo:")
    Base = float(input("Ingrese la Base de su rectángulo: "))
    Altura = float(input("Ingrese la Altura de su rectángulo: "))
    Area = int((Base * Altura) / 2) # hice una conversion para los decimales, en dado caso.
    print("Base:", Base)
    print("Altura:", Altura)
    Area_message = str("El Area de tu Rectangulo es igual a:" , Area)
    print(Area_message)


# --------------------------------
# Ejercicio 11: Metros a centímetros
# --------------------------------

def Metros_a_centímetros():
    """Convierte Metros a Centimetros, La formula para caulcula M a C es 
    "M * 100", ya que en cada metro hay 100 centimetros."""
    print("Metros a centímetros")
    Metros = float(input("Ingrese la cantidad de metros a convertir: "))
    Centimetros = int(Metros * 100)
    valor_final = str(f"Si tenemos unos {Metros} metros, entonces hay {Centimetros} centimetros")
    print(valor_final)

# --------------------------------
# Ejercicio 12: Conversor de dólares a pesos
# (ejemplo: 1 dólar = 58 pesos)
# --------------------------------

def dolares_a_pesos():
    """Convierte una cantidad de dolares 
    a su equivalente a pesos dominicanos."""
    print("Conversor de dólares a pesos")
    # le pongo 'int' en vez de float porque el ejericio dice '58' 
    # osea un numero entero, asi que por esa razon no uso 'float' para numeros decimales.
    dolar = int(input("Cuantos dolares tienes? : "))
    pesos = float(dolar * 58)
    print(f"Si tienes unos {dolar} dolares")
    cantidad_pesos = str(f"Entonces posees unos {pesos} pesos.")
    print(cantidad_pesos)

# --------------------------------
# Ejercicio 13: Saludo personalizado
# --------------------------------

def Saludo_personal():
    """Muestra un saludo personalizado por el propio usuario....."""
    print("Saludo personalizado")
    # aqui no se si tengo que pedir el nombre nuevamente, asi que lo interprete asi al final :V
    saludo_propio = str(input("Ingresa un saludo personalizado para que te lo envie: \n"))
    num_x = float(3.99) 
    Manzanas = int(4)
    print(saludo_propio)

# --------------------------------
# Ejercicio 14: Número al cuadrado
# --------------------------------

def Potencia_cuadrada():
    """Muestra la Potencia cuadrado de un numero, 
    osea el resultado de un numero al multiplicarse por si mismo."""
    print("Número al cuadrado")
    num = float(input("Ingresa el numero a elevar a la potencia cuadrada: "))
    cuadrado = int(num ** 2) # ** es igual a decir "num elevado a la 2"
    print(f"El cuadrado de {num} es igual a {cuadrado}")

# --------------------------------
# Ejercicio 15: Promedio de tres números
# --------------------------------

def Mostrar_promedio():
    """Esta funcion pide 3 numeros al usuario tipo 'decimal' y luego 
    saca el promedio de esos 3 numeros juntos en formato 'decimal'."""
    print("Promedio de tres números")
    num1 = float(input("Ingrese su primera nota: "))
    num2 = float(input("Ingrese su segunda nota: "))
    num3 = float(input("Ingrese su tercera nota: "))
    promedio = int((num1 + num2 + num3) / 3)
    r = str(f"Tus notas son: {num1}, {num2}, {num3}")
    print(r)
    print("El promedio es igual a :" , promedio)

# --------------------------------
# Ejercicio 16: Perímetro de un cuadrado
# --------------------------------

def Perimetro_cuadrado():
    """Esta funcion debuelve el valor del Perimetro de un cuadrado 
    dados por el usuario, "un 'cuadrado' simepre tiene 4 lados"."""
    print("Perímetro de un cuadrado:")
    longitud = float(input("Cual es la longitud de los lados de tu cuadrado en CM? : "))
    perimetro = int(longitud * 4) # repito, el 4 es porque simpre tiene 4 lados, es un valor constante.
    final = str(f"El perimetro de tu cuadrado de {longitud} cm de longitud")
    print(final)
    print("El perimetro es igual a :" , perimetro , "cm")

# --------------------------------
# Ejercicio 17: Conversor de temperatura
# Celsius a Fahrenheit
# Fórmula: F = C * 9/5 + 32
# --------------------------------

def Celsius_to_Fahrenheit():
    """Esta funcion te debuelve el valor la cantidad de grados 
    Celsius ingresada por el usuario a su equivalente a Fahrenheit"."""
    print("Convertir de Celsius a Fahrenheit:")
    # para la conversion puedemos usar tanto 'float' como 
    # 'int' pero use el primero por un tema de presicion.
    Celsius = float(input("Ingrese su cantidad de grados en Celcius para convertirla a Fahrenheit :"))
    Fahrenheit = int((Celsius * 9/5) + 32) # copie la formula dada solo cambie 'c' por 'Celsius' :v
    result = str(f"Tus {Celsius}° Celsius son unos {Fahrenheit}° Fahrenheit")
    print(result)

# --------------------------------
# Ejercicio 18: Calcular sueldo semanal
# --------------------------------

def Calcular_sueldo_semanal():
    """Esta funcion te debuelve el calculo 
    del total de tu salario mensual."""
    print("Calcular sueldo semanal:")
    Sueldo_mes = 4000 # esto simularan unos 4,000$ siendo el 'suelo' del mes
    # dividimos lo que gano al anio por 52 porque en 1 anio hay 52 semanas en total.
    Sueldo_semanal = int(Sueldo_mes * 12) / 52
    otroNumeroDeNuevo = float(Sueldo_mes)
    print(f"Tu sueldo mensual es de unos {Sueldo_mes}$")
    string = str(f"Por tanto tu sueldo semanal sera igual a {round(Sueldo_semanal,2)}$")
    print(string)

# --------------------------------
# Ejercicio 19: Suma de edades
# --------------------------------

def Sumar_edades():
    """Esta funcion te debuelve la suma de 
    dos edades ingresadas por el usuario"""
    print("Suma de edades")
    edad1 = int(input("Ingrese su primera edad en años: "))
    edad2 = int(input("Ingrese su segunda edad en años: "))
    edad_falsa = float(11.5)
    suma = edad1 + edad2
    resultados = str(f"La suma entre estas dos edades da un total de : {suma} años")
    print(resultados)

# --------------------------------
# Ejercicio 20: Mini encuesta
# --------------------------------

import os
def Encuesta():
    """Esta funcion pretende simular una encuesta en la terminal 
    con opciones y presionando numeros para simular botones"""
    print("Mini encuesta:")
    fruta1, fruta2, fruta3 = str("Manzana"), str("Pera"), str("Melon")
    frutas = (fruta1, fruta2, fruta3)
    precio1, precio2, precio3 = float(1.99), float(5.78), float(9.43)
    precios = (precio1, precio2, precio3)
    print("Presione el numero dicha fruta para votar por ella:")
    for i in range(len(frutas)):
        # La "i" es el indice que empieza en 0 y luego 
        # va hasta la cantidad de fruta que haya "len(frutas)"
        print(f"{i+1}. {frutas[i]} con un precio de {precios[i]}$")
    voto = int(input("Cual frutas quieres? "))
    # Realmente poner un 'if' es algo revundante si uso el 'for' en MI CASO, la verdad es 
    # mas eficiente <<poner el indice de la fruta y el precio que el usuario quiere>>.🤯🤯🤯
    try:
        # El "-1" es porque en python y en su mayoria de los lenguajes los 'Arreglos o Listas' 
        # empiezan en desde 0 no desde el 1 como a nosotros nos hacen creer a veces :O
        print(f"Ha votado por la {frutas[voto-1]} {precios[voto-1]}$") 
    except:
        print(os.system("cls")) # limpiar 'pantalla' o consola.
        print("ERROR: :(")
        print(f"No hay una fruta en la cuesta que tenga el numero: {voto}")

# # Pruebas:
# Hola_nombre()

# Edad_user()

# # nombre y edad funcionan perfectamente como 1 :)
# Nombre_y_Edad()

# Suma()

# Multiplicacion()

# Resta()

# Concatenar()

# Repetir_texto()

# Area_rectángulo()

# dolares_a_pesos()

# Saludo_personal()

# Potencia_cuadrada()

# Mostrar_promedio()

# Perimetro_cuadrado()

# Celsius_to_Fahrenheit()

# Calcular_sueldo_semanal()

# Sumar_edades()

# Encuesta()