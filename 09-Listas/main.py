"""
LISTAS (arrays)

Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.

"""

pelicula ="Batman"

peliculas = ["Batman","Spiderman", "El Señor de los anillos","Hello"]

# Tupla -> no se puede modificar
cantantes = list(('2pac','Drake', 'Jennifer López',"Phill"))

# Rango de números
years = list(range(2020,2050))
variada = ["Victor", 10,4.4, True, "Texto"]

# print(peliculas)
# print(cantantes)
# print(years)
# print(variada)

# Índices positivos de izquierda 0
# De derecha a izquierda se comienza con -1
# Se reemplaza el valor del índice 1
peliculas[1] ="Gran Torino"
print(peliculas)
print(peliculas[0])
print(peliculas[-1])
print(peliculas[1:3])
print(peliculas[1:])