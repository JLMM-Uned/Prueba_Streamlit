import streamlit as st
import time

def mi_funcion():
    st.write("¡El botón ha sido clickeado!")

# 1. Definir la función para alternar la visibilidad
def toggle_visibility():
    st.session_state.visible = not st.session_state.visible


st.header('st.button')

# 2. Inicializar el estado de visibilidad
if 'visible' not in st.session_state:
    st.session_state.visible = False

# 3. Crear el botón y asignar la función on_click
st.button("Mostrar/Ocultar Texto", on_click=toggle_visibility)

# 4. Mostrar el texto condicionalmente
if st.session_state.visible:
    mi_funcion()
    #time.sleep(1)
    #toggle_visibility()