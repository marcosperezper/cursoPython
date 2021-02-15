# Crear una variabel "tupla" que sea una tupla de los siguientes nombres: Antonio, Pedro y Maria
# Mostrar el valor de la variable "tupla"
# Recoger un dato por teclado y almacenarlo en la variable "dato"
# Si el valor "dato" esta dentro de los valores de la tupla mostar "Si"
# Si el valor "dato"  no esta dentro de los valores de la tupla mostar "No"


tupla = ("Antonio", "Pedro", "Maria")

print(tupla)

dato = input ("Introduce un nombre: ")

if dato in tupla:
    print("Si")
else:
    print("No")