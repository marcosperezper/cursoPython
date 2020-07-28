# Insertar datos en una tabla

import sqlite3 

conexion = sqlite3.connect("Bases de datos/Ejemplos/base_datos1.db")
cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Marcos','Perez','Perpina','24')")
conexion.commit()
conexion.close()