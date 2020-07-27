import pickle

lista_colores = ["azu","rojo","verde","amarillo"]

fichero = open("Ficheros Binarios/fichero_colores.pckl","wb")

pickle.dump(lista_colores,fichero)

fichero.close()