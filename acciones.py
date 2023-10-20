"""Funciones de la secuencia de la consola"""

# JSON: Lectura y Escritura de archivos
# DATETIME: Establecer la fecha y hora de envío de los mensajes
from estructuras import *
from modelos import *
import json
from datetime import datetime

# ------------------------------ Manejo de Archivos ------------------------------ #

def leer_json(nombre_del_archivo: str) -> dict:
    """
    ## Summary:
        Lee el archivo json y lo retorna como un diccionario
    ## Args:
        - `nombre_del_archivo (str)`: Archivo del que se extrae el diccionario
    ## Returns:
        - `diccionario (dict)`: Diccionario con los datos del json
    """

    with open(nombre_del_archivo, "r") as file:
        diccionario = json.load(file)
    return diccionario


def guardar_json(nombre_del_archivo: int, guardar: any) -> None:
    """
    ## Summary:
        Sobreescribe el diccionario en un archivo json
    ## Args:
        - `nombre_del_archivo (str)`: Archivo donde se guarda el diccionario\n
        - `guardar (dict)`: Diccionario a guardar
    """
    with open(nombre_del_archivo, "w") as file:
        dicccionario = json.dumps(guardar, indent=4)
        file.write(dicccionario)


def cargar_datos(empleados: dict, password: dict, mensajes: dict) -> DoubleList:
    """
    ## Summary:
        Crea la colección de usuarios guardados en el sistema a partir de los
        diccionarios obtenidos de los archivos JSON
    ## Args:
        - `empleados (dict)`: Diccionario obtenido de `empleados.json`
        - `password (dict)`: Diccionario obtenido de `password.json`
        - `mensajes (dict)`: Diccionario obtenido de `mensajes.json`
    ## Returns:
        - `usuarios (DoubleList)`: Colección con los usuarios guardados en el sistema
    """

    # Generar la colección de usuarios a partir de los diccionarios EMPLEADOS y PASSWORD
    usuarios = DoubleList()
    for id in empleados:
        datos = empleados[id]
        datos2 = password[id]

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

        usuarios.add_last(usuario)
    
    # Hacer el mismo recorrido, esta vez para guardar los mensajes
    # (el mensaje puede tener como destinatario/remitente un usuario
    # que todavía no se ha obtenido si se incluye este proceso
    # en el primer ciclo)
    i = 0
    for id in empleados:
        datos = empleados[id]
        datos2 = password[id]

        temp = usuarios.get_first()
        k = 0
        while (k < i):
            temp = temp.get_next()
            k += 1
        usuario = temp.get_data()

        # Recorrer cada mensaje del usuario y guardarlo en su atributo tipo colección
        # de mensajes correspondiente
        for msg in mensajes[id]:
            mensaje_dict = mensajes[id][msg]

            # Encontrar objeto Usuario del remitente usando su cédula
            temp_rem = usuarios.get_first()
            while (temp_rem.get_data().get_cedula()
                   != mensaje_dict["remitente"]):
                temp_rem = temp_rem.get_next()
            
            # Encontrar objeto Usuario del destinatario usando su cédula
            temp_dest = usuarios.get_first()
            while (temp_dest.get_data().get_cedula()
                   != mensaje_dict["destinatario"]):
                temp_dest = temp_dest.get_next()
            
            mensaje = Mensaje(
                destinatario=temp_dest.get_data(),
                tipo=mensaje_dict["tipo"],
                remitente=temp_rem.get_data(),
                fecha=mensaje_dict["fecha"],
                hora=mensaje_dict["hora"],
                asunto=mensaje_dict["asunto"],
                cuerpo=mensaje_dict["cuerpo"]
            )

            match mensaje_dict["tipo"]:
                case "BA":
                    usuario.get_ba().add_last(mensaje)
                case "ML":
                    usuario.get_ml().enqueue(mensaje)
                case "B":
                    usuario.get_b().push(mensaje)
        
        i += 1
    
    return usuarios


def guardar_datos(lista: DoubleList):
    """
    ## Summary:
        Recorre la colección de usuarios guardados en el sistema (después de
        los cambios realizados al correr `main.py`) y devuelve diccionarios
        con la información actualizada de los usuarios y sus colecciones
        de mensajes
    ## Args:
        - `lista (DoubleList)`: Lista de usuarios en el sistema
        (con cambios aplicados)
    ## Returns:
        - `empleados (dict)`
        - `password (dict)`
        - `mensajes (dict)`
    """

    # Crear los diccionarios a guardar en los archivos JSON
    empleados = {}
    password = {}
    mensajes = {}

    # Recorrer la lista de usuarios para guardar los cambios
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

        # Generar diccionario para EMPLEADOS.JSON
        empleados[cedula] = {
            "cedula": cedula,
            "nombre": nombre,
            "fecha_de_nacimiento": fecha,
            "ciudad": ciudad,
            "celular": celular,
            "email": email,
            "direccion": direccion,
        }

        # Generar diccionario para PASSWORD.JSON
        password[cedula] = {
            "password": contrasena,
            "cargo": cargo
        }

        # Generar diccionario para MENSAJES.JSON
        mensajes[cedula] = {}
        ba_nuevo = usuario.get_ba()
        ml_nuevo = usuario.get_ml()
        b_nuevo = usuario.get_b()
        
        # Actualizar la coleción BANDEJA DE ENTRADA
        temp_ba = ba_nuevo.get_first()
        while (temp_ba != None):
            mensaje = temp_ba.get_data()
            mensajes[cedula][f"{mensaje.get_fecha()} {mensaje.get_hora()}"] = {
                "destinatario": mensaje.get_destinatario().get_cedula(),
                "tipo": mensaje.get_tipo(),
                "remitente": mensaje.get_remitente().get_cedula(),
                "fecha": mensaje.get_fecha(),
                "hora": mensaje.get_hora(),
                "asunto": mensaje.get_asunto(),
                "cuerpo": mensaje.get_cuerpo()
            }

            temp_ba = temp_ba.get_next()
        
        # Actualizar la colección MENSAJES LEÍDOS
        temp_ml = ml_nuevo.first()
        while (not ml_nuevo.is_empty()):
            temp_ml = ml_nuevo.dequeue()
            mensaje = temp_ml
            mensajes[cedula][f"{mensaje.get_fecha()} {mensaje.get_hora()}"] = {
                "destinatario": mensaje.get_destinatario().get_cedula(),
                "tipo": mensaje.get_tipo(),
                "remitente": mensaje.get_remitente().get_cedula(),
                "fecha": mensaje.get_fecha(),
                "hora": mensaje.get_hora(),
                "asunto": mensaje.get_asunto(),
                "cuerpo": mensaje.get_cuerpo()
            }
        
        # Actualizar la colección BORRADORES
        temp_b = b_nuevo.top()
        while (not b_nuevo.is_empty()):
            temp_b = b_nuevo.pop()
            mensaje = temp_b
            mensajes[cedula][f"{mensaje.get_fecha()} {mensaje.get_hora()}"] = {
                "destinatario": mensaje.get_destinatario().get_cedula(),
                "tipo": mensaje.get_tipo(),
                "remitente": mensaje.get_remitente().get_cedula(),
                "fecha": mensaje.get_fecha(),
                "hora": mensaje.get_hora(),
                "asunto": mensaje.get_asunto(),
                "cuerpo": mensaje.get_cuerpo()
            }

        temp = temp.get_next()

    return empleados, password, mensajes

# ------------------------------ Acciones de Usuario ------------------------------ #

def login(lista: DoubleList) -> Usuario:
    """
    ## Summary:
        Inicia sesión con inputs del usuario para la Cédula y la Contraseña.
    ## Args:
        - `lista (DoubleList)`: Lista los usuarios existentes
    ## Returns:
        - `user (Usuario)`:
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
            if (
                temp.get_data().get_cedula() == id
                and temp.get_data().get_contrasena() == password
            ):
                cargo = temp.get_data().get_cargo()
                print(f"\n¡Hola, {temp.get_data().nombre}! ({cargo})")
                return temp.get_data()

            else:
                temp = temp.get_next()

        print(
            "\n*Error en la Cédula o Contraseña ingresadas. Por favor inténtelo de nuevo."
        )
        logged_in = False


def crear_mensaje(remitente: Usuario, usuarios: DoubleList):
    """
    ## Summary
        Para crear un nuevo mensaje desde 0. Incluye el proceso de
        guardar/enviar/descartar el mensaje, con sus respectivos cambios en
        las bandejas.

        Para enviar el mensaje, hace uso la función `enviar_mensaje()`.
    ## Args
        - `remitente (Usuario)`: Persona que envía el mensaje
        - `usuarios (DoubleList)`: Colección con los usuarios guardados en el sistema
    """

    # Obtener información del nuevo mensaje
    asunto = input("\nIngrese el asunto del mensaje:\n")
    cuerpo = input("\nIngrese el contenido del mensaje:\n")

    # Buscar al usuario destinatario en la colección usando su Cédula
    destinatario_ced = input("\nIngrese la cédula del destinatario:\n")
    temp = usuarios.get_first()
    while (temp.get_data().get_cedula() != destinatario_ced):
        temp = temp.get_next()
    destinatario: Usuario = temp.get_data()

    # Fecha y Hora no se definen hasta el envío (línea 367)
    fecha = datetime.now().strftime("%Y/%m/%d")
    hora = datetime.now().strftime("%H:%M:%S")

    # Crear instancia de Mensaje con los datos obtenidos
    mensaje = Mensaje(
        remitente = remitente,
        tipo = "",
        destinatario = destinatario,
        fecha = fecha,
        hora = hora,
        asunto = asunto,
        cuerpo = cuerpo,
    )

    # Mostrar las posibles acciones
    print(
        "\nOpciones:\n\n\
    1 - Guardar borrador\n\
    2 - Enviar mensaje\n\
    3 - Descartar\n"
    )

    # Realizar la acción escogida
    match input():
        # "Guardar borrador": Se guarda el mensaje en el atributo borrador del remitente
        case "1":
            mensaje.set_tipo("B")
            remitente.get_b().push(mensaje)
            print("Mensaje guardado en borradores.")
        
        # "Enviar mensaje": Llamar al método enviar_mensaje()
        case "2":
            mensaje.set_tipo("BA")
            enviar_mensaje(mensaje)
            print("Mensaje enviado con éxito.")

        # "Descartar": No se hace nada con el mensaje.
        case "3":
            print("Mensaje descartado.")


def enviar_mensaje(mensaje: Mensaje):
    """
    ## Summary
        Para "enviar" el mensaje indicado (el objeto mensaje contiene al remitente
        y destinatario).

        Si el mensaje estaba guardado como borrador, lo remueve de el atributo de
        borradores del remitente y lo almacena el atributo de bandeja de entrada del
        destinatario.
    ## Args
        - `mensaje (Mensaje)`
    """

    destinatario = mensaje.get_destinatario()

    # Establecer fecha y hora de envío, y tipo del mensaje
    mensaje.set_tipo("BA")
    mensaje.set_fecha(datetime.now().strftime("%Y/%m/%d"))
    mensaje.set_hora(datetime.now().strftime("%H:%M:%S"))

    destinatario.ba.add_first(mensaje)


def ver_bandeja(usuario: Usuario):
    """
    ## Summary:
        Muestra completamente la colección Bandeja de Entrada del usuario,
        permite ver un mensaje en particular de la misma, y mueve los mensajes
        vistos a la colección de Mensajes Leídos del usuario
    ## Args:
        - `usuario (Usuario)`
    """

    # Obtener las colecciones BANDEJA DE ENTRADA y MENSAJES LEÍDOS del usuario
    ba = usuario.get_ba()
    ml = usuario.get_ml()

    # Verificar si hay mensajes en la Bandeja de Entrada
    if (ba.is_empty()):
        print("\nNo tiene mensajes nuevos para leer.")
    
    else:
        print("\n    BANDEJA DE ENTRADA\n\n" + 50 * "-")

        # Recorrer y mostrar los mensajes en la colección de Bandeja
        temp = ba.get_first()
        i = 1
        while (temp != None):
            mensaje = temp.get_data()
            print(mensaje.preview(i))
            print(50 * "-")
            temp = temp.get_next()
            i += 1

        print("\n¿Qué mensaje desea ver? (indique su numeral)")
        inx = int(input())

        # Obtener y mostrar el mensaje especificado
        temp = ba.get_first()
        for k in range(inx - 1):
            temp = temp.get_next()
        mensaje = temp.get_data()
        print(mensaje)

        # Pasar mensaje de Bandeja a Leídos
        ba.remove(temp)
        mensaje.set_tipo("ML")
        ml.enqueue(mensaje)

        print(
            "¿Qué desea hacer?\n\n\
    1 - Volver a Bandeja\n\
    2 - Cerrar Sesión\n"
        )

        # Realizar la acción escogida
        match input():
            case "1":
                ver_bandeja(usuario)
            case "2":
                pass


def ver_leidos(usuario: Usuario):
    """
    ## Summary
        Muestra secuencialmente la colección de Mensajes Leídos del usuario indicado
        (desde el más antiguo hasta el más nuevo)
    ## Args
        - `usuario (Usuario)`
    """

    # Obtener la colección MENSAJES LEÍDOS del usuario
    ml = usuario.get_ml()

    # Verificar si hay Mensajes Leídos
    if ml.is_empty():
        print("\nNo has leído ningún mensaje.")
    
    else:
        print("\n    MENSAJES LEÍDOS\n")
        print("Mensaje leído más antiguo:")
        print(ml.first())

        print(
            "¿Qué deseas hacer?\n\n\
    1 - Ver Siguiente Mensaje Leído\n\
    2 - Cerrar Sesión\n"
        )

        match input():
            case "1":
                ml.dequeue()
                ver_leidos(usuario)
            case "2":
                pass


def ver_borradores(usuario: Usuario):
    """
    ## Summary
        Muestra secuencialmente la colección de Borradores del usuario indicado
        (desde el más nuevo hasta el más antiguo)
    ## Args
        - `usuario (Usuario)`
    """

    # Obtener la colección BORRADORES del usuario
    b = usuario.get_b()

    # Verificar si hay mensajes guardados como borradores
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

        # Realizar la acción escogida
        match input():
            case "1":
                enviar_mensaje(b.pop())
                ver_borradores(usuario)
            case "2":
                b.pop()
                ver_borradores(usuario)
            case "3":
                pass

# Admin
def crear_usuario(lista: DoubleList):
    """
    ## Summary:
        Añade un nuevo usuario a la lista de usuarios
    ## Args:
        - `lista (DoubleList)`: Lista de usuarios en el sistema
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
        cedula, nombre, fecha_nac, ciudad, celular, email, direccion, contrasena, cargo
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
