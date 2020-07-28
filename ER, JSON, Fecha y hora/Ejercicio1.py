#Crear una funcion "buscar" que mediante una expresion regular indique si una palabra esta en una frase

# Probar la funcion "buscar" con estas frases 
#     texto = "Esta es una frase de prueba para hacer busquedas"
#     palabra_a_buscar = "frase"

# En caso de encontrar la palabra en la frase indicar en que posicion empieza y cual finlaiza


import re

def buscar(texto,palabra_a_buscar):
    busqueda = re.search(palabra_a_buscar,texto)
    return busqueda

texto = "Esta es una frase de prueba para hacer busquedas"
palabra_a_buscar = "frase"

busqueda = buscar(texto,palabra_a_buscar)

if(busqueda):
    print("Palabra {} encontrada".format(palabra_a_buscar))
    inicial = busqueda.start()
    final = busqueda.end()
    print("La palabra {} empieza en la posicion {} y termina en la {}" .format(palabra_a_buscar,inicial,final))
else:
    print("Palabra {} no encontrada".format(palabra_a_buscar))