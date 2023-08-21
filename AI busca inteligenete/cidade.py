class Cidade:
    def __init__(self,nome):
        self.nome = nome
        self.visitado = False
        self.adjacentes = []
    
    def add_cidade_adjacente(self,cidade):
        self.adjacentes.append(cidade)


