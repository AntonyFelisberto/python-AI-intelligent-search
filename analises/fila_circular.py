from models.mapa import Mapa

class Fila:
    def __init__(self,tamaho):
        self.tamanho = tamaho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeros_elementos = 0

    def enfileirar(self,cidade):
        if not Fila.fila_cheia(self):
            if self.fim == self.tamanho - 1:
                self.fim = -1
            self.fim += 1
            self.cidades[self.fim] = cidade
            self.numeros_elementos += 1
        else:
            print("fila cheia")

    def desinfileirar(self):
        if not Fila.fila_vazia(self):
            temp = self.cidades[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
            self.numeros_elementos -= 1
            return temp
        else:
            print("fila vazia")
            return None

    def get_primeiro(self):
        return self.cidades[self.inicio]
    
    def fila_vazia(self):
        return self.numeros_elementos == 0
    
    def fila_cheia(self):
        return self.numeros_elementos == self.tamanho

mapa = Mapa()
fila = Fila(5)
fila.enfileirar(mapa.canoinhas)
fila.enfileirar(mapa.irati)
fila.enfileirar(mapa.balsa_nova)
fila.get_primeiro().nome
fila.desinfileirar()
fila.enfileirar(mapa.porto_uniao)