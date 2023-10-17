from estructuras import DoubleList
from modelos import Usuario, Mensaje
from archivos import *
from datetime import datetime


# ------------------------------ Manejo de usuarios ------------------------------ #
def crear_usuarios(diccionario_datos: dict, credenciales: dict) -> DoubleList:
    """
    [Summary]:
        Crea una lista de usuarios(objetos) existentes en el sistema
    [Args]:
        diccionario (dict): Diccionario con los datos de los usuarios
        credenciales (dict): Diccionario con las contraseñas y cargos de los usuarios
    [Returns]:
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


def login(lista: DoubleList) -> bool:
    """
    [Summary]:
        El usuario a ingresar existe en el sistema
    [Args]:
        id (str): id del usuario que desea acceder
        password (str): Contraseña del usuario que desea acceder
        lista (DoubleList): Lista Doble donde que almacena los usuarios existentes
    [Returns]:
        True : id y password se encuentran y coinciden con el usuario ubicado en lista
        False : id o password no se encuentran o no coinciden con el usuario ubicado en lista
    """
    logged_in = False
    id = 0
    while not logged_in:
        print("\nIngrese su Cédula:")
        id = input()
        if id == "x":
            return None
        print("\nIngrese su Contraseña:")
        password = input()
        if password == "x":
            return None

        temp = lista.get_first()
        for i in range(lista.get_size()):
            if temp.get_data().cedula == id:
                if temp.get_data().get_contrasena() == password:
                    cargo = temp.get_data().get_cargo()
                    print(f"\nHola, {temp.get_data().nombre} ({cargo})")
                    logged_in = True
                    return temp.get_data(), id, cargo
                else:
                    print("\nContraseña incorrecta. Por favor intentelo de nuevo.")
                    logged_in = False
            temp = temp.get_next()
        print("\nEl Usuario no existe. Por favor intentelo de nuevo.")
        logged_in = False


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


def ver_bandeja(id: str, ba: DoubleList()):
    """Extrae de la Bandeja de Entrada Global los mensajes
    dirigidos a un usuario específico.

    Incluye salida (prints) de la consola.
    """

    print("BANDEJA DE ENTRADA\n\n")

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
    if i == 1:
        print("No tienes mensajes nuevos para leer.")


def enviar_mensaje(remitente):
    remitente = remitente
    destinatario = input("Ingrese la cedula del destinatario:\n")
    fecha = datetime.now().strftime("%Y/%m/%d")
    hora = datetime.now().strftime("%Y/%m/%d")
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

    opcion = input(
        "Opciones:\n\
            1. Guardar borrador\n\
            2. Enviar mensaje\n\
            3. Descartar"
    )

    while True:
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


def bandeja_entrada(mensajes, cedula, usuarios) -> DoubleList:
    ba = DoubleList()

    for msg in mensajes[cedula]["BA"]:
        mensaje = mensajes[cedula]["BA"][msg]

        # Búsqueda del nombre del remitente
        remitente = ""
        temp = usuarios.get_first()
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
    return ba


# Cambiar de lista
def mensajes_leidos(mensajes, cedula, usuarios) -> DoubleList:
    ba = DoubleList()

    for msg in mensajes[cedula]["ML"]:
        mensaje = mensajes[cedula]["ML"][msg]

        # Búsqueda del nombre del remitente
        remitente = ""
        temp = usuarios.get_first()
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
    return ba


# Cambiar de lista
def bandeja_borradores(mensajes, cedula, usuarios) -> DoubleList:
    ba = DoubleList()

    for msg in mensajes[cedula]["B"]:
        mensaje = mensajes[cedula]["B"][msg]

        # Búsqueda del nombre del remitente
        remitente = ""
        temp = usuarios.get_first()
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
    return ba
