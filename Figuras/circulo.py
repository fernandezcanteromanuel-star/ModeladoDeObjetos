from Figuras.figura import Figura

class circulo(Figura):
    def __init__(self, color="Sin color", diametro=0):
        super().__init__(color)
        self.diametro = diametro
    def __str__(self):
        return "Se creo un círculo de color: {} y diametro: {}".format(self.color, self.diametro)
