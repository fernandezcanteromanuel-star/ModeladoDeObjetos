#Creamos el objeto más general: Persona

class Persona:
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_nacimiento = apellido_nacimiento
        self.sexo = sexo
    