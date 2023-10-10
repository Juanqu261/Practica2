from estructuras import *
from archivos import *
from acciones import *

# Lectura de registro --> Cargamos los archivos .json en formato de diccionarios
empleados, credenciales = leer_json("empleados.json"), leer_json("password.json")

# Crear objetos usuario --> Creamos objetos que contengan la informacion de los diccionarios
#   Estos objetos quedaran agrupados en la siguiente lista
lista_usuarios = crear_usuarios(empleados, credenciales)

# Login --> Para ingresar al sistema, los datos ingresados deben coincidir con los datos
#   De algun objeto(usuario) existente dentro de lista_usuarios.
print("Bienvenido al Sistema de Mensajería")

user = login(lista_usuarios).get_data()

# Si se omite el login
if (user == None):
    quit()

print("Acciones:\n\n\
    1 - Ver Bandeja\n\
    6 - Cambiar contraseña de un empleado\n\
    7 - Eliminar empleado\n\
    x - ...\n\n\
Indique el número de la acción que desea realizar:\n")

match input():
    case "1":
        ver_bandeja()
    case "6":        
        cambiar_contrasena(lista_usuarios)
    case "7":
        eliminar_usuario(lista_usuarios)
        
# temp = lista_usuarios.get_first()
# for i in range(lista_usuarios.get_size()):
#     print(temp.get_data().__str__())
#     temp = temp.get_next()