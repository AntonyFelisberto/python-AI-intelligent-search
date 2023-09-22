from vetor_ordenado_adjacente import VetorOrdenadoAdjacente
from models.mapa import Mapa

class Estrela:
    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.achou = False

    def buscar(self,atual):
        print("atual ",atual.nome)
        atual.visitado = True

        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = VetorOrdenadoAdjacente(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a)
            self.fronteira.mostrar()
            if self.fronteira.get_primeiro() != None:
                Estrela.buscar(self,self.fronteira.get_primeiro())

mapa = Mapa()
estrela = Estrela(mapa.curitiba)
estrela.buscar(mapa.porto_uniao)