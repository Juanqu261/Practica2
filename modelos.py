"""Contiene las clases Usuario y Mensaje"""
import estructuras

class Usuario:
    def __init__(
        self,
        cedula,
        nombre,
        fecha_nacimiento,
        ciudad,
        celular,
        email,
        direccion,
        contrasena,
        cargo,
    ):
        self.cedula = cedula
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad = ciudad
        self.celular = celular
        self.email = email
        self.direccion = direccion
        self.contrasena = contrasena
        self.cargo = cargo
        self.ba = estructuras.DoubleList()
        self.ml = estructuras.Queue()
        self.b = estructuras.Stack()

    def get_cedula(self):
        return self.cedula

    def get_nombre(self):
        return self.nombre

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    def get_ciudad(self):
        return self.ciudad

    def get_celular(self):
        return self.celular

    def get_email(self):
        return self.email

    def get_direccion(self):
        return self.direccion

    def get_contrasena(self):
        return self.contrasena

    def get_cargo(self):
        return self.cargo

    def set_cedula(self, e):
        self.cedula = e

    def set_nombre(self, e):
        self.cedula = e

    def set_fecha_nacimiento(self, e):
        self.fecha_nacimiento = e

    def set_ciudad(self, e):
        self.ciudad = e

    def set_celular(self, e):
        self.celular = e

    def set_email(self, e):
        self.celular = e

    def set_direccion(self, e):
        self.direccion = e

    def set_contrasena(self, e):
        self.contrasena = e

    def set_cargo(self, e):
        self.cargo = e

    def es_admin(self) -> bool:
        return True if self.cargo == "administrador" else False

    def set_bandejas(self, entrada, leidos, borrador):
        self.ba = entrada
        self.ml = leidos
        self.b = borrador

    def get_bandejas(self):
        return self.ba, self.ml, self.b

    def __dict__(self):
        return {
            f"{self.cedula}": {
                "cedula": self.cedula,
                "nombre": self.nombre,
                "fecha_de_nacimiento": self.fecha_nacimiento,
                "ciudad": self.ciudad,
                "celular": self.celular,
                "email": self.email,
                "direccion": self.direccion,
            }
        }

    def __str__(self):
        return f"\n\
USUARIO\n\
    Nombre: {self.nombre}\n\
    Contraseña: {self.contrasena}\n\
    Cédula: {self.cedula}\n"


class Mensaje:
    def __init__(
        self,
        destinatario=None,
        tipo=None,
        remitente=None,
        fecha=None,
        hora=None,
        asunto=None,
        cuerpo=None,
    ):
        self.destinatario = destinatario
        self.tipo = tipo
        self.remitente = remitente
        self.fecha = fecha
        self.hora = hora
        self.asunto = asunto
        self.cuerpo = cuerpo

    # GETTERS
    def get_destinatario(self):
        return self.destinatario

    def get_tipo(self):
        return self.tipo

    def get_remitente(self):
        return self.remitente

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_asunto(self):
        return self.asunto

    def get_cuerpo(self):
        return self.cuerpo

    # SETTERS
    def set_destinatario(self, destinatario):
        self.destinatario = destinatario

    def set_tipo(self, tipo="B"):
        self.tipo = tipo

    def set_remitente(self, remitente):
        self.remitente = remitente

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self, hora):
        self.hora = hora

    def set_asunto(self, asunto):
        self.asunto = asunto

    def set_cuerpo(self, cuerpo: str):
        self.cuerpo = cuerpo

    def __dict__(self):
        return {
            "tipo": self.tipo,
            "remitente": self.remitente,
            "fecha": self.fecha,
            "hora": self.hora,
            "asunto": self.asunto,
            "cuerpo": self.cuerpo,
        }

    def __str__(self):
        return f'\n    De: {self.remitente}\n\
    Enviado a las {self.hora} del {self.fecha}\n\n\
    Asunto: {self.asunto}\n\n\n\
    "{self.cuerpo}"\n'
