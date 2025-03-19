from cls.register import Register
import streamlit as st
from cls.login import Login


st.set_page_config(page_title="UnrandomProy", layout="wide")

st.markdown(
    """
    <style>
        .centered-text {
            text-align: center;
        }
        .sidebar-buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .stButton>button {
            width: 100%;
            background-color: gray;
            color: white;
            border-radius: 10px;
            padding: 10px;
        }
        .stTextInput>div>div>input {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if "user" not in st.session_state:
    st.session_state["user"] = []

# Menú lateral
st.sidebar.markdown("<h2 class='centered-text'>Menú</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-buttons'>", unsafe_allow_html=True)
if st.sidebar.button("Registro de Usuario"):
    st.session_state["mostrar_formulario"] = "registro"
if st.sidebar.button("Login"):
    st.session_state["mostrar_formulario"] = "login"
st.sidebar.markdown("</div>", unsafe_allow_html=True)

# Verifica si el formulario debe mostrarse
if "mostrar_formulario" not in st.session_state:
    st.session_state["mostrar_formulario"] = None
if "mostrar_alerta" not in st.session_state:
    st.session_state["mostrar_alerta"] = False
if "form_data" not in st.session_state:
    st.session_state.form_data = {
        "id_usuario": "",
        "nombre": "",
        "apellido": "",
        "email": "",
        "contrasena": ""
    }

if st.session_state["mostrar_formulario"] == "registro":
    st.markdown("<h2 class='centered-text'>Registrate</h2>", unsafe_allow_html=True)
    
    with st.container():
        form_data = st.session_state.form_data
        id_usuario = st.text_input("ID", value=form_data["id_usuario"], key="id_usuario")
        nombre = st.text_input("Primer Nombre", value=form_data["nombre"], key="nombre")
        apellido = st.text_input("Primer Apellido", value=form_data["apellido"], key="apellido")
        email = st.text_input("Email", value=form_data["email"], key="email")
        contrasena = st.text_input("Contraseña", type="password", value=form_data["contrasena"], key="contrasena")
    
        passwordEncoded = contrasena.encode('utf-8')

        
        formRegister = Register(id_usuario, nombre, apellido, email, passwordEncoded, st.session_state["user"])
        if st.button("Registrar"):
            formRegister.user_register()
            st.session_state.form_data = {  # Limpia el formulario después del registro
            "id_usuario": "",
            "nombre": "",
            "apellido": "",
            "email": "",
            "contrasena": ""
            }
            st.session_state["mostrar_alerta"] = True
            

if st.session_state["mostrar_alerta"]:
    st.balloons()
    st.success("🎉 ¡Felicitaciones! Te acabas de registrar exitosamente.")
    st.session_state["mostrar_alerta"] = False

elif st.session_state["mostrar_formulario"] == "login":
    st.markdown("<h2 class='centered-text'>Inicio de Sesion</h2>", unsafe_allow_html=True)
    emailLogin = st.text_input("Email")
    contrasenaLogin = st.text_input("Contraseña", type="password")

    if st.button("Enviar"):
        loginAuth = Login(st.session_state["user"])
        if loginAuth.verificar_credenciales(emailLogin, contrasenaLogin):
            st.success("El login ha sido exitoso cargando...")
        else:
            st.error("Datos incorrectos")