import streamlit as st
from PIL import Image 
import pandas as pd
import numpy as np
import geopandas as gpd
import json
    
st.title("Analítica de datos")

with open('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Localización de sensores de calidad del aire en Medellín")

st.write("En este mapa encontrarás sensores de calidad del aire, los cuales miden la contaminación, según el material particulado PM2.5. Y el ozono del aire")
image= Image.open('accidentes.jpg')
st.image(image,caption='Accidentalidad')

st.subheader('Sistema de consulta de sensores de calidad del aire')
st.write("Si desea conocer más información acerca de la calidad del aire en el Valle de Aburrá y otros fenómenos metereológicos, los invitamos a consultar la página del SIATA")
st.write("SIATA [link] (https://demo.thingsboard.io/dashboards/221eb150-db1f-11ee-bc03-55147b89654f)")

La = []
Lo = []
day = []
hour = []
neig = []
dir = []

# Decodificar el archivo en formato JSON (Java Script Object Notation)
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    dia = feature['properties']['dia']
    Hora = feature['properties']['hora']
    barrio = feature['properties']['barrio']
    direccion = feature['properties']['direccion']
    La.append(coordinates[1])
    Lo.append(coordinates[0])
    day.append(dia)
    hour.append(Hora)
    neig.append(barrio)
    dir.append(direccion)

nm = st.slider('Selecciona el número de registros de accidentes quieres visualizar', 5, 1500)
# Construir la tabla de datos (dataframe)
dfLa = pd.DataFrame({'lat': La[0: nm]})
dfLo = pd.DataFrame({'lon': Lo[0: nm]})
dfdia = pd.DataFrame({'dia': day[0:nm]})
dfhor = pd.DataFrame({'Hora': hour[0:nm]})
dfbarr = pd.DataFrame({'Barrio': neig[0:nm]})
dfdir = pd.DataFrame({'Dirección': dir[0:nm]})
df_g = pd.concat([dfLa, dfLo, dfdia, dfhor, dfdir, dfbarr], axis=1)

# Mostrar la tabla de datos (dataframe)
st.dataframe(df_g)
# Dibujar el mapa utilizando las columnas 'lat', 'lon'.
st.map(df_g)

# Realizar un filtrado de los datos

st.subheader('Filtrado')

# Filtrado por hora
option_hour_min = st.selectbox('Selecciona filtro por Hora',
                               ('08:00:00', '09:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00'),
                               key='1')

# Filtrado por día
option_day = st.selectbox('Selecciona filtro por día', ('LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO'))

# Filtrado por barrio
option_neighborhood = st.selectbox('Selecciona filtro por barrio', dfbarr['Barrio'].unique())

# Aplicar los filtros
df_filtrado = df_g.query('dia == @option_day and Hora >= @option_hour_min and Barrio == @option_neighborhood')

# Mostrar el DataFrame filtrado
st.dataframe(df_filtrado)

try:
    # Mostrar la cantidad de incidentes dentro del filtro
    st.metric("Cantidad de Incidentes dentro del filtro", df_filtrado.shape[0])
except:
    pass

# Mostrar un mapa con los incidentes filtrados
st.map(df_filtrado)

St.write("Existen varios tipos de sensores utilizados para medir la calidad del aire, cada uno diseñado para detectar diferentes contaminantes y proporcionar información sobre la composición y concentración de los mismos. Algunos de los tipos de sensores más comunes para medir la calidad del aire son:")
st.header("Sensores de partículas (PM)")
st.write("Estos sensores miden la concentración de partículas suspendidas en el aire, como el polvo, el humo, el polen, el hollín y otros contaminantes sólidos. Los sensores de partículas pueden clasificarse según el tamaño de las partículas que son capaces de detectar, como PM10 (partículas con un diámetro aerodinámico de 10 micrómetros o menos) y PM2.5 (partículas con un diámetro aerodinámico de 2.5 micrómetros o menos).")
st.header("Sensores de gases")
st.write("Monóxido de carbono (CO): Estos sensores detectan la concentración de monóxido de carbono en el aire, un gas incoloro e inodoro producido por la combustión incompleta de combustibles fósiles.")
st.write("Dióxido de azufre (SO2): Detectan la concentración de dióxido de azufre en el aire, un gas generado principalmente por la quema de combustibles fósiles que contiene azufre.")
st.write("Dióxido de nitrógeno (NO2): Estos sensores miden la concentración de dióxido de nitrógeno en el aire, un subproducto de la combustión de combustibles fósiles que contribuye a la formación de smog y lluvia ácida.")
st.write("Óxidos de nitrógeno (NOx): Pueden detectar tanto el dióxido de nitrógeno (NO2) como el monóxido de nitrógeno (NO), que son productos de la combustión a alta temperatura.")
st.write("Ozono (O3): Los sensores de ozono miden la concentración de ozono en el aire, un gas que puede ser perjudicial para la salud humana y el medio ambiente cuando se encuentra en niveles elevados en la atmósfera.")

image= Image.open('contaminantes.jpg')
st.image(image,caption='Principales contaminantes')

