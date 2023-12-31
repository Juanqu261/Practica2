import estructuras
import archivos
import acciones
import modelos

# ------------------------------ Lectura de Archivos ------------------------------ #

# Obtener Datos de los Empleados
dict_empleados = archivos.leer_json("empleados.json")

# Obtener las Contraseñas y Cargos
dict_credenciales = archivos.leer_json("password.json")

# Extraer la información de los diccionarios en una DoubleList
lista_usuarios = acciones.cargar_usuarios(dict_empleados, dict_credenciales)


# Obtener Mensajes
dict_mensajes = archivos.leer_json("mensajes.json")

# ----------------------------------- Interfaz ----------------------------------- #

print("\n¡Bienvenido/a al Sistema de Mensajería!")

# Inicio de Sesión del usuario
user = acciones.login(lista_usuarios)

# Generación de las estructuras de datos con los mensajes
# BA: DoubleList, ML: Queue, B: Stack

temp = lista_usuarios.get_first()
while temp != None:
    data = temp.get_data()
    ba, ml, b = acciones.generar_bandejas(
        mensajes=dict_mensajes, cedula=data.get_cedula(), usuarios=lista_usuarios
    )
    data.set_bandejas(ba, ml, b)
    temp = temp.get_next()


# Mostrar Acciones que puede hacer el usuario
print(
    "Acciones:\n\n\
    0 - Salir\n\
    1 - Enviar Mensaje\n\
    2 - Ver Bandeja de Entrada\n\
    3 - Ver Mensajes Leídos\n\
    4 - Ver Borradores"
)

if user.es_admin():
    print(
        "\
    5 - Crear usuario \n\
    6 - Cambiar contraseña de un empleado\n\
    7 - Eliminar empleado\n\
    0 - Salir"
    )

print("\nIndique el número de la acción que desea realizar:")

# Realizar Acción escogida
match input():
    # Salir
    case "0":
        pass

    # Enviar Mensaje
    case "1":
        acciones.crear_mensaje(
            remitente=user, mensajes=dict_mensajes, usuarios=lista_usuarios
        )

    # Ver Bandeja de Entrada
    case "2":
        acciones.ver_bandeja(user.get_cedula(), user.ba, user.ml)

    # Ver Mensajes Leídos
    case "3":
        acciones.ver_leidos(user.get_cedula(), user.ml)

    # Ver Borradores
    case "4":
        acciones.ver_borradores(user.get_cedula(), user.b, lista_usuarios)

    # Crear Usuario
    case "5":
        if user.es_admin():
            acciones.crear_usuario(lista_usuarios)
        else:
            print("\nFunción fuera de alcance")

    # Cambiar Contraseña de un empleado
    case "6":
        if user.es_admin():
            acciones.cambiar_contrasena(lista_usuarios)
        else:
            print("\nFunción fuera de alcance")

    # Eliminar empleado
    case "7":
        if user.es_admin():
            acciones.eliminar_usuario(lista_usuarios)
        else:
            print("\nFunción fuera de alcance")

# ----------------------------- Guardado en Archivos ----------------------------- #

# Guardar los cambios a las estructuras en diccionarios
empleados, password, mensajes = acciones.guardar_cambios(lista_usuarios)

# Guardar los diccionarios en los archivos json
archivos.guardar_json("empleados.json", empleados)
archivos.guardar_json("password.json", password)

# mensajes.json
archivos.guardar_json("mensajes.json", mensajes)
