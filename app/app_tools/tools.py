import csv
import pandas as pd
from pathlib import Path
import random
import streamlit as st
import folium
from app_tools.question import question

def looking_for_user(register_file_route, email):
    '''This function finds the email in the file 
    and returns the line in the file according to the 
    email, else returns -1'''

    found = False
    try:
        with open (register_file_route)as file:
            reader = csv.reader(file)
            for line in reader:
                if line[2] == email:
                    found = True
                    break
    finally:
        #Si el archivo o el usuario no existe, devuelvo false
        #sino devuelvo true
        return found
        

def register(register_file_route, user):
    '''This function creates the file with the new user. if it is created,
    adds a new user'''

    with open(register_file_route, 'a', newline='') as csv_file:
        fieldnames = ['Usuario','Nombre','Mail','Fecha de nacimiento','Genero',]
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)

        #Verifico si el archivo no existe, si no existe creo el header
        if (csv_file.tell() == 0): 
            writer.writeheader()

        writer.writerow({'Usuario': user.username, 'Nombre': user.full_name, 'Mail': user.email,
                         'Fecha de nacimiento': user.date_of_birth, 'Genero': user.gender})
        

def update_user(register_file_route, user):
    '''This function update an user without changing his email'''

    with open(register_file_route, encoding='utf-8') as file:
        reader = csv.reader(file)
        header, data = next(reader), list(reader)

    for line in data:
        if line[2] == user.email:
            line[0] = user.username 
            line[1] = user.full_name
            line[3] = user.date_of_birth
            line[4] = user.gender
            break

    with open(register_file_route, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    return file 


def return_users():
    """This function returns a tuple with the username, the mail and the gender"""

    register_file_route = Path("./files/register.csv")
    list = []
    df_registers = pd.read_csv(register_file_route)
    list = zip(df_registers.Usuario, df_registers.Mail, df_registers.Genero)
    return list 
    

def generate_questions(dict):
    """This function receives a dict with clues of all datasets
    and returns a random clue to answer"""
    
    while True:
        key, value = random.choice(list(dict.items()))
        if (isinstance(value, str)):
            break

    st.session_state.game_state["question_number"] += 1
    return key


def show_parcially_answer(answer):
    """This function receives a word and returns it incomplete"""

    word = ''
    for letter in answer:
        if (letter != ' '):
            if (random.choice([True, False])):
                word += letter
            else:
                word += '_'
        else:
            word += ' '
    return word


def multiple_choice(correct_answer, field):
    """This function receives the correct answer and the field
    the question. Generates a multiple choice by returning a set 
    with 3 options, including the correct answer. """

    if st.session_state.game_state['thematic'] == 'Aeropuertos':
        file_route = Path("../custom_datasets/ar-airports.csv")
    elif(st.session_state.game_state['thematic'] == 'Lagos'):
        file_route = Path("../custom_datasets/lagos_arg.csv")
    elif(st.session_state.game_state['thematic'] == 'Conectividad'):
        file_route = Path("../custom_datasets/Conectividad_Internet.csv")
    else:
        file_route = Path("../custom_datasets/c2022_tp_c_resumen_adaptado.csv")

    df = pd.read_csv(file_route)
    # Obtener el número total de filas
    num_rows = df.shape[0]  
    # Restar 1 porque los índices van de 0 a num_rows-1

    result = {correct_answer}
    while len(result) < 3:
        random_row = random.randint(0, num_rows - 1)
        result.add(df.at[random_row, field])
    return result
    #return [df.field[random_row], df.field[random_row], correct_answer]


def show_questions(dict, key, questions_list):
    """This function creates a question depending the difficulty. If the
    user answer correctly, increments an score. Also creates a question object"""

    with st.form("questions"):
        st.title(f"Pregunta #{st.session_state.game_state['question_number']}")
        for pos in dict:
            if pos != key:
                st.write(f"{pos}: {dict[pos]}")
        if (st.session_state.game_state['difficulty'] == 'Facil'):
            answer = st.radio(key, st.session_state.game_state["multiple_choice"])
        else:
            if (st.session_state.game_state['difficulty'] == 'Media'):
                st.write(f'Pista: {show_parcially_answer(dict[key])}')
            answer = st.text_input(f"Adivine el siguiente campo: {key}")

        submit_button = st.form_submit_button("Responder")

    if submit_button:
        print(f"Respuesta: {str(answer).lower()}  Respuesta correcta: {dict[key].lower()} \n")
        if str(answer).lower() == str(dict[key]).lower():
            st.session_state.game_state["correct_answers"] += 1
        st.session_state.game_state["state"] = "generate_question"
        Question = question (st.session_state.game_state['question_number'], dict, dict[key], answer, key)
        questions_list.append(Question)
        st.rerun()


def airport_options():
    """This function creates a dict with clues for the airport thematic"""

    airports_file_route = Path("../custom_datasets/ar-airports.csv")
    df_airports = pd.read_csv(airports_file_route)
    
    # Obtener el número total de filas
    num_rows = df_airports.shape[0]  
    # Restar 1 porque los índices van de 0 a num_rows-1
    random_row = random.randint(0, num_rows - 1)  


    airport_name = df_airports.name[random_row]
    municipality = df_airports.municipality[random_row]
    region_name = df_airports.region_name[random_row]
    airport_type = df_airports.type[random_row]

    #dict = (hacerlo con pandas)

    dict = {"name" : airport_name, "municipality" : municipality,
         "region_name" : region_name, "type" : airport_type}
    
    return dict


def lakes_options():
    """This function creates a dict with clues for the lake thematic"""

    lakes_file_route = Path("../custom_datasets/lagos_arg.csv")
    df_lakes = pd.read_csv(lakes_file_route)
    
    num_rows = df_lakes.shape[0]  
    random_row = random.randint(0, num_rows - 1)  

    lake_name = df_lakes.Nombre[random_row]
    province = df_lakes.Ubicación[random_row]
    size = df_lakes['Sup Tamaño'][random_row]
    surface = df_lakes['Superficie (km²)'][random_row]

    dict = {"Nombre" : lake_name, "Ubicación" : province,
         "Sup Tamaño" : size, "Superficie (km²)" : surface}
    
    return dict


def conectivity_options():
    """This function creates a dict with clues for the conectivity thematic"""

    conectivity_file_route = Path("../custom_datasets/Conectividad_Internet.csv")
    df_conectivity = pd.read_csv(conectivity_file_route)
    
    num_rows = df_conectivity.shape[0]  
    random_row = random.randint(0, num_rows - 1)  

    poblation = df_conectivity.Poblacion[random_row]
    province = df_conectivity.Provincia[random_row]
    city = df_conectivity.Localidad[random_row]
    optical_fiber = df_conectivity.FIBRAOPTICA[random_row]

    dict = {"Poblacion" : poblation, "Provincia" : province,
         "Localidad" : city, "FIBRAOPTICA" : optical_fiber}
    
    return dict


def census_options():
    """This function creates a dict with clues for the census thematic"""

    census_file_route = Path("../custom_datasets/c2022_tp_c_resumen_adaptado.csv")
    df_census = pd.read_csv(census_file_route)
    
    num_rows = df_census.shape[0]  
    random_row = random.randint(1, num_rows - 1)  

    poblation = df_census["Total de población"][random_row]
    province = df_census.Jurisdicción[random_row]
    poor_people = df_census["Población en situación de calle(²)"][random_row]
    women_poblation = df_census["Mujeres Total de población"][random_row]

    dict = {"Total de población" : poblation, "Jurisdicción" : province,
         "Población en situación de calle(²)" : poor_people, "Mujeres Total de población" : women_poblation}
    
    return dict


def without_accent(word):
    """This function receives a word and returns it without accent"""

    word = word.replace("á", "a")
    word = word.replace("é", "e")
    word = word.replace("í", "i")
    word = word.replace("ó", "o")
    word = word.replace("ú", "u")
    return word


def census_questions():
    """This function creates the questions for the census data set
    due to the values are almost all numbers"""

    dict = census_options()
    st.session_state.game_state["question_number"] += 1
    
    with st.form(key=f"questions"):
        st.title(f"Pregunta #{st.session_state.game_state['question_number']}")
        st.write("Poblacion: ", dict["Total de población"])
        st.write("Total de mujeres: ", dict["Mujeres Total de población"])
        st.write("Total de gente en situacion de calle: ", dict["Población en situación de calle(²)"])
        answer = st.text_input("Adivine la provincia")

        submit_button = st.form_submit_button("Responder")

    if submit_button: 
        if answer.lower() == without_accent(dict["Jurisdicción"].lower()):
            st.session_state.game_state["correct_answers"] += 1

            
def save_session (game_state):
    """This function receives the game state and saves in a csv file all
    user data, including the correct answers and the score"""

    sessions_route = Path ("./files/sessions.csv")
    with open (sessions_route, 'a', newline='') as sessions_file:
        fieldnames = ['Mail', 'Fecha y hora', 'Dificultad', 'Tematica', 'Respuestas correctas', 'Puntaje', 'Genero']
        writer = csv.DictWriter(sessions_file,fieldnames=fieldnames)

        #Verifico si el archivo no existe, si no existe creo el header
        if (sessions_file.tell() == 0): 
            writer.writeheader()
        
        st.session_state.game_state["score"] = st.session_state.game_state["correct_answers"]

        if st.session_state.game_state["difficulty"] == "Media":
            st.session_state.game_state["score"] *= 1.50 
        else:
            if st.session_state.game_state["difficulty"] == "Dificil":
                st.session_state.game_state["score"] *= 2
         

        writer.writerow({'Mail': game_state['mail'], 'Fecha y hora': game_state['date_time'], 'Dificultad': game_state['difficulty'], 'Genero': game_state['gender'],
                         'Tematica': game_state['thematic'], 'Respuestas correctas': game_state['correct_answers'], 'Puntaje': game_state['score']})


def create_map():
    """This function creates a map with the location of Argentina"""

    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5
    )
    return m


def get_color_airport(elevation):
    """This function returns a color depending
    the elevation of the airport"""

    if elevation == 'bajo':
        return 'green'
    elif elevation == 'medio':
        return 'orange'
    else:
        return 'red'


def get_color_lake (size):
    """This function returns a color depending
    the size of the lake"""

    if size == 'chico':
        return 'green'
    elif size == 'medio':
        return 'orange'
    else:
        return 'red'


def add_marker_to_airport_map(m, row):
    """This function receives a map and a row from the airportsdata set
    and add markers depending on the airport elevation"""

    color = get_color_airport(row['elevation_name'])
    folium.Marker(
        [row['latitude_deg'], row['longitude_deg']],
        popup=row['name'],
        icon = folium.Icon(icon="arrow-down", color=color)
    ).add_to(m)


def add_marker_to_lakes_map(m, row):
    """This function receives a map and a row from the lakes dataset
    and add markers depending on the lake elevation"""

    color = get_color_lake(row['Sup Tamaño'])
    folium.Marker(
        [row['Latitud GD'], row['Longitud GD']],
        popup=row['Nombre'],
        icon = folium.Icon(icon="arrow-down", color=color)
    ).add_to(m)