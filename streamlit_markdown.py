import streamlit as st

# Ejemplo 1: Markdown simple
st.markdown("# Título Principal")
st.markdown("Este es un párrafo en **negrita**.")

# Ejemplo 2: Markdown con HTML y CSS
st.markdown(
    """
    <style>
        .borde-rojo {
            border: 2px solid red;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
    <div class="borde-rojo">
        <p>Este texto está dentro de un div con un borde rojo, gracias a HTML y CSS.</p>
    </div>
    """,
    unsafe_allow_html=True
)

def mostrar_fichero_en_app(ruta_fichero):
    """
    Lee un fichero de texto y muestra su contenido en la aplicación de Streamlit.
    
    Args:
        ruta_fichero (str): La ruta al fichero que se desea leer.
    """
    try:
        with open(ruta_fichero, "r", encoding="utf-8") as file:
            contenido = file.read()
            st.markdown(contenido)
    except FileNotFoundError:
        st.error(f"Error: El fichero '{ruta_fichero}' no fue encontrado.")
    except Exception as e:
        st.error(f"Ocurrió un error al leer el fichero: {e}")

mostrar_fichero_en_app("Elementos streamlit.txt")