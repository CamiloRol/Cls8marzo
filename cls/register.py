import bcrypt


class Register:
    def __init__(self, id_usuario, nombre, apellido, email, passwordEncoded):
        self.id = id_usuario
        self.name = nombre
        self.last_name =  apellido
        self.email =  email
        self.password = passwordEncoded
        self.user = []

    def user_register(self):
        self.user.append(self.id)
        self.user.append(self.name)
        self.user.append(self.last_name)
        self.user.append(self.email)
        self.encryptPassword()
        print("Usuario creado exitosamente")
        print(self.user)

    def encryptPassword(self):
        salt = bcrypt.gensalt()
        hashedPass = bcrypt.hashpw(self.password, salt)
        self.user.append(hashedPass)
