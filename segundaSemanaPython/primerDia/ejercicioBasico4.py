#VERIFICA SI EL NOMBRE DE USUARIO Y LA CONTRASEÑA SON VÁLIDAS
nombreUsuarioCorrecto = "Daniel"
contraseniaCorrecta = "1111"


nombreUsuario = (input("Intoduzca su nombre de usuario: "))
if nombreUsuario == nombreUsuarioCorrecto:

    contrasenia = (input("Intoduzca su contraseña: "))
    if contrasenia == contraseniaCorrecta:
        print("Credenciales válidas")

    else:
        print("Contraseña incorrecta")

else:
    print("Nombre de usuario incorrecto")    