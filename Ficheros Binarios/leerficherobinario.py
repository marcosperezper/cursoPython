import pickle

fichero = open("Ficheros Binarios/fichero_colores.pckl","rb")

lista_leida = pickle.load(fichero)

print(lista_leida)