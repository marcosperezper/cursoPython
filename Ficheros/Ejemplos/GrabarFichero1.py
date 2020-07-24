#Grabar un fichero

fichero = open("Ficheros/fichero_grabar.txt", "wt")

texto_fichero = "Hola holita vecinito"
fichero.write(texto_fichero)
fichero.close()