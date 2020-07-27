# Crear el diccionario "frutas"
# frutas = {"manzana" : "apple","naranja":"orange","platano":"banana","limon":"lemon"}

# Grabar esta estructura de datos "frutas" en un fichero binario "fichero.pckl"
# Ya que es un fichero de texto solo se guardaran caracteres, pero no se pueden guardar guardar estas estructuras

# Recuperar esta estructura de datos del fichero "fichero.pckl"
# Verificar que sigue siendo un diccionario ejecutando el metodo .values()

import pickle

frutas = {"manzana" : "apple","naranja":"orange","platano":"banana","limon":"lemon"}

fichero = open("Ficheros Binarios/fichero.pckl" ,"wb")

pickle.dump(frutas,fichero)

fichero.close()

fichero = open("Ficheros Binarios/fichero.pckl" ,"rb")

fichero_leido = pickle.load(fichero)

print(fichero_leido.values())