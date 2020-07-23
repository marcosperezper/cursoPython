# Crear una clase "Coche" que tenga los siguientes atributos:
#     marca,color,combustible,cilindrada

# Crear la funcion "__init__" que asigna los parametros de la clase a los atributos de la clase

# Crear una funcion "mostrar_caracteristicas" que mediante print muestre por pantalla las caracteristicas que tiene el coche

# Crea un objeto "coche1" de la clase "Coche" con los atributos "Opel", "rojo", "gasolina", "1.6"

# Ejecutar la funcion "mostrar_caracterisitcas" del "coche1"


class Coche :
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print("La marca del coche es {}, es de color {}, funciona a {} y tiene {} cilindros".format(self.marca,self.color,self.combustible,self.cilindrada))


coche1 = Coche("Opel","rojo","gasolina","1.6")
coche1.mostrar_caracteristicas()