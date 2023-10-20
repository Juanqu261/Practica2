import acciones

# ------------------------------ Lectura de Archivos ------------------------------ #

# Obtener Datos de los Empleados
empleados = acciones.leer_json("empleados.json")

# Obtener las Contraseñas y Cargos
password = acciones.leer_json("password.json")

# Obtener Mensajes
mensajes = acciones.leer_json("mensajes.json")

# Extraer la información de los diccionarios en una DoubleList
lista_usuarios = acciones.cargar_datos(empleados, password, mensajes)

# ----------------------------------- Interfaz ----------------------------------- #

print("\n¡Bienvenido/a al Sistema de Mensajería!")

# Inicio de Sesión del usuario
usuario = acciones.login(lista_usuarios)

# Mostrar Acciones que puede hacer el usuario
print(
    "Acciones:\n\n\
    0 - Salir\n\
    1 - Enviar Mensaje\n\
    2 - Ver Bandeja de Entrada\n\
    3 - Ver Mensajes Leídos\n\
    4 - Ver Borradores"
)

if (usuario.es_admin()):
    print(
        "\
    5 - Crear usuario \n\
    6 - Cambiar contraseña de un empleado\n\
    7 - Eliminar empleado"
    )

print("\nIndique el número de la acción que desea realizar:")

# Realizar Acción escogida
match input():
    # Salir
    case "0":
        pass

    # Enviar Mensaje
    case "1":
        acciones.crear_mensaje(usuario, lista_usuarios)

    # Ver Bandeja de Entrada
    case "2":
        acciones.ver_bandeja(usuario)

    # Ver Mensajes Leídos
    case "3":
        acciones.ver_leidos(usuario)

    # Ver Borradores
    case "4":
        acciones.ver_borradores(usuario)

    # Crear Usuario
    case "5":
        if (usuario.es_admin()):
            acciones.crear_usuario(lista_usuarios)

    # Cambiar Contraseña de un empleado
    case "6":
        if (usuario.es_admin()):
            acciones.cambiar_contrasena(lista_usuarios)

    # Eliminar empleado
    case "7":
        if (usuario.es_admin()):
            acciones.eliminar_usuario(lista_usuarios)

print("\nFIN DE LA SESIÓN\n")

# ----------------------------- Guardado en Archivos ----------------------------- #

# Guardar los cambios a las estructuras en diccionarios
empleados, password, mensajes = acciones.guardar_datos(lista_usuarios)

# Guardar los diccionarios en los archivos JSON
acciones.guardar_json("empleados.json", empleados)
acciones.guardar_json("password.json", password)
acciones.guardar_json("mensajes.json", mensajes)
