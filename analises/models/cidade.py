class Cidade:
    def __init__(self,nome, distancia_objetivo):
        self.nome = nome
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []
    
    def add_cidade_adjacente(self,cidade):
        self.adjacentes.append(cidade)
"""
TESTES
c = Cidade("Teste", 140)
c.nome
c.visitado
c.distancia_objetivo
"""