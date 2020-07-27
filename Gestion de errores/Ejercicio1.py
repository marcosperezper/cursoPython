# Crear la funcion "operacion" que dados 3 numeros divida el primer numero entre la resta de los otros dos numeros

# Utilizar la funcion creada con los numeros 5,4,2
# Utilizar la funcion creada con los numeros 6,3,3

# Utilziar el bloque try...except para controlar los posibles errores

def operacion(numero1,numero2,numero3):
    resta = numero2 - numero3
    resultado = numero1 / resta
    return resultado

numero1 = 5
numero2 = 4
numero3 = 2


try:
    resultado = operacion(numero1,numero2,numero3)
    print(resultado)
except ZeroDivisionError:
    print("El divisor es 0")
finally:
    print("Try finalizado")
