from cls.register import Register
import streamlit as st

st.set_page_config(page_title="UnrandomProy", layout="wide")

# Menú lateral
st.sidebar.title("Menú")
if st.sidebar.button("Registro de Usuario"):
    st.session_state.mostrar_formulario = True

# Verifica si el formulario debe mostrarse
if "mostrar_formulario" not in st.session_state:
    st.session_state.mostrar_formulario = False

if st.session_state.mostrar_formulario:
    st.title("Formulario de Registro")
    
    with st.container():
        id_usuario = st.text_input("ID")
        nombre = st.text_input("Primer Nombre")
        apellido = st.text_input("Primer Apellido")
        email = st.text_input("Email")
        contrasena = st.text_input("Contraseña", type="password")
        passwordEncoded = contrasena.encode('utf-8')

        formRegister = Register(id_usuario, nombre, apellido, email, passwordEncoded)
        if st.button("Registrar"):
            formRegister.user_register()