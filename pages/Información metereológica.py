import streamlit as st
from PIL import Image 
st.title("Mapa de sensores de calidad del aire")

st.header("Este sistema se construyó con un sistema de sensores conetados a internet (IoT) ")
st.write("Enlace para acceder sensores climáticos en tiempo real")
st.write("Ingresa al link [link] (https://demo.thingsboard.io/dashboards/221eb150-db1f-11ee-bc03-55147b89654f)")

st.title(" ¿En qué influye el clima con la calidad del aire?")

st.header( "Las condiciones meteorológicas pueden influir significativamente en la calidad del aire. Aquí hay algunas maneras en que estas condiciones pueden afectar la calidad del aire:")
image= Image.open ('Cambio climatico.jpg')
st.image(image,caption= 'Cambio climático y calidad del aire')
st.write("Velocidad y dirección del viento: El viento puede dispersar los contaminantes en el aire, alejándolos de su fuente de emisión y diluyendo su concentración en la atmósfera. Sin embargo, si los vientos son suaves o inexistentes, los contaminantes pueden acumularse cerca de su fuente de emisión y aumentar la concentración local del contaminante.")
st.write("Inversión térmica: En condiciones normales, la temperatura del aire disminuye con la altitud. Sin embargo, durante una inversión térmica, una capa de aire cálido se forma sobre una capa de aire frío, lo que crea una especie de "tapa" que atrapa los contaminantes cerca de la superficie. Esto puede llevar a la acumulación de contaminantes y empeorar la calidad del aire.")
st.write("Precipitación: La lluvia y la nieve pueden limpiar el aire al atrapar y eliminar los contaminantes en suspensión. Sin embargo, en algunos casos, la lluvia puede lavar los contaminantes del aire y depositarlos en el suelo o en cuerpos de agua, lo que puede causar la contaminación del suelo y del agua.")
st.write("Temperatura y radiación solar: La temperatura y la radiación solar pueden afectar la formación de contaminantes atmosféricos como el ozono. Las altas temperaturas y la luz solar intensa pueden desencadenar reacciones químicas entre los contaminantes primarios (como los óxidos de nitrógeno y los compuestos orgánicos volátiles) para formar ozono troposférico, que es un componente importante de la contaminación del aire en áreas urbanas.")
st.write("Humedad relativa: La humedad relativa del aire puede influir en la capacidad de dispersión y dilución de los contaminantes. La atmósfera más húmeda tiende a favorecer la dispersión de los contaminantes, mientras que la atmósfera más seca puede permitir que los contaminantes se acumulen y se concentren más cerca de su fuente de emisión.")
         
image= Image.open ('meteorologica.png')
st.image(image,caption= 'Valle de Aburrá')

st.title("El caso de Medellín y el Valle de Aburrá")
st.write("El Valle de Aburrá, ubicado en la región andina de Colombia y donde se encuentra la ciudad de Medellín, tiene características geográficas y meteorológicas que influyen notablemente en la calidad del aire de la región. A continuación, se describen algunas de las principales formas en que las condiciones meteorológicas afectan la calidad del aire en el Valle de Aburrá:")

st.Header("Inversión térmica:")
st.write("Frecuencia y severidad: El Valle de Aburrá experimenta frecuentes eventos de inversión térmica debido a su geografía montañosa. Durante una inversión térmica, una capa de aire cálido se superpone a una capa de aire frío más cercana al suelo, atrapando los contaminantes en la superficie y dificultando su dispersión. Esto puede llevar a altos niveles de contaminación del aire, especialmente durante las horas de la mañana y en las noches frías.")
st.header("Relieve montañoso:")
st.write"Efecto de cuenca: La forma de cuenca del valle dificulta la dispersión de los contaminantes, especialmente en condiciones de calma atmosférica. Los vientos débiles no logran mover eficientemente el aire fuera del valle, lo que contribuye a la acumulación de contaminantes.")
st.header("Vientos:")
st.write("Dirección y velocidad: Los patrones de viento en el Valle de Aburrá influyen en cómo se dispersan los contaminantes. Los vientos que bajan desde las montañas pueden empujar los contaminantes hacia la ciudad y dificultar su dispersión. Por otro lado, vientos más fuertes pueden ayudar a dispersar los contaminantes y mejorar temporalmente la calidad del aire.")
st.write("¡Nota para Carlos Mario! Profe si usted se está tomando el tiempo de leer esto, quiero que sepa que lo quiero mucho.")
st.header("Precipitación:")
st.write("Efecto de lavado: La lluvia puede ayudar a limpiar el aire al arrastrar los contaminantes hacia el suelo. Sin embargo, los patrones de precipitación varían y la lluvia no siempre ocurre cuando los niveles de contaminación son altos. Durante la temporada seca, la falta de lluvia puede permitir que los contaminantes se acumulen en el aire.")
st.header("Temperatura y radiación solar:")
st.write("Formación de ozono: Las altas temperaturas y la intensa radiación solar pueden aumentar la formación de ozono troposférico, un contaminante secundario que se forma a partir de reacciones químicas entre óxidos de nitrógeno (NOx) y compuestos orgánicos volátiles (COV). Durante días soleados y cálidos, los niveles de ozono pueden aumentar, empeorando la calidad del aire.")
st.header("Humedad relativa:")
st.write("Dispersión de partículas: La humedad puede afectar la dispersión y la composición de las partículas en suspensión. En condiciones de alta humedad, las partículas pueden absorber agua y aumentar de tamaño, lo que puede afectar su capacidad para permanecer en el aire y su impacto en la salud humana.")

st.write("En resumen, las condiciones meteorológicas en el Valle de Aburrá, junto con su geografía particular, desempeñan un papel crucial en la calidad del aire. La combinación de inversiones térmicas frecuentes, la forma de cuenca del valle, los patrones de viento, las precipitaciones y otros factores meteorológicos contribuyen a los desafíos en el manejo de la calidad del aire en la región. Estas condiciones requieren estrategias específicas y adaptadas para monitorear y mitigar la contaminación del aire en el Valle de Aburrá.")
