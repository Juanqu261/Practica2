import estructuras
import archivos
import acciones
import modelos
import algoritmos

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
ba, ml, b = acciones.generar_bandejas(
    mensajes=dict_mensajes,
    cedula=user.get_cedula(),
    usuarios=lista_usuarios
)

# Mostrar Acciones que puede hacer el usuario
print("Acciones:\n\n\
    0 - Salir\n\
    1 - Enviar Mensaje (FALTA)\n\
    2 - Ver Bandeja de Entrada\n\
        (Falla cuando hay 1 mensaje)\n\
    3 - Ver Mensajes Leídos\n\
    4 - Ver Borradores")

if (user.es_admin()):
    print("\
    5 - Crear usuario \n\
    6 - Cambiar contraseña de un empleado\n\
    7 - Eliminar empleado\n\
    0 - Salir")

print("\nIndique el número de la acción que desea realizar:")

# Realizar Acción escogida
match input():
    case "1":
        acciones.enviar_mensaje(remitente=user.get_cedula())
    
    case "2":
        acciones.ver_bandeja(user.get_cedula(), ba)

    case "3":
        acciones.ver_leidos(user.get_cedula(), ml)

    case "4":
        acciones.ver_borradores(user.get_cedula(), b)
    
    case "5":
        if (user.es_admin()):
            acciones.crear_usuario(lista_usuarios)
        else:
            print("\nFunción fuera de alcance")
    
    case "6":
        if (user.es_admin()):
            acciones.cambiar_contrasena(lista_usuarios)
        else:
            print("\nFunción fuera de alcance")
    
    case "7":
        if (user.es_admin()):
            acciones.eliminar_usuario(lista_usuarios)
        else:
            print("\nFunción fuera de alcance")
    
    case "0":
        quit()
