# Estructura de control que permite controlar el flujo del programa
"""
# IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones

SI NO:
    Se ejecutan otro grupo de instrucciones

if condicion:
    instrucciones
else:
    otras instrucciones
    

# Operadores de Comparación

== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
"""

# Ejemplo 1

print("################ EJENPLO 1 ################")

color = "azul"
# color = input("Adivina cuál es mi color favorito: ")
if color == "rojo":
    print("Has adivinado el color")
    print("El color es ROJO")
else: 
    print(f"El color no es {color}")
    print("El color es incorrecto")


# Ejemplo 2

print("\n################ EJENPLO 2 ################")

year = 2020
# year = int(input("¿En qué año estamos?: "))
if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else: 
    print("Es un año anterior a 2021")

# Ejemplo 3

print("\n################ EJENPLO 3 ################")

nombre = input("¿Cuál es tu nombre?: ")
continente = input("¿En qué continente vives?: ")
ciudad = input("¿En qué ciudad vives?: ")
edad = input(("Qué edad tienes?: "))
mayoria_edad = 18

if int(edad) >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente == "Europa":
        print(f"Es europeo y de {ciudad}")
    else:
        print(f"El usuario no es Europeo, es de {ciudad} en {continente}")
else:
    print(f"{nombre} no es mayor de edad")
