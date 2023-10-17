import estructuras
import archivos
import acciones
import modelos

# ------------------------------ Lectura de Archivos ------------------------------ #

# Obtener datos de los Empleados
dict_empleados = archivos.leer_json("empleados.json")

# Obtener las Contraseñas y cargos
dict_credenciales = archivos.leer_json("password.json")

# Extraer la información de los diccionarios en una DoubleList
lista_usuarios = archivos.cargar_usuarios(dict_empleados, dict_credenciales)

# Obtener Mensajes
dict_mensajes = archivos.leer_json("mensajes.json")

# ------------------------------ Interfaz ------------------------------ #

print("Bienvenido/a al Sistema de Mensajería")

# Inicio de Sesión del usuario
user = acciones.login(lista_usuarios)

# "Menú"
print(
    "Acciones:\n\n\
    1 - Enviar Mensaje\n\
    2 - Ver Bandeja de entrada\n\
    3 - Ver Bandeja de leidos\n\
    4 - Ver Borradores \n\
    5 - Pendiente \n\
    6 - Cambiar contraseña de un empleado\n\
    7 - Eliminar empleado\n\
    0 - Salir\n\n\
Indique el número de la acción que desea realizar:\n"
)

# Realizar acción escogida
match input():
    case "1":
        acciones.enviar_mensaje(remitente=user.get_cedula())
    case "2":
        ba = acciones.bandeja_entrada(
            mensajes=dict_mensajes, cedula=user.get_cedula(), usuarios=lista_usuarios
        )
        acciones.ver_bandeja(user.get_cedula(), ba)
    case "3":
        ml = acciones.mensajes_leidos(
            mensajes=dict_mensajes, cedula=cedula, usuarios=lista_usuarios
        )
        acciones.ver_bandeja(user.get_cedula(), ml)
    case "4":
        b = acciones.bandeja_borradores(
            mensajes=dict_mensajes, cedula=cedula, usuarios=lista_usuarios
        )
        acciones.ver_bandeja(user.get_cedula(), b)
    case "5":
        pass
    case "6":
        acciones.cambiar_contrasena(lista_usuarios)
    case "7":
        acciones.eliminar_usuario(lista_usuarios)
    case "0":
        quit()
