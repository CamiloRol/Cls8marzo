import bcrypt

user = []

class Register:
    def __init__(self, user):
        self.user = user
        self.register = self.user_register()

    def user_register():

        id = int(input("Ingrese su numero de documento de identidad"))
        user.append(id)
        name = input("Ingrese su primer nombre")
        user.append(name)
        last_name = input("Ingrese su primer apellido")
        user.append(last_name)
        email = input("Ingrese su correo electronico")
        user.append(email)
        password = input("Ingrese un contraseña minimo 8 caracteres entre numeros y letras con un caracter especial")
        user.append(password)
        print("Usuario creado exitosamente")
        print(user)

    def encryptPassword():
        pass
