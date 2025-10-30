#Creamos el objeto más general: Persona

class Persona:
    def __init__(self, nombre, apellido, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
class Casada(Persona):
    def __init__(self, nombre, apellido, apellido_nacimiento, sexo):
        super().__init__(nombre, apellido, sexo)
        self.apellido_nacimiento = apellido_nacimiento
    def __str__(self):
        return "{} {}(nacida {})".format(self.nombre, self.apellido, self.apellido_nacimiento)
    
    def marido(self, Marido):
        if Marido.apellido == self.apellido:
            return print('{} {}(nacida {}) casada con'.format(self.nombre, self.apellido, self.apellido_nacimiento), Marido)
        else:
            return print('No casados')
        


Lolito = Persona('Lolito', 'Fernández', 'Indefinido')
Juana = Casada('Juana', 'Fernández', 'Heredia', 'Hombre')
Juana.marido(Lolito)