class Adjacente:
    def __init__(self,cidade, distancia):
        self.cidade = cidade
        self.distancia = distancia
        self.distancia_estrela = self.cidade.distancia_objetivo + self.distancia
    