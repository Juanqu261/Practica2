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


# with open("Empleados.txt", "r") as f:
#     registro = List()
#     emps = [line[:-1].split(' ') for line in f.readlines()]
#     for emp in emps:
#         registro.add_last(emp)

# print(f"Verificación registro:\n{registro.get_first().get_data()}\n\n")

# with open("Password.txt", "r") as p:
#     ids = List()
#     for emp in [line[:-1].split(' ') for line in p.readlines()]:
#         ids.add_last(emp)
# print(f"Verificación ID's:\n{ids.get_first().get_data()}\n\n")

# # Login
# print("Bienvenido al Sistema de Mensajería")
# print("Por favor ingresa tu No. de Documento:")
