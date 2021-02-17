# Crear una variable diccionario con los pares de valores siguientes
#     clave = uno     valor = one
#     clave = dos     valor = two
#     clave = tres     valor = three
# Mostrar por pantalla el valor de la variable diccionario
# Añadir un nuevo elemento al diccionario
#     clave = cuatro     valor = four
# Mostrar ahora el valor del diccionario
# Recoger un valor introducido por teclado y almacenarlo en la variable "dato"
# Utilizar "dato" como clave del diccionario para recuperar su valor


diccionario = {"uno": "one", "dos": "two", "tres": "three"}
print(diccionario)

diccionario["cuatro"] = "four"
print(diccionario)

dato = input("Introduce una clave para ver su valor: ")
valor = diccionario[dato]
print(valor)