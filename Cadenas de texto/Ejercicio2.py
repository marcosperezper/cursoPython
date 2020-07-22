# Crear una variable "cadena" que contiene el texto "Esto es un texto de ejemplo"
# Crear una variable "longitud" que contiene la longitud de la variable "cadena"
# Crear una variable "mayusculas" que contiene la variable "cadena" en mayusculas
# Crear una variable "resultado" que concatene la variable "mayusculas" y la variable "longitud" convertida a string



cadena = "Esto es un texto de ejemplo"

longitud = len(cadena)
print(longitud)

mayusculas = cadena.upper()
print (mayusculas)

resultado = mayusculas + " tiene longitud de " + str(longitud)
print(resultado)