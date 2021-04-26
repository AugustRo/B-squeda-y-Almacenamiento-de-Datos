import sqlite3
from sqlite3 import Error
import pandas as pd
import matplotlib.pyplot as plt

archivo_excel = "Olympic Athletes.xlsx"

# Cargar en memoria la hoja de cÃ¡lculo en formato de Excel usando "pandas"
archivo_memoria = pd.read_excel(archivo_excel)

# Extraer el nÃºmero de columnas de la hoja de cÃ¡lculo
columnas = archivo_memoria.columns
# Lee todas las columnas del archivo en memoria
datos = archivo_memoria[columnas]

#Guardar en una lista la columna Athlete
Lista_Atletas= archivo_memoria['Athlete'].tolist()
#Guardar en una lista la columna Age
Lista_Edad= archivo_memoria['Age'].tolist()
#Guardar en una lista la columna Country
Lista_Pais= archivo_memoria['Country'].tolist()
#Guardar en una lista la columna Year
Lista_Anio= archivo_memoria['Year'].tolist()
#Guardar en una lista la columna Closing Ceremony Date
Lista_Ceremonia= archivo_memoria['Closing Ceremony Date'].tolist()
#Guardar en una lista la columna Sport
Lista_Deporte= archivo_memoria['Sport'].tolist()
#Guardar en una lista la columna Gold Medals
Lista_Gold= archivo_memoria['Gold Medals'].tolist()
#Guardar en una lista la columna Silver Medals
Lista_Silver= archivo_memoria['Silver Medals'].tolist()
#Guardar en una lista la columna Bronze Medals
Lista_Bronze= archivo_memoria['Bronze Medals'].tolist()
#Guardar en una lista la columna Total Medals
Lista_Total_Medallas= archivo_memoria['Total Medals'].tolist()

#Pruebas
#print(Lista_Atletas[0])
#print(Lista_Edad[0])
#print(Lista_Pais[0])
#print(Lista_Anio[0])
#print(Lista_Ceremonia[0])
#print(Lista_Deporte[0])
#print(Lista_Gold[0])
#print(Lista_Silver[0])
#print(Lista_Bronze[0])
#print(Lista_Total_Medallas[0])

def sql_connection():
    try:
        conexion = sqlite3.connect('olimpiadas.db')
        return conexion
    except Error:
        print(Error)
def sql_table(con):
    objetoCursor = con.cursor()
    #Crear la tabla datos si no existe ya
    objetoCursor.execute("CREATE TABLE IF NOT EXISTS datos(Atleta text, Edad integer, Pais text, Año integer, Ceremonia_Clausura text, Deporte text, Medallas_Oro integer, Medallas_Plata integer, Medallas_Bronze integer, Total_Medallas integer)")
    #For para ingresar los datos a la BD ya que las columnas son del mismo tamaño
    for i in range(len(Lista_Atletas)):
      objetoCursor.execute("INSERT INTO datos (Atleta,Edad,Pais,Año,Ceremonia_Clausura,Deporte,Medallas_Oro,Medallas_Plata,Medallas_Bronze,Total_Medallas)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (str(Lista_Atletas[i]), Lista_Edad[i], str(Lista_Pais[i]), Lista_Anio[i], str(Lista_Ceremonia[i]),str(Lista_Deporte[i]),Lista_Gold[i],Lista_Silver[i],Lista_Bronze[i],Lista_Total_Medallas[i]))
    con.commit()
    #comprobación que si se hizo el INSERT de los datos del EXCEL
    datos = pd.read_sql_query("SELECT * from datos",con)
    #Query para obtener los 3 paises con mayor cantidad de medallas de oro
    medallas= pd.read_sql_query("SELECT Pais, sum(Medallas_Oro) as Medallas_de_Oro FROM datos group by Pais order by Medallas_de_Oro DESC Limit 3",con)
    medallas.plot(kind='bar',x='Pais',y='Medallas_de_Oro',figsize=(6,5),fontsize=10)
    #Imprime todas las columnas para comprobar que estan en la tabla datos
    print(datos)
    #Imprime la tabla con los 3 paises con mas medallas de oro
    print(medallas)
    con.close()
    #Mostrar la gráfica
    plt.show()
    
con = sql_connection() #entrar a la función sql_connection para obtener la conexion
sql_table(con)#entrar a la función sql_table para ingresar a la BD los datos obtenidos del EXCEL y graficarlos usando matplotlib y pandas

