from estructuras import *
from archivos import *
from acciones import *

# Lectura de registro --> Cargamos los archivos .json en formato de diccionarios
empleados, credenciales = leer_json("empleados.json"), leer_json("password.json")

# Crear objetos usuario --> Creamos objetos que contengan la informacion de los diccionarios
#   Estos objetos quedaran agrupados en la siguiente lista
lista_usuarios = crear_usuarios(empleados, credenciales)
# print(lista_usuarios.as_pylist()[0].get_contrasena())

# Login --> Para ingresar al sistema, los datos ingresados deben coincidir con los datos
#   De algun objeto(usuario) existente dentro de lista_usuarios.
print("Bienvenido al Sistema de Mensajería")
# print("Ingrese su cedula: ")
# cedula = input()
# print("Ingrese su contrasena: ")
# contrasena = input()
user = login(
    lista=lista_usuarios,
)

# Si se omite el login
if (user == None):
    quit()


