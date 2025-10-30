from figura import Figura

class Rectangulo(Figura):
    def __init__(self, color, longitud, anchura):
        super().__init__(color)
        self.longitud = longitud
        self.anchura = anchura
    def __str__(self):
        return "Se creo un rectangulo de longitud: {}, y anchura: {}".format(self.longitud, self.anchura)
    

r1 = Rectangulo("azul", 5, 6)
print(r1)