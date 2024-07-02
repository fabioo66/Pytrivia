import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image
import plotly.graph_objects as go
import plotly.express as px
import datetime as dt

sessions_file_route = Path("./files/sessions.csv")
users_file_route = Path("./files/register.csv")

icon = Image.open("icon.png")
st.set_page_config(page_title="Seccion de estadisticas", page_icon=icon, layout="wide")

st.title("Seccion de estadisticas 📈")


# Inciso 1
st.subheader("Grafico de torta con el porcentaje de cada genero que jugo a pytrivia 🍩")
df_sessions = pd.read_csv(sessions_file_route)

values = df_sessions.Genero.value_counts().values
labels = df_sessions.Genero.value_counts().index
colors = ['#FFA500', '#008000', '#FF0000']

fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, hoverinfo='label+percent+value',
                                 textinfo='percent', textfont=dict(size=20), marker=dict(colors=colors),
                                 hoverlabel=dict(font_size=16))])
fig_pie.update_layout(legend=dict(font=dict(size=20)), width=800, height=600)

st.plotly_chart(fig_pie)


# Inciso 2: 
average_score = df_sessions['Puntaje'].mean()
above_average = df_sessions[df_sessions['Puntaje'] > average_score].shape[0]
below_average = df_sessions.shape[0] - above_average

labels = ['Puntaje superior a la media', 'Puntaje inferior o igual a la media']
values = [above_average, below_average]
colors = ['#FFA500', '#FF0000']

fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3, hoverinfo='label+percent+value',
                                 textinfo='percent', textfont=dict(size=20), marker=dict(colors=colors),
                                 hoverlabel=dict(font_size=16))])
fig_pie.update_layout(legend=dict(font=dict(size=20)), width=800, height=600)

st.subheader("Gráfico de torta con porcentaje de partidas que tienen una puntuación superior a la media 🍩")
st.write(f"Porcentaje de puntuación promedio = {average_score:.2f}")
st.plotly_chart(fig_pie)


# Inciso 3: Gráfico de barras que para cada día de la semana muestre la cantidad de partidas realizadas
# Extraer el dia de la semana de la fecha
days_in_spanish = {'Monday': 'Lunes','Tuesday': 'Martes','Wednesday': 'Miércoles','Thursday': 'Jueves','Friday': 'Viernes','Saturday': 'Sábado','Sunday': 'Domingo'}
df_sessions['Fecha y hora'] = pd.to_datetime(df_sessions['Fecha y hora'], format='%Y-%m-%d %H:%M')
df_sessions['Dia de semana'] = df_sessions['Fecha y hora'].dt.day_name().map(days_in_spanish)
# Contar la cantidad de partidas por dia de la semana 
sessions_per_day = df_sessions['Dia de semana'].value_counts().reindex(['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']).fillna(0)
# Crear el gráfico de barras
fig_bar = go.Figure(data=go.Bar(x=sessions_per_day.index, y=sessions_per_day.values, marker=dict(color='skyblue'), hoverinfo='x+y'))
# Configurar algunos aspectos del gráfico
fig_bar.update_layout(
    xaxis=dict(title='Días de la semana', title_font=dict(size=20), tickfont=dict(size=16)),
    yaxis=dict(title='Cantidad de partidas', title_font=dict(size=20), tickfont=dict(size=16)),
    width=800, height=500
)
# Mostrar el gráfico
st.subheader("Cantidad de partidas por día 🎮")
st.plotly_chart(fig_bar)


# Inciso 4: Promedio de preguntas acertadas mensuales entre un rango de dos fechas insertadas en dos inputs.
months_in_spanish = {'January': 'Enero', 'February': 'Febrero','March': 'Marzo','April': 'Abril',
                    'May': 'Mayo','June': 'Junio','July': 'Julio','August': 'Agosto','September': 'Septiembre',
                    'October': 'Octubre','November': 'Noviembre','December': 'Diciembre'}

st.subheader ('Promedio de preguntas acertadas mensuales entre un rango de dos fechas')
with st.form(key='form'):
    st.write ('Ingrese las 2 fechas:')
    first_date = st.date_input('Primera fecha:')
    second_date = st.date_input('Segunda fecha:')
    submitted = st.form_submit_button('Enviar')

if submitted:
    # Filtrar sesiones entre las fechas ingresadas
    mask = ((df_sessions['Fecha y hora'] >= pd.to_datetime(first_date)) & (df_sessions['Fecha y hora'] <= pd.to_datetime(second_date)))
    days_between_dates = df_sessions[mask]
    if not days_between_dates.empty:
        # Agregar columna mes al dataframe filtrado
        days_between_dates['Mes'] = days_between_dates['Fecha y hora'].dt.to_period('M')
        # Sacar el promedio de respuestas correctas por mes
        monthly_average = days_between_dates.groupby('Mes')['Respuestas correctas'].mean().reset_index()
        st.write (f'Rango de fechas seleccionado: {first_date} hasta {second_date}')
        st.write ('Este es el promedio mensual de preguntas acertadas entre las fechas seleccionadas:')
        for index, row in monthly_average.iterrows():
            month_name = months_in_spanish[row['Mes'].strftime('%B')]
            anio = row['Mes'].year
            st.markdown(f"### {month_name} del {anio}:")
            st.markdown(f"**Promedio de preguntas acertadas:** {row['Respuestas correctas']}")
    else:
        st.error ('No se encontraron datos en el rango de fechas seleccionado')


# Inciso 5: Top 10 de usuarios con mayor cantidad de puntos acumulados entre un rango de
# dos fechas insertadas por input.
st.subheader ('Top 10 de usuarios con mayor cantidad de puntos acumulados entre un rango de dos fechas 🔥')
with st.form(key="formm"):
    st.write('Ingrese las 2 fechas:')
    first_date = st.date_input('Primera fecha:')
    second_date = st.date_input('Segunda fecha:')
    submitted = st.form_submit_button('Enviar')

if submitted:
    # Asegurarse de que las fechas sean válidas
    if first_date > second_date:
        st.error("La primera fecha debe ser anterior o igual a la segunda fecha.")
    else:
        # Convertir la columna 'Fecha y hora' a datetime si no lo está
        df_sessions['Fecha y hora'] = pd.to_datetime(df_sessions['Fecha y hora'])
        
        # Filtrar sesiones entre las fechas ingresadas
        mask = (df_sessions['Fecha y hora'].dt.date >= first_date) & (df_sessions['Fecha y hora'].dt.date <= second_date)
        filtered_sessions = df_sessions[mask]

        # Verificar cuántos registros hay después del filtrado
        st.write(f"Total de registros filtrados: {filtered_sessions.shape[0]}")
        
        # Agrupar por usuario y sumar los puntos
        user_scores = filtered_sessions.groupby('Mail')['Puntaje'].sum().reset_index()
        
        # Verificar cuántos usuarios hay después del agrupamiento
        st.write(f"Total de usuarios después del agrupamiento: {user_scores.shape[0]}")
        
        # Ordenar por puntos acumulados en orden descendente y seleccionar los top 10
        top_10_users = user_scores.sort_values(by='Puntaje', ascending=False).head(10)
        
        # Mostrar el resultado en una tabla
        st.subheader(f"Top 10 usuarios con más puntos acumulados entre {first_date} y {second_date}")
        st.table(top_10_users)

# Inciso 6 Ordenar los datasets por dificultad donde primero se debe ubicar el dataset que
# tiene mayor número de errores en las respuestas.

df_sessions['Errores'] = 5 - df_sessions['Respuestas correctas']

# Agrupar por temática y sumar los errores
errores_por_tematica = df_sessions.groupby('Tematica')['Errores'].sum().reset_index()

st.subheader("Datasets ordenados por dificultad y cantidad de errores en las respuestas")
st.write(errores_por_tematica)


# Inciso 7:Gráfico de líneas que permita seleccionar dos usuarios para compararlos. Al
# seleccionarlos se debe mostrar la evolución de su puntaje a lo largo del tiempo.
st.subheader("Evolución del puntaje a lo largo del tiempo 📈")
with st.container(border=True):
    df_sessions['Fecha y hora'] = pd.to_datetime(df_sessions['Fecha y hora'])
    usuarios = df_sessions['Mail'].unique()
    usuario1 = st.selectbox('Selecciona el primer usuario', usuarios)
    usuario2 = st.selectbox('Selecciona el segundo usuario', usuarios)
    filtered_df = df_sessions[(df_sessions['Mail'] == usuario1) | (df_sessions['Mail'] == usuario2)]
    fig = px.line(filtered_df, x='Fecha y hora', y='Puntaje', color='Mail')
    st.plotly_chart(fig)


# Inciso 8: Listar para cada género cuál es la temática en la cual demuestra mayor conocimiento.
# Agrupar por género y temática, y sumar las respuestas correctas
grouped_df = df_sessions.groupby(["Genero", "Tematica"])["Respuestas correctas"].sum().reset_index()
# Encontrar la temática con más respuestas correctas para cada género
max_knowledge_df = grouped_df.loc[grouped_df.groupby("Genero")["Respuestas correctas"].idxmax()]
# Renombrar columnas para que sean más descriptivas
max_knowledge_df = max_knowledge_df.rename(columns={
    "Genero": "Género",
    "Tematica": "Temática",
    "Respuestas correctas": "Respuestas Correctas"
})
# Mostrar el resultado como una tabla en Streamlit
st.subheader("Listado de la temática en la cual cada género demuestra mayor conocimiento")
st.table(max_knowledge_df)


# Inciso 9:
resultados = df_sessions.groupby('Dificultad').agg(
    puntaje_promedio=('Puntaje', 'mean'),
    cantidad_elegida=('Dificultad', 'count')
).reset_index()

st.subheader("Listado con el promedio obtenido en cada dificultad y la cantidad de veces que fue elegida.")
st.write(resultados)


# Inciso 10: Listado de usuarios en racha
# Filtrar las partidas de los ultimos 7 dias 
today = dt.datetime.today()
start_date = today - dt.timedelta(days=7)
last_seven_days = df_sessions[(df_sessions['Fecha y hora'] >= start_date) & (df_sessions['Fecha y hora'] <= today)] 
# Filtrar partidas con puntaje mayor a 0 
valid_sessions = last_seven_days[(last_seven_days['Puntaje'] > 0)]
# Extraer el día de la semana de la columna 'Fecha y hora'
valid_sessions['Dia de la semana'] = valid_sessions['Fecha y hora'].dt.dayofweek
# Contar los dias unicos en los que el usuario tiene una partida valida
days_per_user = valid_sessions.groupby('Mail')['Dia de la semana'].nunique()
# Filtrar los usuarios que tienen partidas validas en los ultimos 7 dias 
users_on_streak = days_per_user[days_per_user == 7].index.tolist()
# Mostrar la lista de usuarios en racha 
st.subheader('Usuarios en racha 🔥')
df_users = pd.read_csv(users_file_route)
if users_on_streak:
    for mail in users_on_streak:
        username = df_users.loc[df_users['Mail'] == mail, 'Usuario'].iloc[0]
        st.write(f'Nombre de usuario: {username} / Mail: {mail}')
else:
    st.write("No se han encontrado jugadores en racha") 