import json
from modelos import Usuario
from estructuras import DoubleList


def leer_json(nombre_del_archivo: str) -> dict:
    """
    ### Summary:
        Lee el archivo json y lo retorna como un diccionario
    ### Args:
        nombre_del_archivo (str): Nombre del archivo a leer
    ### Returns:
        diccionario (dict): Diccionario con los datos del json
    """
    with open(nombre_del_archivo, "r") as file:
        diccionario = json.load(file)
    return diccionario


def guardar_json(nombre_del_archivo: int, guardar: any) -> None:
    """
    ### Summary:
        Guarda el diccionario en un archivo json
    ### Args:
        nombre_del_archivo (str): Nombre del archivo a guardar
        guardar (dict): Diccionario a guardar
    """
    with open(nombre_del_archivo, "w"):
        diccionario = json.dump(guardar, nombre_del_archivo, indent=4)
