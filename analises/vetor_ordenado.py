
class VetorOrdenado:
    def __init__(self,tamanho):
        self.numero_elementos = 0
        self.cidades = [None] * tamanho

    def inserir(self,cidade):
        if self.numero_elementos == 0:
            self.cidades[0] = cidade
            self.numero_elementos = 1
            return
        posicao = 0
        i = 0
        while i < self.numero_elementos:
            if cidade.distancia_objetivo > self.cidades[posicao].distancia_objetivo:
                posicao +=1
            i += 1
        
        for k in range(self.numero_elementos,posicao,-1):
            self.cidades[k] = self.cidades[k - 1]

        self.cidades[posicao] = cidade
        self.numero_elementos += 1

    def get_primeiro(self):
        return self.cidades[0]
    
    def mostrar(self):
        for i in range(0,self.numero_elementos):
            print(f"{self.cidades[i].nome} _ {self.cidades[i].distancia_objetivo}")

from models.mapa import Mapa
mapa = Mapa()
vetor = VetorOrdenado(5)
vetor.inserir(mapa.porto_uniao)
vetor.inserir(mapa.paulo_frontin)
vetor.inserir(mapa.balsa_nova)
vetor.mostrar()
vetor.inserir(mapa.palmeira)