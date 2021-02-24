"""
Variable -->  básicamente un contenedor de información que guardará dentro de sí un data. 
Se pueden crear muchas variables. Cada una puede tener un valor distinto

"""

# Creación de variables y asignarles un valor
texto = "Máster en Python"
texto2 = "practicando python"
numero = 45
decimal = 6.7
# Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("--------------------------")

# Reasignación de valores a las variables
numero = 77
decimal=8.9
print(numero)
print(decimal)

print("--------------------------")

# Concatenación
nombre = "Naya"
apellido ="Gonza"
edad = "?"

print(nombre+ " " + apellido + " " + "-" + " " + edad)

# Interpolación
print(f"{nombre} {apellido} - {edad}")

# Método format
print("Hola mi nombre es {} {} y mi edad es {}".format(nombre,apellido,edad))

# No se está concatenando
print(nombre,apellido,edad)