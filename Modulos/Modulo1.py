class Coche :
    def __init__(self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print("La marca del coche es {}, es de color {}, funciona a {} y tiene {} cilindros".format(self.marca,self.color,self.combustible,self.cilindrada))

media = lambda nota1,nota2,nota3: (nota1 + nota2 + nota3) / 3

