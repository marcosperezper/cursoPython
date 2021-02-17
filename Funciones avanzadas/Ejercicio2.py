# A partir de la lista de "numeros" que contiene numeros del 1 al 10, obtener mediante filter
# una lista llamda "pares" con los numeros pares de la lista "numeros"

numeros = list(range(10+1))


# def pares():
#     pares = list()
#     for numero in numeros:
#         if numero % 2 == 0:
#             pares.append(numero)
#     print(pares)
# pares()


def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

resultado = filter(par, numeros)
pares = list(resultado)
print(pares)