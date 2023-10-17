from estructuras import *
from archivos import *
from acciones import *
from modelos import *

# LECTURA DE ARCHIVOS

# Registro --> Cargamos los archivos .json en formato de diccionarios
empleados, credenciales = leer_json("empleados.json"), leer_json("password.json")

# Crear objetos usuario --> Creamos objetos que contengan la informacion de los diccionarios
lista_usuarios = crear_usuarios(empleados, credenciales)

# Mensajes
dict_mensajes = leer_json("mensajes.json")


# Login --> Para ingresar al sistema, los datos ingresados deben coincidir con los datos
#   De algun objeto(usuario) existente dentro de lista_usuarios.
print("Bienvenido al Sistema de Mensajería")

user, cedula = login(lista_usuarios)

# Si se omite el login
if user == None:
    quit()


print(
    "Acciones:\n\n\
    1 - Enviar Mensaje\n\
    2 - Ver Bandeja de entrada\n\
    3 - Ver Bandeja de leidos\n\
    4 - Ver Borradores \n\
    6 - Cambiar contraseña de un empleado\n\
    7 - Eliminar empleado\n\
    0 - Salir\n\n\
Indique el número de la acción que desea realizar:\n"
)

ba = DoubleList()

for msg in dict_mensajes[cedula]["BA"]:
    mensaje = dict_mensajes[cedula]["BA"][msg]

    # Búsqueda del nombre del remitente
    remitente = ""
    temp = lista_usuarios.get_first()
    while temp.get_next() != None:
        if temp.get_data().get_cedula() == mensaje["remitente"]:
            remitente = temp.get_data().get_nombre()
            break
        temp = temp.get_next()

    mensaje = Mensaje(
        remitente,
        cedula,
        mensaje["fecha"],
        mensaje["hora"],
        mensaje["asunto"],
        mensaje["cuerpo"],
    )
    ba.add_last(mensaje)


match input():
    case "1":
        enviar_mensaje(remitente=cedula)
    case "2":
        ver_bandeja(user.get_cedula(), ba)
    case "3":
        print("Not ready")
    case "4":
        print("Not ready")
    case "5":
        print("Not ready")
    case "6":
        cambiar_contrasena(lista_usuarios)
    case "7":
        eliminar_usuario(lista_usuarios)
    case "0":
        quit()
