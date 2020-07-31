#Dataframes 

import pandas as pd 
import webbrowser

# website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
# webbrowser.open(website)

dataframeNBA = pd.read_clipboard()

# print(dataframeNBA.tail(1)

listaasginaturas = ['matematicas', 'fisica','historia'] 
listanotas = [8,5,9]

dicionario = {'Asignaturas': listaasginaturas, 'Notas': listanotas}

# print(dicionario)

dataframe_notas = pd.DataFrame(dicionario)

print(dataframe_notas)