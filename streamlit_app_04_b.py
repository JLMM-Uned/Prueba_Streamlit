import streamlit as st
import pandas as pd
import numpy as np
import random
import string

def crear_dataframe_aleatorio():
    """
    Crea y devuelve un dataframe de pandas aleatorio con 3 registros y 5 columnas.
    La primera columna es de tipo string, y las otras cuatro son de tipo entero.
    """
    # Define la primera columna con valores string aleatorios
    letras = string.ascii_lowercase
    columna_str = [''.join(random.choice(letras) for i in range(5)) for _ in range(3)]
    
    # Crea las cuatro columnas restantes con valores enteros aleatorios
    columna_int1 = np.random.randint(0, 100, 3)
    columna_int2 = np.random.randint(0, 100, 3)
    columna_int3 = np.random.randint(0, 100, 3)
    columna_int4 = np.random.randint(0, 100, 3)
    
    # Crea un diccionario con los datos
    datos = {
        'columna_char': columna_str,
        'columna_int1': columna_int1,
        'columna_int2': columna_int2,
        'columna_int3': columna_int3,
        'columna_int4': columna_int4
    }
    
    # Crea el dataframe a partir del diccionario
    df = pd.DataFrame(datos)
    
    return df

# Ejemplo de uso
df_aleatorio = crear_dataframe_aleatorio()
add_sidebar = st.sidebar.selectbox('Opciones de sidebar', ('Opción 1', 'Opción 2'))

col1, col2, col3, col4, col5 = st.columns(5)
columns = [col1, col2, col3, col4, col5]

if add_sidebar == 'Opción 1':
    st.write ('Has elegido opción 1')
    df = df_aleatorio[['columna_char', 'columna_int1']]
    st.metric('Métrica 1', 302, '50%')

if add_sidebar == 'Opción 2':
    st.write ('Segunda opción')
