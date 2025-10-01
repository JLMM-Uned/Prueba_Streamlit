import streamlit as st

def mi_funcion():
    st.write("¡El botón ha sido clickeado!")


st.header('st.button')

if st.button('Say hello', on_click=mi_funcion):
     st.write('Why hello there')
else:
     st.write('Goodbye')