import streamlit as st
from PIL import Image 
st.title("Mapa de sensores de calidad del aire")

st.header("Este sistema se construyó con un sistema de sensores conetados a internet (IoT) ")

st.title(" ¿En qué influye el clima con la calidad del aire?")

st.header( "En este espacio podrás obtener información de tu ciudad.")

image= Image.open ('inteligencia.jpg')
st.image(image,caption= 'Inteligencia Urbana')
st.write("Enlace para acceder sensores climáticos en tiempo real")
st.write("Ingresa al link [link] (https://demo.thingsboard.io/dashboards/221eb150-db1f-11ee-bc03-55147b89654f)")
