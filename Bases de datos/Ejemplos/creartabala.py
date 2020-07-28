#Crear una tabla

import sqlite3 

conexion = sqlite3.connect("Bases de datos/Ejemplos/base_datos1.db")

cursor = conexion.cursor()
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT,apellido1 TEXT,apellido2 TEXT,edad INTEGER)")

conexion.commit()

conexion.close()