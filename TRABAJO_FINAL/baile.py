import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 
import joblib



# [theme]
# backgroundColor = "#F0F0F0"
# st.set_page_config(page_title="SPOTIFY DJ", page_icon=":chart_with_upwards_trend:", layout="wide", initial_sidebar_state="expanded", theme="dark")

# @st.cache_data()
# def load_data():
#     music = pd.read_csv(r"C:\Users\Jesús\Desktop\BOOTCAMP\TEMARIO\FINAL_PROYECTO\spotmusic.csv")
#     return music

# # --------------------CARGA DATOS----------------------------#
# df= load_data()

modelo_file = 'modelos\modelo_lgb.pkl'
loaded_model = joblib.load(modelo_file)
# ---------------------------------
# with open('modeloforest.pkl', 'rb') as pickle_in:
#     modelo_rf = joblib.load(pickle_in)
# ----------------------------------------
# seleccion = st.sidebar.selectbox("Selecciona una opción", ["Home", "Predicción"])
# # st.sidebar.image("spotify.png", use_column_width=True)

# # Página de inicio
# if seleccion == "Home":
#     st.title("Predicción de la danzabilidad")
    
    
    

#     # Expansión con información sobre la aplicación
#     with st.expander("¿Qué es esta aplicación?"):
#         st.write("Es una primera aproximación para predecir cuáles son las canciones más bailables")

#     # Cargar imagen
#     img = Image.open('baile.jpg')
#     st.image(img)




# elif seleccion == "Predicción":
    # st.title("¡Vamos a predecir la danceability de la canción!")
    
st.sidebar.image("img\Spotify_logo_with_text.svg.png", use_column_width=True)

# Seleccionar una opción desde la barra lateral
seleccion = st.sidebar.selectbox("Selecciona una opción", ["Predicción"])

# Si se selecciona "Predicción", muestra el contenido de esa página
if seleccion == "Predicción":
    st.title("Página de Predicción")    
    nombre_cancion = st.text_input("Ingresa el nombre de la canción")

    valores_dict = {"poca": 0.0, "media": 0.5, "mucha": 1.0}
    valor_seleccionado = st.select_slider("Popularity:", options=list(valores_dict.keys()))
        # Mostrar el nivel seleccionado
    if valor_seleccionado == 'poca':
        popularity = 0.1
    elif valor_seleccionado == 'media':
        popularity = 0.5
    else:
        popularity = 1.2
        
        
    # popularity = st.slider("Popularity", min_value=-60.0, max_value=0.0, value=-10.0)
    # acousticness = st.slider("Energy", min_value=0.0, max_value=1.0, value=0.7)
    # instrumentalness = st.slider("Instrumentalness", min_value=0.0, max_value=1.0, value=0.1)
    # valence = st.slider("Valence", min_value=0.0, max_value=1.0, value=0.1)
    # loudness = st.slider("Loudness", min_value=0.0, max_value=1.0, value=0.1)
    # speechiness = st.slider("Speechiness", min_value=0.0, max_value=1.0, value=0.1)
    # energy = st.slider("Energy", min_value=0.0, max_value=1.0, value=0.1)
    # music_genre_cod = st.slider("Music Genre",  min_value=0, max_value=10, value=5, step=1)
    # tempo_cod = st.slider("Tempo", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    valores_ac = {"digital": 0.0, "acústica/digital": 0.5, "acústica": 1.0}
    valor_seleccionado = st.select_slider("Acusticness:", options=list(valores_ac.keys()))
        # Mostrar el nivel seleccionado
    if valor_seleccionado == 'digital':
        acousticness = 0
    elif valor_seleccionado == 'acústica/digital':
        acousticness = 0.5
    else:
        acousticness = 1


    valores_in = {"musica vocal": 0.0, "vocal/instrumental": 0.5, "música instrumental": 1.0}
    valor_seleccionado = st.select_slider("Instrumentalness:", options=list(valores_in.keys()))
    if valor_seleccionado == 'vocal':
        instrumentalness = 0
    elif valor_seleccionado == 'vocal/instrumental':
        instrumentalness = 0.5
    else:
        instrumentalness = 1
        


    valores_val = {"atmósfera triste/negativa": 0.0, "atmósfera estándar": 0.5, "atmósfera alegre/positiva": 1.0}
    valor_seleccionado = st.select_slider("Valence:", options=list(valores_val.keys()))
    if valor_seleccionado == 'atmósfera triste/negativa':
        valence = 0
    elif valor_seleccionado == 'atmósfera estándar':
        valence = 0.5
    else:
        valence = 1
        

    valores_loud = {"Susurros Nocturnos (-60 dB a -30 dB)": 0.0, "Serenidad Ambiental (-30 dB a -15 dB)": 0.33, "Energía Crepuscular (-15 dB a 0 dB)": 0.66, 'Tormenta Sonora (0 dB)': 1.0}
    valor_seleccionado = st.select_slider("Loudness:", options=list(valores_loud.keys()))
    if valor_seleccionado == 'Susurros Nocturnos (-60 dB a -30 dB)':
        loudness = 0
    elif valor_seleccionado == 'Serenidad Ambiental (-30 dB a -15 dB)':
        loudness = 0.33
    elif valor_seleccionado == 'Energía Crepuscular (-15 dB a 0 dB)':
        loudness = 0.66
    else:
        loudness = 1
            
    
    valores_speech = {"Instrumental": 0.0, "Vocales Moderadas": 0.5, 'Podcast': 1.0}
    valor_seleccionado = st.select_slider("Speechiness:", options=list(valores_speech.keys()))
    if valor_seleccionado == 'Instrumental':
        speechiness = 0
    elif valor_seleccionado == 'Vocales Moderadas':
        speechiness = 0.5
    else:
        speechiness = 1      

    valores_en = {"Serenidad Calmada": 0.0, "Vitalidad Moderada": 0.33, "Dinamismo Enérgico": 0.66, 'Fuego Apasionado': 1.0}
    valor_seleccionado = st.select_slider("Energy:", options=list(valores_en.keys()))
    if valor_seleccionado == 'Serenidad Calmada':
        energy = 0
    elif valor_seleccionado == 'Vitalidad Moderada':
        energy = 0.33
    elif valor_seleccionado == 'Dinamismo Enérgico':
        energy = 0.66
    else:
        energy = 1      
            
    
    valores_m = {"Electronic": 1, "Anime": 2, "Jazz": 3, 'Alternative': 4, 'Country': 5, 'Rap': 6, 'Blues': 7, 'Rock': 8, 'Classical': 9, 'Hip-Hop': 10}
    valor_seleccionado = st.select_slider("Music Genre:", options=list(valores_m.keys()))
    if valor_seleccionado == "Electronic": 
        music_genre_cod = 1
    elif valor_seleccionado == 'Anime':
        music_genre_cod = 2
    elif valor_seleccionado == 'Jazz':
        music_genre_cod = 3
    elif valor_seleccionado == 'Alternative':
        music_genre_cod = 4
    elif valor_seleccionado == 'Country':
        music_genre_cod = 5
    elif valor_seleccionado == 'Rap':
        music_genre_cod = 6
    elif valor_seleccionado == 'Blues':
        music_genre_cod = 7
    elif valor_seleccionado == 'Rock':
        music_genre_cod = 8
    elif valor_seleccionado == 'Classical':
        music_genre_cod = 9
    else:
        music_genre_cod = 10     
        
    
    valores_t = {"Lento (80-120 BPM)": 0.0, "Medio (121-160 BPM)": 0.5, 'Rápido (161-200 BPM)': 1.0}
    valor_seleccionado = st.select_slider("Tempo:", options=list(valores_t.keys()))
    if valor_seleccionado == 'Susurros Nocturnos (-60 dB a -30 dB)':
        tempo_cod = 0
    elif valor_seleccionado == 'Serenidad Ambiental (-30 dB a -15 dB)':
        tempo_cod = 0.33
    elif valor_seleccionado == 'Energía Crepuscular (-15 dB a 0 dB)':
        tempo_cod = 0.66
    else:
        tempo_cod = 1


    # mapeo = {'Electronic': 1, 'Anime': 2, 'Jazz': 3, 'Alternative': 4, 'Country': 5, 'Rap': 6, 'Blues': 7, 'Rock': 8, 'Classical': 9, 'Hip-Hop': 10}
    # music_genre.map(mapeo)

    loudness_cat = 0 if -47.047 <= loudness < -15 else \
                                1 if -15 <= loudness < -10 else \
                                5 if -10 <= loudness < -5 else \
                                4 if -5 <= loudness < 0 else \
                                1 if 0 <= loudness <= 3.8 else None
    loudness_cod = 0 if loudness_cat == 0 else \
                                6 if loudness_cat == 4 or loudness_cat == 1 else \
                                9 if loudness_cat == 5 else None
    speech_cat = 0 if speechiness < 0.05 else \
                    1 if 0.05 <= speechiness < 0.1 else \
                    2 if 0.1 <= speechiness < 0.15 else \
                    3 if 0.15 <= speechiness < 0.2 else \
                    4 if 0.2 <= speechiness < 0.25 else \
                    5 if 0.25 <= speechiness < 0.3 else \
                    6 if 0.3 <= speechiness < 0.35 else \
                    7 if 0.35 <= speechiness < 0.4 else \
                    8 if 0.4 <= speechiness < 0.45 else \
                    9 if 0.45 <= speechiness < 0.5 else \
                    10 if 0.5 <= speechiness < 0.55 else \
                    11 if 0.55 <= speechiness < 0.6 else \
                    12 if 0.6 <= speechiness < 0.65 else \
                    13 if 0.65 <= speechiness < 0.7 else \
                    14 if 0.7 <= speechiness < 0.75 else \
                    15 if 0.75 <= speechiness < 0.8 else \
                    16 if 0.8 <= speechiness < 0.85 else \
                    17 if 0.85 <= speechiness < 0.9 else \
                    18 if 0.9 <= speechiness < 0.95 else None
    speech_cod = 0 if speech_cat == 0 else \
                    2 if speech_cat == 1 else \
                    4 if speech_cat == 17 or speech_cat == 16 else \
                    6 if speech_cat == 2 or speech_cat == 14 else \
                    8 if speech_cat == 10 or speech_cat == 11 or speech_cat == 15 or speech_cat == 3 else \
                    10 if speech_cat == 9 or speech_cat == 12 else \
                    12 if speech_cat == 8 or speech_cat == 18 else \
                    14 if speech_cat == 7 or speech_cat == 6 or speech_cat == 4 else \
                    16 if speech_cat == 13 or speech_cat == 5 else -1 
    energy_cat = 0 if energy < 0.2 else \
                    1 if 0.2 <= energy < 0.4 else \
                    2 if 0.4 <= energy < 0.6 else \
                    3 if 0.6 <= energy < 0.8 else \
                    4 if 0.8 <= energy < 0.9999 else None
    energy_cod = 0 if energy_cat == 0 else \
                    2 if energy_cat == 1 else \
                    4 if energy_cat == 4 else \
                    6 if energy_cat == 3 else \
                    7 if energy_cat == 2 else -1
    datos = pd.DataFrame({
        'popularity': [popularity],
        'acousticness': [acousticness],
        'instrumentalness': [instrumentalness],
        'valence': [valence],
        'loudness_cod': [loudness_cod],
        'speech_cod': [speech_cod],
        'energy_cod': [energy_cod],
        'tempo_cod': [tempo_cod],
        'music_genre_cod': [music_genre_cod]       
    })
    prediccion = [-1]
    if st.button("Predecir"):
        prediccion = loaded_model.predict(datos)
        st.write("Resultado de la predicción:")
        if prediccion[0] == -1:
            st.write("Haz tu predicción")
        elif prediccion[0] < 0.35:
            st.write("La canción", nombre_cancion, "tiene danceability")
        else:
            st.write("La canción", nombre_cancion, "no tiene mucha danceability.")
