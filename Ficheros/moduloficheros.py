#Crear una clase "Fichero"
#     Crear la funcion "leer_fichero" para leer un fichero de texto
#     Crear la funcion "grabar_fichero" para crear un fichero de texto
#     Crear la funcion "incluir_ficher" para añadir datos al final del fichero de texto#

class Fichero:
    def __init__(self,nombre):
        self.nombre = nombre

    def grabar_fichero(self,texto):
        fichero = open(self.nombre, "wt")
        fichero.write(texto)
        fichero.close()
    
    def incluir_fichero(self,texto):
        fichero = open(self.nombre, "at")
        fichero.write(texto)
        fichero.close()
    
    def leer_fichero(self):
        fichero = open(self.nombre, "rt")
        texto = fichero.read()
        return texto