import streamlit as st
from app_tools import tools
from pathlib import Path
from PIL import Image
from app_tools.user import User

icon = Image.open("icon.png")
st.set_page_config(page_title="Formulario de registros", page_icon=icon, layout="wide")

register_file_route = Path('./files/register.csv')

with st.form(key='form'):
    list_gender = ['Masculino', 'Femenino', 'No binario']

    st.write(f"# Formulario de registro 📝")
    st.write(f"## Ingrese los siguientes datos")

    username = st.text_input('Nombre de usuario')
    full_name = st.text_input('Nombre completo')
    email = st.text_input('Mail')
    date_of_birth = st.date_input('Fecha de nacimiento') 
    gender = st.radio('Género', list_gender, index=None)
    user = User(username, full_name, email, date_of_birth, gender)

    submitted = st.form_submit_button("Enviar")

if submitted:
    if not username or not full_name or not email or not date_of_birth or not gender:
        st.error('Por favor complete todos los campos antes de finalizar el formulario')
    elif '@' not in email or '.' not in email or 'com' not in email:
        st.error('Por favor ingrese un correo electrónico válido')
    else:
        st.success(f'Hola {full_name}, gracias por enviar tu formulario')
        found = tools.looking_for_user(register_file_route, user.email)
        if found:
            tools.update_user(register_file_route, user)
        else:
            tools.register(register_file_route, user)
