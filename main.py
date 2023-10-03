from estructuras import *
from archivos import *
from acciones import *


def login(id: str, password: str, lista: DoubleList) -> bool:
    pass


# Lectura de registro
empleados, credenciales = leer_json("empleados.json"), leer_json("password.json")

lista = crear_usuarios(empleados, credenciales)

# Login
print("Bienvenido al Sistema de Mensajería")
print("Ingrese su cedula: ")
cedula = input()
print("Ingrese su contrasena: ")
contrasena = input()
login(
    id=cedula,
    password=contrasena,
    lista=lista,
)
