#Insertar varias lineas a la vez

import sqlite3 

conexion = sqlite3.connect("Bases de datos/Ejemplos/base_datos1.db")
cursor = conexion.cursor()

lista_personas = [('Paco','Martinez','Soria',60),('Do','Acquaviti','Notiene',33),('Javichu','Triste','Borracho',28)]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)",lista_personas)
conexion.commit()
conexion.close()