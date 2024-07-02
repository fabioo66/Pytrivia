import streamlit as st
from PIL import Image
import pandas as pd
from pathlib import Path

icon = Image.open("icon.png")
st.set_page_config(page_title="Ranking", page_icon=icon, layout="wide")

sessions_file_route = Path("./files/sessions.csv")
users_file_route = Path("./files/register.csv")

# Muestro el resultado de la partida del jugador 
if st.session_state and st.session_state.game_state['questions_list']:
    st.title("Felicidades, finalizaste tu partida 👏")
    st.subheader("Aquí están tus resultados:")
    st.write(f"Hora de finalización: {st.session_state.game_state['date_time']}")
    st.write(f"Preguntas acertadas: {st.session_state.game_state['correct_answers']}/5")
    st.write(f"Dificultad elegida: {st.session_state.game_state['difficulty']}")
    st.write(f"Puntaje: {st.session_state.game_state['score']}")
    for question in st.session_state.game_state['questions_list']:
        with st.container(border=True):
            st.subheader (f"Pregunta #{question.number}")
            for option in question.options:
                if option != question.key:
                    st.markdown(f"**{option}:** {question.options[option]}")
            st.markdown (f'**Incognita:** {question.key}')
            st.markdown(f'**Respuesta correcta:** {question.correct_answer}')
            if question.correct_answer.lower() == question.user_answer.lower():
                st.success (f'Su respuesta: {question.user_answer}')
            else:   
                st.error (f'Su respuesta: {question.user_answer}')

# Ranking de las mejores 15 partidas

# Leo los archivos csv
df_sessions = pd.read_csv(sessions_file_route)
df_users = pd.read_csv(users_file_route)

# Filtro las columnas necesarias para el ranking 
df_ranking = df_sessions[['Mail', 'Puntaje']]

# Ordeno en orden descendente por puntaje y me quedo con los primero 15
df_ranking = df_ranking.sort_values(by='Puntaje', ascending=False).head(15)

# Mergeo los dataframe para obtener los nombres de usuarios
df_combined = pd.merge(df_ranking, df_users, on='Mail', how='left')

# Creo la columna puesto
df_combined['Puesto'] = range(1, len(df_combined) + 1)

# Asigno como indice del ranking la columna puesto
df_combined = df_combined.set_index('Puesto')

# Muestro el ranking
st.title('Ranking historico de puntajes')
st.table(df_combined[['Usuario','Mail','Puntaje']])