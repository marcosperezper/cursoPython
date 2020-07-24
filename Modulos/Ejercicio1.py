# Crear al modulo "modulo1.py"
# Añadir la clase "Coche" creada en un ejercicio anterior
# Añadir la funcion lambda "media" creada en un ejercicio anterior

# Crear un programa en llamado "programa1.py"
# Importar el modulo creado anteriomente
# Crear un objeto "coche1" al instanciar la clase "Coche" y mostrar las caracteristicas del coche
# Calcular la media de las 3 notas y mostrarlas con print

# Ejecutar el programa y ver el resultado.


import modulo1


coche1 = modulo1.Coche("Pegueot","Granate","Diesel","1.8")
coche1.mostrar_caracteristicas()

resultado = modulo1.media(5,7,9)

print(resultado)