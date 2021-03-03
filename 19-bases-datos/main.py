import mysql.connector
# database= mysql.connector.connect(host='localhost',database='mysql',user='root',password='')
database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='master_python'
)

# La conexión ha sido correcta?
# print(database)

# Cursor - Nos permite ejecutar la consulta
cursor = database.cursor()
# cursor = database.cursor(buffered=True) *** Solo cuando ejecutamos varias consultas diferentes
"""
# Crear base de datos
cursor.execute("CREATE DATABASE IF not EXISTS master_python")

# Para saber en el códgo si existe la base de datos
cursor.execute("SHOW DATABASES")
# Muestra todas las bases de datos existentes
for bd in cursor:
    print(bd)
"""

# # Crear tablas
# cursor.execute("""
# CREATE TABLE vehiculos(
#     id int(10) auto_increment not null,
#     marca varchar(40) not null,
#     modelo varchar(40) not null,
#     precio float(10,2) not null,
#     CONSTRAINT pk_vehiculo PRIMARY KEY(id)
# )
# """)

# # Para saber en el códgo si existe la tabla recién creada para no ir al administrador
# cursor.execute("SHOW TABLES")
# # Muestra todas las bases de datos existentes
# for table in cursor:
#     print(table)

# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
coches = [
    ('Seat', 'Ibiza',5000),
    ('Renault', 'Clio',15000),
    ('Citroen', 'Saxo',2000),
    ('Mercedes', 'Clase C',35000)
]

# cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)",coches)

database.commit() # Guarda los cambios en la base de datos que tenemos dentro del cursor

# LISTAR
# cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 and  marca = 'Seat'")
# result = cursor.fetchall()
# for auto in result:
#     print(auto[1],auto[3])

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()
for auto in result:
    print(auto[1], auto[2], auto[3])

# Realiza consulta
# cursor.execute("SELECT marca FROM vehiculos")
# # Trae y almacena todos los datos de la consulta
# result = cursor.fetchall()
# for auto in result:
#     print(auto[0])

# cursor.execute("SELECT * FROM vehiculos")
# coche = cursor.fetchone()
# # for auto in result:
# print(coche)

# BORRAR
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()# Ejecutar cambios en la base

print(cursor.rowcount,"borrados!!") # Indica cuántos registros fueron borrados

# ACTUALIZAR

cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat'")
database.commit() 
print(cursor.rowcount,"actualizados!!") # Indica cuántos registros fueron actualizados