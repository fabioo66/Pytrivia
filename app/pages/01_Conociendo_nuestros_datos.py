import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
from PIL import Image
from app_tools import tools
import plotly.graph_objects as go

icon = Image.open("icon.png")
st.set_page_config(page_title="Conociendo nuestros datos", page_icon=icon, layout="wide")

st.title("Conociendo nuestros datos")
st.write("En esta sección vamos a conocer un poco más sobre nuestros datos")

# Aeropuertos
st.subheader("Mapa de aeropuertos según su elevación 🗺️")
st.write('🟢 Para los aeropuertos de altura baja (menos de 131ft).')
st.write('🟠 Para los aeropuertos de altura media (entre 131ft y 903ft).')
st.write('🔴 Para los aeropuertos de altura alta (mas de 903ft).')
## Leemos el csv de aeropuertos
df_airports = pd.read_csv("../custom_datasets/ar-airports.csv")
# Creamos un mapa
m = tools.create_map()
# Por cada linea del dataframe, agregamos un marcador al mapa
df_airports.apply(lambda row: tools.add_marker_to_airport_map(m, row), axis=1)
# Mostramos el mapa de elevaciones
st_folium(m)

# Grafico de torta con los % segun la elevacion a la que se encuentra el aeropuerto
st.subheader('Proporción de aeropuertos segun su elevacion 🍩')
st.write('🟢 Para los aeropuertos de altura baja (menos de 131ft).')
st.write('🟠 Para los aeropuertos de altura media (entre 131ft y 903ft).')
st.write('🔴 Para los aeropuertos de altura alta (mas de 903ft).')
st.write('🔵 Para los aeropuertos de altura desconocida.')

values = df_airports.elevation_name.value_counts().values
labels = df_airports.elevation_name.value_counts().index
colors = ['#FFA500', '#008000', '#FF0000']
# Crear el gráfico de torta con etiquetas y porcentajes más pequeños y ajustando el radio para que se vea mejor
fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, hoverinfo='label+percent+value',
                                 textinfo='percent', textfont=dict(size=20), marker=dict(colors=colors),
                                 hoverlabel=dict(font_size=16))])
fig_pie.update_layout(legend=dict(font=dict(size=20)), width=800, height=600)
# Mostrar el grafico
st.plotly_chart(fig_pie)

# Grafico de barras de cantidad de aeropuertos segun su tamanio
st.subheader('Cantidad de aeropuertos según su tipo y tamaño 📊')
# Configurar los datos para el gráfico de barra
labels = df_airports.type.value_counts().index
sizes = df_airports.type.value_counts().values
fig_bar = go.Figure(data=go.Bar(x=labels, y=sizes, marker=dict(color='skyblue'), hoverinfo='x+y', 
                                name='Cantidad de lagos en las distintas provincias'))
# Configurar algunos aspectos del grafico
fig_bar.update_layout(width=1000, height=600, margin=dict(l=50, r=50, t=50, b=200), xaxis=dict(title_text='Tipos de aeropuertos', 
                    title_font={'size':20}, tickfont=dict(size=16)), yaxis=dict(title_text='Cantidad', 
                    title_font={'size':20}, tickfont=dict(size=16)))
# Mostrar el grafico
st.plotly_chart(fig_bar)


# Lagos
# Hacemos el mapa el lagos
st.subheader("Mapa de lagos de Argentina según su tamaño 🗺️")
st.write('🔴 Para los lagos de superficie grande (superficie mayor a 59 km²)')
st.write('🟠 Para los lagos de superficie media (superficie mayor que 17 km² y menor o igual a 59 km²).')
st.write('🟢 Para los lagos de superficie chica (superficie menor o igual a 17 km²).')
# Leemos el csv de lagos
df_lakes = pd.read_csv("../custom_datasets/lagos_arg.csv")
# Creamos un mapa
m = tools.create_map()
# Por cada linea del dataframe agregamos un marcador al mapa
df_lakes.apply(lambda row: tools.add_marker_to_lakes_map(m, row), axis=1)
# Mostramos el mapa
st_folium(m)


# Grafico de torta con los % de lagos segun su tamaño
st.subheader('Proporción de lagos segun su tamaño 🍩')
st.write('🔴 Para los lagos de superficie grande (superficie mayor a 59 km²)')
st.write('🟠 Para los lagos de superficie media (superficie mayor que 17 km² y menor o igual a 59 km²).')
st.write('🟢 Para los lagos de superficie chica (superwficie menor o igual a 17 km²).')

values = df_lakes['Sup Tamaño'].value_counts().values
labels = df_lakes['Sup Tamaño'].value_counts().index
colors = ['#FFA500', '#008000', '#FF0000', 'FFF333']

fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, hoverinfo='label+percent+value',
                                 textinfo='percent', textfont=dict(size=20), marker=dict(colors=colors),
                                 hoverlabel=dict(font_size=16))])
fig_pie.update_layout(legend=dict(font=dict(size=20)), width=800, height=600)

st.plotly_chart(fig_pie)


# Grafico de barras con la cantidad de lagos en las distintas provincias
st.subheader('Cantidad de lagos en las distintas provincias 📊')
labels_province = df_lakes['Ubicación'].value_counts().index 
amount_province = df_lakes['Ubicación'].value_counts().values 

fig_bar = go.Figure(data=go.Bar(x=labels_province, y=amount_province, marker=dict(color='skyblue'), hoverinfo='x+y', 
                                name='Cantidad de lagos en las distintas provincias'))

fig_bar.update_layout(width=1000, height=600, margin=dict(l=50, r=50, t=50, b=200), xaxis=dict(title_text='Provincias', 
                    title_font={'size':20}, tickfont=dict(size=16)), yaxis=dict(title_text='Cantidad de lagos', 
                    title_font={'size':20}, tickfont=dict(size=16)))

st.plotly_chart(fig_bar)