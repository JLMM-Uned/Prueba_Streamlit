import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write', divider="blue")

# Ejemplo 1

st.write('Hello, *World!* :sunglasses:')

st.subheader( "Para conocer cómo se escribe en pantalla", help="Esta es la ayuda :heart:")
# Ejemplo 2

st.write(1234)

# Ejemplo 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Ejemplo 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# Más ejemplos: subtitle



# Más ejemplos: Badge
st.subheader( "Badges")
st.write("https://docs.streamlit.io/develop/api-reference/text/st.badge")
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")
st.write("Otros símbolos: [Símbolos](https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded&icon.size=24&icon.color=%231f1f1f)")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# Más ejemplos: Caption
st.subheader( "Caption")
st.write("Esto es texto normal")
st.caption("This is a string that explains something above.")
st.caption("A caption with _italics_ :blue[colors] and emojis :sunglasses:")
st.write("Esto vuelve a ser texto normal")

# Más ejemplos: Code
st.subheader( "Code")

import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

code = '''Is it a crown or boat?
                        ii
                      iiiiii
WWw                 .iiiiiiii.                ...:
 WWWWWWw          .iiiiiiiiiiii.         ........
  WWWWWWWWWWw    iiiiiiiiiiiiiiii    ...........
   WWWWWWWWWWWWWWwiiiiiiiiiiiiiiiii............
    WWWWWWWWWWWWWWWWWWwiiiiiiiiiiiiii.........
     WWWWWWWWWWWWWWWWWWWWWWwiiiiiiiiii.......
      WWWWWWWWWWWWWWWWWWWWWWWWWWwiiiiiii....
       WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWwiiii.
          -MMMWWWWWWWWWWWWWWWWWWWWWWMMM-
'''
st.code(code, language=None)


st.divider(width=64)  # 👈 Draws a horizontal rule
st.write("This is some text.")
st.slider("This is a slider", 0, 100, (25, 75))
st.divider()  # 👈 Draws a horizontal rule
st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule