import bcrypt

class Login:
    def __init__(self, user):
        self.user = user  

    def verificar_credenciales(self, email, contrasenaLogin):
        usuario = next((u for u in self.user if u[3] == email), None)

        if usuario:
            hashed_password = usuario[4]  

            # Asegurar que hashed_password está en bytes
            if isinstance(hashed_password, str):
                hashed_password = hashed_password.encode('utf-8')

            # Comparar la contraseña ingresada con la almacenada
            if bcrypt.checkpw(contrasenaLogin.encode("utf-8"), hashed_password):
                return True
        
        return False
