import streamlit as st
import time

# Prueba para colocar dos cajas de texto, y que se vayan limpiando un segundo después.

# Inicializa el estado para controlar la visibilidad del texto
if 'show_text' not in st.session_state:
    st.session_state.show_text = False

# Función que se ejecuta al hacer clic en el botón
def show_text_on_click():
    st.session_state.show_text = True
    

placeholder = st.empty()
placeholder2 = st.empty()

# Botón para activar la función
st.button("Mostrar Texto por 1 segundo", on_click=show_text_on_click)

# Lógica principal del script
if st.session_state.show_text:
    # Usa un contenedor para mostrar el texto
    
    placeholder.write("¡Texto visible!")
    placeholder2.write("¡Texto 2 visible!")
    
    # Espera 1 segundo y luego oculta el texto
    time.sleep(1)
    placeholder.empty()
    #st.session_state.show_text = False

    # Espera 1 segundo y luego oculta el texto
    time.sleep(1)
    placeholder2.empty()
    st.session_state.show_text = False