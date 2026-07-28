class Pet:

    def __init__(
        self,
        nombre,
        tipo,
        color="",
        apodo="",
        propietario="",
        telefono=""
    ):

        self.nombre = nombre
        self.tipo = tipo
        self.color = color
        self.apodo = apodo
        self.propietario = propietario
        self.telefono = telefono

    def to_dict(self):

        return {
            "nombre": self.nombre,
            "tipo": self.tipo,
            "color": self.color,
            "apodo": self.apodo,
            "propietario": self.propietario,
            "telefono": self.telefono
        }