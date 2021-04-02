import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os
#esto se hace para asegurar que busca el archivo donde se encuentra el .py
here = os.path.dirname(os.path.abspath(__file__))
print("Hola, ¿Qué archivo desea abrir? escribelo porfavor")
texto = input()
filename = os.path.join(here, texto)

archivo = open (filename,encoding="utf8")#abrimos el archivo con codificacion utf8 para simbolos como acentos
lectura = archivo.read() #aqui es donde se lee

#eliminar simbolos
puntuacion = '()[],.¿?!¡_-*+;:}{/><|°¬$#%&@~^="“”012345679'
sin_puntuacion = ""
for caracter in lectura:
    if(caracter not in puntuacion):
        sin_puntuacion = sin_puntuacion + caracter

archivo.close()#cerramos archivo

nespacionpuntuacion = re.sub(r'[^\w\s]','', sin_puntuacion)


tokens = word_tokenize(nespacionpuntuacion)#esto crea los tokens

#print(tokens)

palabrasnorelevantes = set(stopwords.words('spanish'))#eliminamos palabras no relevantes con stopwords
listafinal = []
for palabra in tokens:
    if palabra not in palabrasnorelevantes:
        listafinal.append(palabra)
print("\n Lista Final\n\n\n")
print(listafinal)
print('\nTotal:',len(listafinal)," de tokens.")

#################################################################################################################################################
#tokenizar positivas
filename = os.path.join(here, 'positivas.txt')
archivo = open (filename,encoding="utf8")#abrimos el archivo con codificacion utf8 para simbolos como acentos
lectura = archivo.read() #aqui es donde se lee

#eliminar simbolos

sin_puntuacion = ""
for caracter in lectura:
    if(caracter not in puntuacion):
        sin_puntuacion = sin_puntuacion + caracter

archivo.close()#cerramos archivo

nespacionpuntuacion = re.sub(r'[^\w\s]', '', sin_puntuacion)


tokenspositivas = word_tokenize(nespacionpuntuacion)#esto crea los tokens

#################################################################################################################################################
#tokenizar negativas
filename = os.path.join(here, 'negativas.txt')

archivo = open (filename,encoding="utf8")#abrimos el archivo con codificacion utf8 para simbolos como acentos
lectura = archivo.read() #aqui es donde se lee


sin_puntuacion = ""
for caracter in lectura:
    if(caracter not in puntuacion):
        sin_puntuacion = sin_puntuacion + caracter

archivo.close()#cerramos archivo

nespacionpuntuacion = re.sub(r'[^\w\s]', '', sin_puntuacion)


tokensnegativas = word_tokenize(nespacionpuntuacion)#esto crea los tokens


cantidadbuenas = 0
cantidadmalas = 0
lista_malas_del_texto = []
lista_buenas_del_texto = []

for palabra in tokens:
    if palabra in tokensnegativas: #esto es para contar cuantas panabras negativas hay
        cantidadmalas += 1
        lista_malas_del_texto.append(palabra)   
    elif palabra in tokenspositivas:
        cantidadbuenas += 1 #esto cuenta las palabras positivas
        lista_buenas_del_texto.append(palabra)   

 
A = list(set(lista_malas_del_texto))  #Cantidad de palabras malas encontradas sin repetir
B = list(set(lista_buenas_del_texto)) #Cantidad de palabras buenas encontradas sin repetir


lista_malas_del_texto_2 = []
lista_buenas_del_texto_2 = []


for palabra in A:
    lista_malas_del_texto_2.append(palabra)  
    lista_malas_del_texto_2.append(str(tokens.count(palabra)))

for palabra in B:
    lista_buenas_del_texto_2.append(palabra)  
    lista_buenas_del_texto_2.append(str(tokens.count(palabra)))


if cantidadbuenas > cantidadmalas:
    print("\nHay más palabras buenas.","\nCantidad de palabras buenas",cantidadbuenas,"\ncantidad de palabras malas",cantidadmalas)
elif cantidadbuenas < cantidadmalas:
    print("\nHay más palabras malas.","\nCantidad de palabras buenas",cantidadbuenas,"\ncantidad de palabras malas",cantidadmalas)
elif cantidadbuenas == cantidadmalas:
    print("\aLa cantidad de palabras buenas y malas es igual.","\ncantidad de palabras buenas",cantidadbuenas,"\ncantidad de palabras malas",cantidadmalas)

print("\nPalabras buenas encontradas y las veces que se repiten:\n\n",lista_buenas_del_texto_2)
print("\nPalabras malas encontradas y las veces que se repiten: \n\n",lista_malas_del_texto_2)