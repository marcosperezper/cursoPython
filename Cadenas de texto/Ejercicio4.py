# Imprime por pantalla el texto "Introduce el primer numero"
# Crea la variable "dato1" con el valor introducido en el texto anterior
# Imprime por pantalla el texto "Introduce el segundo numero"
# Crea la variable "dato2" con el valor introducido en el texto anterior
# Convertir las variables "dato1" y "dato2" en variables numericas "numero1" y "numero2"
# Crear la variable "suma" con la suma de "numero1" y "numero2"
# Convertir la variable "suma" en una variable de texto denominada "strSuma"
# Crear la variable "resultado" con la concatenacion de "La suma es: " y "strSuma"
# Imprimr por pantall la variable "resultado


dato1 = input("Introduce el primer numero: ")
dato2 = input("Introduce el primer numero: ")

numero1 = int(dato1)
numero2 = int(dato2)

suma = numero1 + numero2
strSuma = str(suma)

resultado = "La suma es: " + strSuma

print(resultado)
