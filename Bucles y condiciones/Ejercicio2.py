# Creamos una variable "nota" que tenga el valor 4.5
# Creamos una variable "trabajo_realizado" que tenga el valor "si"
# Calcular el valor de la variable "nota_final", teniendo en cuenta que si la nota_final es mayor o igual que 4 
# y el valor de "trabajo_realizado" es igual a "si", "nota_final" sera "aprobado", en caso contrario sera "suspenso"

nota = 4.5
trabajo_realizado = "no"

if (nota >= 4) and (trabajo_realizado == "si"):
    nota_final = "aprobado"
else:
    nota_final = "suspenso"

print(nota_final)