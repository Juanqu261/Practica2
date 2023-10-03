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

    def __str__(self):
        return f"Carlos {self.celular} {self.email}"
