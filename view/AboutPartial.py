"""Instructions"""
from PIL import Image
import streamlit as st
def consultar_instrucciones():
    img = Image.open( "JaverianaLogo.jpg" )
    img2 = Image.open( "ISO_7010_M002.svg.png" )
    img3 = Image.open( "logosmall.png" )
    st.markdown("<h1 style='text-align: center; color: white;'>Bienvenido al Acta de Evaluación de Trabajo de Grado</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    col5, col6, col7 = st.columns([6, 7, 7])
    with col5:
        st.write("")
    with col6:
        st.image(img3, width=500, caption='Logo perteneciente a la universidad Javeriana')
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    with col7:
        st.write("")
    col9, col10, col11 = st.columns([8, 6, 5])
    with col9:
        st.write("")
    with col10:
        st.header("Descripción")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
    with col11:
        st.write("")
    col1, col2, col8 = st.columns([3, 10, 2])
    with col1:
        st.write("")
    with col2:
        st.subheader("A continuación podrá observar la descripción de esta apliación para su uso")
        st.write("")
        st.write("")
        st.text(
            "La siguiente aplicación tiene como finalidad automatizar las evaluaciones de trabajos de grado, con el \npropósito de facilitar el proceso.\n"
            "Cuenta con un amplio catálogo de opciones que le permitirá registrar a los estudiantes que usted desee.\n"
            "Además, será capaz de observar un listado con la información de cada estudiante registrado.\n"
            "Esta aplicación esta dedicada (por ahora) únicamente para uso del personal educativo de la universidad\nJaveriana Cali.")
        st.write("")
        st.write("")
    col3, col4 = st.columns([3,6])
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.image(img2, width=400)
    with col4:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.header("Instrucciones:")
        st.write("")
        st.subheader("A continuación podrá observar las opciones que puedes elegir en la aplicacion, cada una de esta depende de tu labor")
        st.write("")
        st.text("La aplicación cuenta con diferentes opciones:\n")
        st.text("1. Identificate\n")
        st.text("2. Agrega una evaluación (Asistente)\n")
        st.text("3. Histórico (Asistente o Directora)\n")
        st.text("4. Listar Criterios (Directora)\n")
        st.text("5. Crear Criterios (Directora)\n")
        st.text("6. Califica un Proyecto (Jurado)\n")




