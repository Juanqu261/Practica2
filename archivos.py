import json


def leerJSON(nombre_del_archivo: str) -> dict:
    """
    [Summary]:
        Lee el json y lo retorna como un diccionario
    [Args]:
        nombre_del_archivo (str): Nombre del archivo a leer
    [Returns]:
        diccionario (dict): Diccionario con los datos del json
    """
    with nombre_del_archivo, "r":
        diccionario = json.load(nombre_del_archivo)
    return diccionario


def guardarJSON(nombre_del_archivo: int, guardar: any) -> None:
    """
    [Summary]:
        Guarda el diccionario en un archivo json
    [Args]:
        nombre_del_archivo (str): Nombre del archivo a guardar
        guardar (dict): Diccionario a guardar
    """
    # with nombre_del_archivo, "w":
    #    json.dump(guardar, #nombre_del_archivo)
