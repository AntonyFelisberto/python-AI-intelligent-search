from models.mapa import Mapa

class Pilha:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.topo = -1

    def empilhar(self,cidade):
        if not Pilha.pilha_cheia(self):
            self.topo += 1
            self.cidades[self.topo] = cidade
        else:
            print("pilha ja cheia")

    def desempilhar(self):
        if not Pilha.pilha_vazia(self):
            temp = self.cidades[self.topo]
            self.topo -= 1
            return temp
        else:
            print("pilha ja vazia")
            return None
    
    def get_topo(self):
        return self.cidades[self.topo]
    
    def pilha_vazia(self):
        return (self.topo == -1)
    
    def pilha_cheia(self):
        return (self.topo == self.tamanho -1)

mapa = Mapa()
pilha = Pilha(5)
pilha.tamanho
pilha.topo
pilha.empilhar(mapa.porto_uniao)
pilha.empilhar(mapa.campo_largo)
pilha.empilhar(mapa.canoinhas)
print(pilha.get_topo().nome)
pilha.desempilhar()
pilha.empilhar(mapa.curitiba)