#Consultar con condicion
import sqlite3 

conexion = sqlite3.connect("Bases de datos/Ejemplos/base_datos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE edad > 40")

personas = cursor.fetchall()

for persona in personas:
    print(persona)
    
conexion.close()