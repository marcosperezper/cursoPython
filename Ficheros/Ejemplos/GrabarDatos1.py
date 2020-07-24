#Grabar datos en un fichero


fichero = open("Ficheros/fichero.txt","at")

linea = "\nOtra linea para mi precioso fichero"

fichero.write(linea)

fichero.close()