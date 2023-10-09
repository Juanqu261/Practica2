from estructuras import DoubleList
from modelos import Usuario
from archivos import *

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

def login(id: str, password: str, lista: DoubleList) -> bool:
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
    temp = lista.get_first()
    for i in range(lista.get_size()):
        if (temp.get_data().cedula == id):
            print(f"Bienvenido, {temp.get_data().nombre}")
            return True
    return False


# empleados, credenciales = leer_json("empleados.json"), leer_json("password.json")
# lista_usuarios = crear_usuarios(empleados, credenciales)
# login("134","weggq",lista_usuarios)