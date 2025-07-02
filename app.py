from funciones.menu import main
import pwinput

def pedir_credenciales():
    try:
        with open("credenciales.txt", "r") as f:
            linea = f.readline().strip()
            usuario_correcto, contraseña_correcta = linea.split(",")
    except FileNotFoundError:
        print("Archivo de credenciales no encontrado.")
        return False

    intentos = 3
    while intentos > 0:
        usuario = input("Ingrese el usuario: ")
        contraseña = pwinput.pwinput("Ingrese la contraseña: ")

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("\nAcceso concedido.\n")
            return True
        else:
            intentos -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")

    print("Acceso denegado. Cerrando el programa.")
    return False


if pedir_credenciales():
    main()
