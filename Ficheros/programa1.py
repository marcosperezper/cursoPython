# Crear un modulo llamado "moduloficheros.py"
#     Crear una clase "Fichero"
#     Crear la funcion "leer_fichero" para leer un fichero de texto
#     Crear la funcion "grabar_fichero" para crear un fichero de texto
#     Crear la funcion "incluir_ficher" para añadir datos al final del fichero de texto
# Crear un programa llamado "programa1.py"
#     Crear el objeto "fichero" de la clase "Fichero" del modulo "moduloficheros.py"
#     Utilizar el metodo "grabar_fichero" del objeto "fichero" para crear un nuevo fichero de texto
#     Utilizar el metodo "incluir_fichero" para incorporar mas datos al final del fichero
#     Utilizar el metodo "leer fichero" para ver el contendio del fichero
# Ejecutar el programa desde el terminal

import moduloficheros

nombre_fichero = 'Ficheros/fichero1.txt'

fichero = moduloficheros.Fichero(nombre_fichero)

texto = "Primera linea del fichero.\nSegunda fila"

fichero.grabar_fichero(texto)

texto = "\nHola David, jefaso"
fichero.incluir_fichero(texto)

texto_final = fichero.leer_fichero()

print(texto_final)