#!/usr/bin/python3
from covid import Covid
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
figure(figsize=(12, 6), dpi=80) #Con esto se ajusta el tamaño de la figura
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

covid = Covid()
countries = covid.list_countries() # Guardamos aqui todos los paises



cuentan=[]
for i in range (11):
    cuentan.append(countries[i]) # Obtenemos los primeros 11 paises ** US no lo pudimos usar asi que nos lo saltamos** 

subtitle=[]
for value in cuentan:
   subtitle.append(value['name']) #Aqui obtenemos solo el nombre de los paises con la llave 'name'

#################################################################################################################################################   
entero = 1
espacio = 0.25
colores=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'r','b', 'g'] # Paleta de colores para bar
print("Top 10 de paises con mayor casos confirmados de COVID-19:")
lista_de_confirmed = []
for largo in subtitle: 
   if entero == 11: #obligamos a salirse cuando llegue a 11 para que no haya un desbordabiento
      break
   prueba = covid.get_status_by_country_name(subtitle[entero]) # Obtemos y agregamos a prueba los datos de los paises del cual mandamos como parametro
   lista_de_confirmed.append((prueba['confirmed'])/1000)       # subtitle (es una lista de los nombres de los top 10 de paises)
   plt.bar(subtitle[entero],lista_de_confirmed[entero-1],color=colores[entero-1],width=.5) 
   entero += 1
   print(prueba)

#################################################################################################################################################
print("\nCasos confirmados de los paises dividido entre 1000:\n",lista_de_confirmed)
plt.legend()
plt.grid() # Genera una cuadrilla
plt.xlabel('PAÍSES') #Label X
plt.ylabel('CASOS CONFIRMADOS X 1000') # Label Y
plt.title('TOP 10 DE PAISES CON CASOS CONFIRMADOS DE COVID-19') # Titulo de la Figura
plt.show()