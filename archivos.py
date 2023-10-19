"""Operaciones de Cargado y Guardado de datos usando archivos tipo JSON"""

import json
from modelos import Usuario
from estructuras import DoubleList


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
