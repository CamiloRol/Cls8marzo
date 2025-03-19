import bcrypt

class Register:
    def __init__(self, id_usuario, nombre, apellido, email, passwordEncoded, user):
        self.id = id_usuario
        self.name = nombre
        self.last_name = apellido
        self.email = email
        self.password = passwordEncoded  # Se pasa la contraseña en texto plano
        self.user = user

    def user_register(self):
       
        hashed_password = bcrypt.hashpw(self.password, bcrypt.gensalt())

        self.user.append([self.id, self.name, self.last_name, self.email, hashed_password])

        print("✅ Usuario creado exitosamente")
        print(self.user) 

