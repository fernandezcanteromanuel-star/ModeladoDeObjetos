from Figuras.figura import Figura

class elipse(Figura):
    def __init__(self, color="Sin color", eje_may=0, eje_men=0):
        super().__init__(color)
        self.eje_may = eje_may
        self.eje_men = eje_men
    def __str__(self):
        return "Se creo una elipse de eje mayor: {}, y eje menor: {}, y de color {}".format(self.eje_may, self.eje_men, self.color)