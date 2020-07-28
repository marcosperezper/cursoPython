# Crear una base de datos "basededatos.db"
# Crear una tabla "productos" con 3 campos
#     id: Identificador de la tabla, numerico
#     nombre: Nombre del producto, texto
#     precio: precio del producto, numerico

# Insertar 3 productos en la tabla "productos"
#     1,"Impresora",300
#     2,"Raton",20
#     3,"Ordenador"600
# Consultar los prodcutos de la tabla
# Cerrar la base de datos

import sqlite3

conexion = sqlite3.connect("Bases de datos/basededatos.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER,nombre TEXT,precio INTEGER)")

listaproductos  = [(1,'Impresora',300),(2,'Raton',20),(3,'Ordenador',3600)]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",listaproductos)
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")

productos = cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()