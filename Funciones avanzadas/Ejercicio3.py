# A partir de una lista de numeros del 1 al 10
# obtener una nueva lista con los elementos incrementados en 10 unidades

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def incrementar(numero):
    return numero + 10


resultado = map(incrementar, lista)

lista2 = list(resultado)
print(lista2)
