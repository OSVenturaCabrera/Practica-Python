#En esta Practica vamos a resolver los siguientes ejercicios utilizando condicionales en Python: Israel Ulloa
#----------------------------------------------------------------------------------------------

import os # libreria para usar comandos de la consola 'ejemplo: cls'

#Ejercicio 1: Par o impar
#------------------------------------

def Par_Impar(num):
    """Devuelve si un numero ingresado por el usuario es par o impar."""
    os.system("cls")
    if num % 2:
        print(f"{num} es impar")
    else:
        print(f"{num} es par")

# Ejercicio 2: Mayor de edad
#------------------------------------

def Mayor_edad():
    """Evalua si el usuario es un adulto segun la edad ingresada."""
    os.system("cls")
    edad = int(input("Ingresa tu edad: "))
    if edad < 18:
        print("No eres mayor de edad, eres menor de edad! ❌")
    elif edad > 17:
        print("Eres mayor de edad, eres un adulto! 🎉")

# Ejercicio 3: Comparar dos números
#------------------------------------

def Comparar_nums():
    """Compara si dos numeros ingresados por el usuario son iguales."""
    os.system("cls")
    num1 = int(input("Ingresa tu numero 1: "))
    num2 = int(input("Ingresa tu numero 2: "))
    if num1 > num2:
        print(f"{num1} es mayor que {num2}.")
    elif num1 < num2:
        print(f"{num1} es menor que {num2}.")
    else:
        print(f"{num1} y {num2} son iguales.")

# Ejercicio 4: Calificación con letra
#------------------------------------

def Calificacion():
    """Devuelve la nota en forma de Letra segun tu promedio universitario actual."""
    os.system("cls") # limpiar pantalla o consola.
    op = int(input("Ingrese su promedio universitario como '1, 2, 3 , 4': "))
    match op:
        case 4:
            print(f"Tu promedio universitario es una A")
        case 3:
            print(f"Tu promedio universitario es una B")
        case 2:
            print(f"Tu promedio universitario es una C")
        case 1:
            print(f"Tu promedio universitario es una D")
        case _:
            print("Error: valor invalido")

# Ejercicio 5: Cajero automático básico
#------------------------------------

def Cajero():
    """Hace una simulacion de un ATM el cual puede 'Depositar, Retirar y Consultar Saldo'."""
    os.system("cls") # limpiar pantalla
    Dinero = 5000
    print("Cajero Automatico:")
    print("1. Consultar Saldo")
    print("2. Depositar Saldo")
    print("3. Retirar Saldo")
    op = int(input("Presione el numero para realizar dicha accion: "))
    if op < 1 or op > 3: # si el numero presionado no es ninguno de los 3, mando error:
        print("Error: OPCION NO VALIDA!! ❌")
    else:
        match op:
            case 1:
                print(f"Tu saldo acutal es: {Dinero}$ 💰")
            case 2:
                cantidad = float(input("Cuanto dinero deseas Depositar? : "))
                print(f"Tu saldo acutal es: {(Dinero + cantidad)}$ 💲")
            case 3:
                cantidad = float(input("Cuanto dinero deseas Retirar? : "))
                print(f"Tu saldo acutal es: {(Dinero - cantidad)}$ 💵")
        # nota use varios emojis porque 'si', no hay una razon en concreta: 😜

# Par_Impar(2) # caso par
# Par_Impar(3) # caso impar
# Mayor_edad()
# Comparar_nums()
# Calificacion()
Cajero()