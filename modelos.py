"""Contiene las clases Usuario y Mensaje"""
from estructuras import *

class Usuario:
    """
    ## Attributes
        - `cedula (str)`
        - `nombre (str)`
        - `fecha_nacimiento (str)`
        - `ciudad (str)`
        - `celular (str)`
        - `email (str)`
        - `direccion (str)`
        - `contrasena (str)`
        - `cargo (str)`
        - `ba (DoubleList)`
        - `ml (Queue)`
        - `b (Stack)`
    """

    def __init__(
        self,
        cedula = None,
        nombre = None,
        fecha_nacimiento = None,
        ciudad = None,
        celular = None,
        email = None,
        direccion = None,
        contrasena = None,
        cargo = None,
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
        self.ba = DoubleList()
        self.ml = Queue()
        self.b = Stack()

    # GETTERS
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
    
    def get_ba(self):
        return self.ba
    
    def get_ml(self):
        return self.ml
    
    def get_b(self):
        return self.b

    # SETTERS
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
    
    def set_ba(self, ba: DoubleList):
        self.ba = ba
    
    def set_ml(self, ml: Queue):
        self.ml = ml

    def set_b(self, b: Stack):
        self.b = b

    def es_admin(self) -> bool:
        return True if self.cargo == "administrador" else False

    # def set_bandejas(self, entrada, leidos, borrador):
    #     self.ba = entrada
    #     self.ml = leidos
    #     self.b = borrador

    # def get_bandejas(self):
    #     return self.ba, self.ml, self.b

    # FORMATOS
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
        destinatario: Usuario,
        tipo: str,
        remitente: Usuario,
        fecha: str,
        hora: str,
        asunto: str,
        cuerpo: str,
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

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_remitente(self, remitente):
        self.remitente = remitente

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self, hora):
        self.hora = hora

    def set_asunto(self, asunto):
        self.asunto = asunto

    def set_cuerpo(self, cuerpo):
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
    
    def preview(self, indice: int):
        """
        Formato con información superficial del mensaje para mostrarlo
        al consultar la Bandeja de Entrada.
        """

        return f"\
            {self.fecha}  {self.hora}\n\
    {'%02d'%indice}      Asunto: {self.asunto}\n\
            {self.remitente.get_nombre()}"

    def __str__(self):
        return f'\n    De: {self.remitente.get_nombre()}\n\
    Enviado a las {self.hora} del {self.fecha}\n\n\
    Asunto: {self.asunto}\n\n\n\
    "{self.cuerpo}"\n'
