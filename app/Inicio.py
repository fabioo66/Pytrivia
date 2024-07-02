import streamlit as st
from PIL import Image

icon = Image.open("icon.png")
st.set_page_config(page_title="Inicio", page_icon=icon, layout="wide")

st.title("Bienvenidos a Pytrivia :wave:")
st.subheader("Explora las diferentes secciones a continuación")

with st.container():
    # Conociendo nuestros datos
    st.write("## Conociendo nuestros datos")
    st.write("Descubre más sobre los datos que utilizamos y su origen.")
    button = st.button("Ir a Conociendo nuestros datos")
    if (button):
        st.switch_page("pages/01_Conociendo_nuestros_datos.py")

    # Juego
    st.write("## Juego")
    st.write("""
    Participa en nuestro juego interactivo y divertite aprendiendo.
    
    ### Breve Descripción del Juego:
    El juego consta de 5 preguntas donde podes elegir entre las siguientes temáticas:
    - Aeropuertos
    - Lagos
    - Censo
    - Conectividad 
    
    ### Datos Necesarios para Comenzar a Jugar:
    Para jugar, necesitas registrarte con los siguientes datos:
    - Nombre de usuario
    - Nombre completo
    - Correo electrónico
    - Fecha de nacimiento
    - Género
    
    ### Instrucciones Básicas:
    Para jugar, debes ingresar a la página del juego desde el sidebar a la izquierda o desde esta página de inicio.
    
    ### Funcionamiento del Parámetro Dificultad:
    - **Fácil:** Multiple choice con 3 opciones, una es la correcta.
    - **Media:** La respuesta se muestra parcialmente, con algunas letras reveladas.
    - **Difícil:** Sin ayudas, solo 3 pistas disponibles para adivinar.
             
    ### ¿Estas listo?
    """)        

    want_to_play = st.button("Jugar")
    if (want_to_play):
        st.switch_page("pages/02_Juego.py")

    # Formulario de registro
    st.write("## Formulario de registro")
    st.write("Regístrate para obtener acceso completo a todas las funcionalidades.")
    button = st.button("Ir al Formulario de registro")
    if (button):
        st.switch_page("pages/03_Formulario_de_registro.py")

    # Ranking
    st.write("## Ranking")
    st.write("Consulta el ranking y compite con otros usuarios.")
    button = st.button("Ir al Ranking")
    if (button):
        st.switch_page("pages/04_Ranking.py")

    # Sección de estadísticas
    st.write("## Sección de estadísticas")
    st.write("Visualiza estadísticas detalladas y análisis de los datos.")
    button = st.button("Ir a la Sección de estadísticas")
    if (button):
        st.switch_page("pages/05_Seccion_de_estadisticas.py")