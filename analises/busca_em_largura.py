from fila_circular import Fila
from models.mapa import Mapa

class Largura:
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(20)
        self.fronteira.enfileirar(inicio)
        self.achou = False

    def buscar(self):
        primeiro = self.fronteira.get_primeiro()
        print("primeiro: ",primeiro.nome)

        if primeiro == self.objetivo:
            self.achou = True
        else:
            temp = self.fronteira.desinfileirar()
            print("desinfileirou ",temp.nome)

            for a in primeiro.adjacentes:
                print("verificando se ja visitado ",a.cidade.nome)
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.enfileirar(a.cidade)
            if self.fronteira.numeros_elementos > 0:
                Largura.buscar(self)

mapa = Mapa()
largura = Largura(mapa.porto_uniao,mapa.curitiba)
largura.buscar()