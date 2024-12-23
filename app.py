import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Aplicación basada en la biblioteca de Python Streamlit')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scat_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
if scat_button: # al hacer clic en el botón
    # escribe un mensaje
    st.write('Creación de un gráfico de dispersión para el archivo de datos de anuncios de venta de vehículos')
    
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, "odometer", y="price")
    
    #mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)