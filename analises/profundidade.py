from pilha import Pilha
from models.mapa import Mapa

class Profundidade:
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(20)
        self.fronteira.empilhar(inicio)
        self.achou = False

    def buscar(self):
        topo = self.fronteira.get_topo()
        print("topo: ",topo.nome)

        if topo == self.objetivo:
            self.achou = True
        else:
            for a in topo.adjacentes:
                if self.achou == False:
                    print("verificando se ja visitado: ",a.cidade.nome)
                    if a.cidade.visitado == False:
                        a.cidade.visitado = True
                        self.fronteira.empilhar(a.cidade)
                        Profundidade.buscar(self)
        
        print(f"desempilhou: {self.fronteira.desempilhar().nome}")

mapa = Mapa()
profundidade = Profundidade(mapa.porto_uniao,mapa.curitiba)
profundidade.buscar()