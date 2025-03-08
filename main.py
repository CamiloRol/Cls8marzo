from cls.register import Register

id = int(input("Ingrese su numero de documento de identidad: "))
name = input("Ingrese su primer nombre: ")
last_name = input("Ingrese su primer apellido: ")
email = input("Ingrese su correo electronico: ")
password = input("Ingrese un contraseña minimo 8 caracteres entre numeros y letras con un caracter especial: ")

passwordEncoded = password.encode('utf-8')

formRegister = Register(id, name, last_name, email, passwordEncoded)
formRegister.user_register()