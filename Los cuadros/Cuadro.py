class cuadro:
    def __init__(self, titulo, autor, ads_cronologica, tecnica, subtecnica, material, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.ads_conologica = ads_cronologica
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material = material
        self.descripcion = descripcion
    def __str__(self):
        return '''
        Título: {}
        Autor: {}
        Cronología: {}
        Técnica empleada: {}
        Subtécnica: {}
        Material de soporte: {}
        Descripción del cuadro: {}'''.format(self.titulo, self.autor, self.ads_conologica, self.tecnica, self.subtecnica, self.material, self.descripcion)

class Lugar:
    def __init__(self, institucion, ciudad, pais):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais
    def __str__(self):
        return '''
        Institución: {}
        Ciudad: {}
        País: {}'''.format(self.institucion, self.ciudad, self.pais)


