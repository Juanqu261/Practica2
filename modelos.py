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
        self.celular= e

    def set_email(self, e):
        self.celular = e

    def set_direccion(self, e):
        self.direccion = e

    def set_contrasena(self, e):
        self.contrasena = e

    def set_cargo(self, e):
        self.cargo = e

    def __str__(self):
        return f"{self.nombre} {self.contrasena} {self.cedula}"
