# Crea un diccionario con los siguientes pares de valores
#     manzana, apple
#     naranja, orange
#     platano, banana
#     limon, lemon

# Muestra la traduccion para la palabra "naranja"
# Añade un elemento nuevo con "piña" y "pineapple"
# Haz un bucle para mostrar todos los elementos del diccionario

frutas = {"manzana" : "apple", "naranja" : "orange", "platano" : "banana",  "limon" : "lemon"}

frutas["piña"] = "pineapple"

for fruta,valor in frutas.items():
    print("{} en ingles es: {}".format(fruta,valor))