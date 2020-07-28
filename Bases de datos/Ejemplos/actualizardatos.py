#Actualizar datos

import sqlite3 

conexion = sqlite3.connect("Bases de datos/Ejemplos/base_datos1.db")
cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET nombre = 'Marcos' WHERE nombre = 'Javichu'")

conexion.commit()
conexion.close()