#Clase figura

class Figura:
    #Figura, init y str
    def __init__(self, color="Sin color"):
        self.color = color
    def __str__(self):
        return "Se creó una figura de color {}".format(self.color)
    


    
        