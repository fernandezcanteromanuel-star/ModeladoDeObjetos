from figura import Figura

class Cuadrado(Figura):
    def __init__(self, color="Sin color", lado=0):
        super().__init__(color)
        self.lado = lado
    def __str__(self):
        return "Se creo un cuadrado de lado: {} y color {}".format(self.lado, self.color)

