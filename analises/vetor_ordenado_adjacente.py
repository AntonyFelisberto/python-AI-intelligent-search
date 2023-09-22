from models.mapa import Mapa

class VetorOrdenadoAdjacente:
    def __init__(self,tamanho):
        self.numero_elementos = 0
        self.adjacentes = [None] * tamanho

    def inserir(self,adjacente):
        if self.numero_elementos == 0:
            self.adjacentes[0] = adjacente
            self.numero_elementos = 1
            return
        
        posicao = 0
        i = 0
        while i < self.numero_elementos:
            if adjacente.distancia_estrela > self.adjacentes[posicao].distancia_estrela:
                posicao +=1
            i += 1
        
        for k in range(self.numero_elementos,posicao,-1):
            self.adjacentes[k] = self.adjacentes[k - 1]

        self.adjacentes[posicao] = adjacente
        self.numero_elementos += 1

    def get_primeiro(self):
        return self.adjacentes[0].cidade
    
    def mostrar(self):
        for i in range(0,self.numero_elementos):
            print(f"{self.adjacentes[i].cidade.nome} _ {self.adjacentes[i].distancia_estrela}")