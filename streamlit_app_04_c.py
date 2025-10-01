import streamlit as st

st.set_page_config(layout="centered")

def metric_con_borde(label, value, delta):
    """
    Muestra una métrica de Streamlit con un borde.
    """
    html_code = f"""
    <style>
        .metric-card {{
            border: 2px solid #555555;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            background-color: #f0f2f6;
            text-align: center;

            
            /* Limita el ancho */
            max-width: 200px; 
            width: 100%;
            overflow: auto; /* Opcional: añade una barra de desplazamiento si el contenido excede la altura */
            
            /* Limita la altura */
            max-height: 120px;
            overflow: auto; /* Opcional: añade una barra de desplazamiento si el contenido excede la altura */

            /* Opcional: se puede usar Flex o Grid para forzar las posiciones dentro de la etiqueta de métricas */
        }}
        .metric-label {{
            font-size: 1rem;
            color: #555555;
            font-weight: bold;
        }}
        .metric-value {{
            font-size: 2.5rem;
            font-weight: bold;
            color: #333333;
        }}
        .metric-delta {{
            font-size: 1rem;
            color: #28a745;
        }}
    </style>
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-delta">{delta}</div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

st.title("Ejemplo de Métrica con Borde en Streamlit")

# Usamos la función personalizada para mostrar métricas con estilo
metric_con_borde("Ventas Totales", "€1,250,000", "+5% desde el mes anterior")
metric_con_borde("Usuarios Activos", "25,000", "-2% desde la semana pasada")