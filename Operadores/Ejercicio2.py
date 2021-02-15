# Crea una variable "minimo" con el valor 20
# Crea una variable "maximo" con el valor 500
# Recoger un valor por teclado y almacenarlo en la variable "dato"
# Convertir la variable "dato" en numerico y almacenarlo en la variable "numero"
# Si el "numero" es menor que el valor de "minimo" mostrar el texto "Valor bajo"
# Si el "numero" es mayor que el valor de "maximo" mostrar el texto "Valor alto"
# Si el "numero" esta entre el valor de "minimo" y "maximo" mostrar el texto "Valor medio"


minimo = 20
maximo = 500

dato = input("Introduce un numero: ")
numero = int(dato)

if numero < minimo :
    print("Valor bajo")
elif numero > maximo:
    print("Valor alto")
else:
    print("Valo medio")