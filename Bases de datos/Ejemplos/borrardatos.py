#Borrar datos

import sqlite3 

conexion = sqlite3.connect("Bases de datos/Ejemplos/base_datos1.db")
cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Marcos'")

conexion.commit()
conexion.close()