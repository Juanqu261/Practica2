from estructuras import DoubleList, Stack, Queue
from modelos import Usuario, Mensaje
from archivos import *
from datetime import datetime

# ------------------------------ Manejo de usuarios ------------------------------ #

def cargar_usuarios(diccionario_datos: dict, credenciales: dict) -> DoubleList:
    """
    ### Summary:
        Crea una lista de usuarios(objetos) existentes en el sistema
    ### Args:
        diccionario (dict): Diccionario con los datos de los usuarios
        credenciales (dict): Diccionario con las contraseñas y cargos de los usuarios
    ### Returns:
        lista_usuarios_cargados (DoubleList): Usuarios creados
    """
    lista_usuarios_cargados = DoubleList()
    for id in diccionario_datos:
        datos = diccionario_datos[id]
        datos2 = credenciales[id]
        usuario = Usuario(
            cedula=datos["cedula"],
            nombre=datos["nombre"],
            fecha_nacimiento=datos["fecha_de_nacimiento"],
            ciudad=datos["ciudad"],
            celular=datos["celular"],
            email=datos["email"],
            direccion=datos["direccion"],
            contrasena=datos2["password"],
            cargo=datos2["cargo"],
        )
        lista_usuarios_cargados.add_last(usuario)
    return lista_usuarios_cargados


def login(lista: DoubleList) -> Usuario:
    """
    ### Summary:
        Inicia sesión con inputs del usuario para la Cédula y la Contraseña.
    ### Args:
        lista (DoubleList): Lista los usuarios existentes
    ### Returns:
        user (Usuario):
    """

    logged_in = False

    # Repetir solicitudes de input si los datos no son válidos
    while (not logged_in):

        # Recibir credenciales
        print("\nIngrese su Cédula:")
        id = input()
        print("\nIngrese su Contraseña:")
        password = input()

        # Recorrer la lista buscando al usuario
        temp = lista.get_first()

        for i in range(lista.get_size()):
            if (temp.get_data().get_cedula() == id
                    and temp.get_data().get_contrasena() == password):
                cargo = temp.get_data().get_cargo()
                print(f"\n¡Hola, {temp.get_data().nombre}! ({cargo})")
                return temp.get_data()
            
            else:
                temp = temp.get_next()
        
        print("\n*Error en la Cédula o Contraseña ingresadas. Por favor inténtelo de nuevo.")
        logged_in = False

# Admin
def crear_usuario(lista: DoubleList):
    """
    ### Summary:
        Añade un nuevo usuario con los datos indicados a la lista de usuarios creada
        en main.
    ### Args:
        lista (DoubleList): Lista de usuarios en el sistema
    """

    print("\n\nIndique la cedula del nuevo empleado: ")
    cedula = input()
    print("\nIndique el nombre del nuevo empleado: ")
    nombre = input()
    print("\nIndique la fecha de nacimiento del nuevo empleado: ")
    fecha_nac = input()
    print("\nIndique la ciudad de nacimiento del nuevo empleado: ")
    ciudad = input()
    print("\nIndique el celular del nuevo empleado: ")
    celular = input()
    print("\nIndique email del nuevo empleado: ")
    email = input()
    print("\nIndique la direccion del nuevo empleado: ")
    direccion = input()
    print("\nIndique la contraseña del nuevo empleado: ")
    contrasena = input()
    print("\nIndique el cargo del nuevo empleado: ")
    cargo = input()

    user = Usuario(
        cedula, nombre, fecha_nac, ciudad, celular, email, direccion,
        contrasena, cargo
    )
    lista.add_last(user)
    print("\n\nUsuario creado con exito.")

# Admin
def cambiar_contrasena(lista: DoubleList):
    print("\n\nIndique la cedula del empleado: ")
    cedula = input()

    temp = lista.get_first()
    for i in range(lista.get_size()):
        if temp.get_data().cedula == cedula:
            print("\nIngrese nueva contrasena: ")
            contrasena = input()
            temp.get_data().set_contrasena(contrasena)
            print("\nContraseña actualizada con exito.")
            break
        temp = temp.get_next()

# Admin
def eliminar_usuario(lista: DoubleList):
    print("\n\nIndique la cedula del empleado: ")
    cedula = input()

    temp = lista.get_first()
    for i in range(lista.get_size()):
        if temp.get_data().cedula == cedula:
            print('\nPara confirmar la eliminacion, digite "SI" :')
            validacion = input()
            if validacion == "SI":
                lista.remove(temp)
                print("\nUsuario eliminado con exito.")
            break
        temp = temp.get_next()

# ------------------------------ Manejo de mensajes ------------------------------ #
# Hacer this
def ver_bandeja_secuencial():
    pass

# INCOMPLETA
def enviar_mensaje(remitente):
    remitente = remitente
    destinatario = input("Ingrese la cedula del destinatario:\n")
    fecha = datetime.now().strftime("%Y/%m/%d")
    hora = datetime.now().strftime("%H:%M:%S")
    asunto = input("Ingrese el asunto del mensaje:\n")
    cuerpo = input("Ingrese el mensaje:\n")
    mensaje = Mensaje(
        remitente=remitente,
        destinatario=destinatario,
        fecha=fecha,
        hora=hora,
        asunto=asunto,
        cuerpo=cuerpo,
    )

    print(
        "Opciones:\n\
            1. Guardar borrador\n\
            2. Enviar mensaje\n\
            3. Descartar\n"
    )

    while True:
        opcion = input()
        if opcion == "1":
            print("Borrador")
            break
        elif opcion == "2":
            print("Enviar mensaje")
            break
        elif opcion == "3":
            print("Mensaje descartado")
            break
        else:
            print("Opcion invalida")
            break


def generar_bandejas(mensajes: dict, cedula: str, usuarios: DoubleList) -> DoubleList:
    """
    ### Summary:
        Crea y retorna a partir de diccionarios las estructuras de datos
        con los 3 tipos de mensajes almacenados en el sistema por el
        usuario con la cédula indicada.
    
    ### Args:
        mensajes (dict): Diccionario con todos los mensajes del sistema
        cedula (str): ID del usuario que consulta los mensajes
        usuarios (DoubleList): Lista de todos los usuarios en el sistema
    
    ### Returns:
        ba (DoubleList): Bandeja de Entrada,
        ml (DoubleList): Mensajes Leídos,
        b (DoubleList): Borradores
    """
    
    # Inicialización
    # Bandeja de Entrada
    ba = DoubleList()

    # Mensajes Leídos
    ml = Queue()

    # Borradores
    b = Stack()

    # Obtener los mensajes y añadirlos a su bandeja correspondiente
    for msg in mensajes[cedula]:
        mensaje = mensajes[cedula][msg]
        bandeja = mensaje["tipo"]

        # Búsqueda del nombre del remitente
        # remitente = ""
        temp = usuarios.get_first()
        while (temp.get_next() != None):
            if (temp.get_data().get_cedula() == mensaje["remitente"]):
                remitente = temp.get_data().get_nombre()
                break
            temp = temp.get_next()

        mensaje = Mensaje(
            cedula,
            bandeja,
            remitente,
            mensaje["fecha"],
            mensaje["hora"],
            mensaje["asunto"],
            mensaje["cuerpo"],
        )

        match bandeja:
            case "BA":
                ba.add_last(mensaje)
            case "ML":
                ml.enqueue(mensaje)
            case "B":
                b.push(mensaje)
        
    return ba, ml, b


def ver_bandeja(id: str, ba: DoubleList, ml: Queue):
    """
    ### Summary:
        Devuelve formato estilizado de los mensajes del tipo de Bandeja indicado
    
    ### Args:
        ID: ID del usuario que consulta los mensajes
        BA: Estructura con el tipo de mensajes que quiere consultar
        el usuario
    """

    if (ba.is_empty()):
        print("\nNo tiene mensajes nuevos para leer.")
    else:
        print("\n    BANDEJA DE ENTRADA\n\n" + 50 * "-")

        # Obtención de la bandeja
        temp = ba.get_first()
        i = 1
        while temp != None:
            if temp.get_data().get_destinatario() == id:
                mensaje = temp.get_data()
                print(
                    f"\
            {mensaje.get_fecha()}\n\
        {'%02d'%i}    Asunto: {mensaje.get_asunto()}\n\
            {mensaje.get_remitente()}"
                )

                print(50 * "-")
            temp = temp.get_next()
            i += 1
        
        # Indicar qué mensaje ver
        print("\n¿Qué mensaje desea ver? (indique su numeral)")
        inx = int(input())
        temp = ba.get_first()
        for k in range(inx - 1):
            temp = temp.get_next()
        
        # Mostrar el mensaje en pantalla
        mensaje = temp.get_data()
        print(mensaje)

        # Pasar de Bandeja a Leídos
        ba.remove(temp)
        ml.enqueue(mensaje)

        print(
            "Opciones:\n\n\
    1 - Volver a Bandeja\n\
    2 - Cerrar Sesión\n"
        )

        match input():
            case "1":
                ver_bandeja(id, ba)
            case "2":
                pass


def ver_leidos(id: str, ml: Queue):
    if (ml.is_empty()):
        print("\nNo has leído ningún mensaje.")
    else:
        print("\n   MENSAJES LEÍDOS\n")
        print("Mensaje leído más antiguo:\n")
        print(ml.first())

        print("¿Qué deseas hacer?\n\n\
    1 - Ver Siguiente Mensaje Leído\n\
    2 - Cerrar Sesión\n")
        match input():
            case "1":
                ml.dequeue()
                ver_leidos(id, ml)
            case "2":
                pass


def ver_borradores(id: str, b: Stack):
    if (b.is_empty()):
        print("\nNo tienes borradores guardados.")
    else:
        print("\n    BORRADORES\n")
        print("Borrador más reciente:\n")
        print(b.top())
        print(
            "¿Qué deseas hacer con este borrador?\n\n\
    1 - Enviar (FALTA)\n\
    2 - Descartar\n\
    3 - Cerrar Sesión\n"
        )
        
        match input():
            case "1":
                # Enviar Mensaje
                ver_borradores(id, b)
            case "2":
                b.pop()
                ver_borradores(id, b)
            case "3":
                pass


def guardar_cambios(lista: DoubleList):
    """
    ### Summary:
        Guarda todos los cambios en las estructuras de datos
        al correr main, y los devuelve en diccionarios.
    ### Args:
        lista (DoubleList): Lista de usuarios en el sistema
        (con cambios aplicados)
    ### Returns:
        dict_empleados, dict_password"""
    
    dict_empleados = {}
    dict_password = {}

    temp = lista.get_first()
    while (temp != None):
        # Obtener objeto Usuario
        usuario = temp.get_data()

        # Obtener datos del usuario
        cedula = usuario.get_cedula()
        nombre = usuario.get_nombre()
        fecha = usuario.get_fecha_nacimiento()
        ciudad = usuario.get_ciudad()
        celular = usuario.get_celular()
        email = usuario.get_email()
        direccion = usuario.get_direccion()
        contrasena = usuario.get_contrasena()
        cargo = usuario.get_cargo()

        # Generar diccionario para empleados.json
        dict_empleados[cedula] = {
            "cedula":cedula,
            "nombre":nombre,
            "fecha_de_nacimiento":fecha,
            "ciudad":ciudad,
            "celular":celular,
            "email":email,
            "direccion":direccion
        }

        # Generar diccionario para password.json
        dict_password[cedula] = {
            "password":contrasena,
            "cargo":cargo
        }
        
        temp = temp.get_next()
    
    return dict_empleados, dict_password


def guardar_mensajes(lista: DoubleList):
    pass
