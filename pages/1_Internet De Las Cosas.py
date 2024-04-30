import streamlit as st
from PIL import Image 
st.title("Internet de las cosas")

st.header("Clase Marzo 10")

st.title(" Aplicación para ciudades inteligentes")

st.header( "En este espacio podrás obtener información de tu ciudad.")

image= Image.open ('inteligencia.jpg')
st.image(image,caption= 'Inteligencia Urbana')
st.write("Enlace para mi sistema de internet de las cosas")
st.write("Ingresa al link [link] (https://demo.thingsboard.io/dashboards/221eb150-db1f-11ee-bc03-55147b89654f)")
