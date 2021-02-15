# Crear una variable numeros con una lista de los numeros del 1 al 10(ambos incluidos)
# Mostrar el valor de la variable "numeros"
# Recoger un dato por teclado y almacenarlo en la variable "dato"
# Convertir "dato" en numero y almacenarlo en la variable "numero"
# Si el valor de "numero" esta en la lista de "numeros" mostrar el mensaje "Si"
# Si el valor de "numero"  no esta en la lista de "numeros" mostrar el mensaje "No"


numeros = list(range(10 + 1))
print(numeros)

dato = input("Introduce un numero: ")
numero = int(dato)

if numero in numeros:
    print("Si")
else:
    print("No")
