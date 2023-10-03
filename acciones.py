from estructuras import DoubleList
from modelos import Usuario


def crear_usuarios(diccionario_datos: dict, credenciales: dict) -> DoubleList:
    """
    [Summary]:
        Crea un usuario nuevo
    [Args]:
        diccionario (dict): Diccionario con los datos del usuario
    [Returns]:
        usuario (Usuario): Usuario creado
    """
    lista_doble = DoubleList()
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
        lista_doble.add_last(usuario)

        return lista_doble
