from cidade import Cidade
from adjacente import Adjacente

class Mapa:
    porto_uniao = Cidade("Porto Uniao")
    paulo_frontin = Cidade("Paulo Frontin")
    canoinhas = Cidade("Canoinhas")
    irati = Cidade("Irati")
    palmeira = Cidade("Palmeira")
    campo_largo = Cidade("Campo Largo")
    curitiba = Cidade("Curitiba")
    bolsa_nova = Cidade("Bolsanova")
    araucaria = Cidade("Araucaria")
    sao_jose = Cidade("Sao Jose")
    contenda = Cidade("Contenda")
    mafra = Cidade("Mafra")
    tijucas = Cidade("Tijucas")
    lapa = Cidade("Lapa")
    sao_mateus = Cidade("Sao Mateus")
    tres_barras = Cidade("Tres Barras")

    porto_uniao.add_cidade_adjacente(Adjacente(paulo_frontin))
    porto_uniao.add_cidade_adjacente(Adjacente(canoinhas))
    porto_uniao.add_cidade_adjacente(Adjacente(sao_mateus))

    paulo_frontin.add_cidade_adjacente(Adjacente(porto_uniao))
    paulo_frontin.add_cidade_adjacente(Adjacente(irati))
    
    canoinhas.add_cidade_adjacente(Adjacente(porto_uniao))
    canoinhas.add_cidade_adjacente(Adjacente(tres_barras))
    canoinhas.add_cidade_adjacente(Adjacente(mafra))
    
    irati.add_cidade_adjacente(Adjacente(paulo_frontin))
    irati.add_cidade_adjacente(Adjacente(palmeira))
    irati.add_cidade_adjacente(Adjacente(sao_mateus))
    
    palmeira.add_cidade_adjacente(Adjacente(irati))
    palmeira.add_cidade_adjacente(Adjacente(sao_mateus))
    palmeira.add_cidade_adjacente(Adjacente(campo_largo))
    
    campo_largo.add_cidade_adjacente(Adjacente(palmeira))
    campo_largo.add_cidade_adjacente(Adjacente(bolsa_nova))
    campo_largo.add_cidade_adjacente(Adjacente(curitiba))
    
    curitiba.add_cidade_adjacente(Adjacente(campo_largo))
    curitiba.add_cidade_adjacente(Adjacente(bolsa_nova))
    curitiba.add_cidade_adjacente(Adjacente(araucaria))
    curitiba.add_cidade_adjacente(Adjacente(sao_jose))
    
    bolsa_nova.add_cidade_adjacente(Adjacente(curitiba))
    bolsa_nova.add_cidade_adjacente(Adjacente(campo_largo))
    bolsa_nova.add_cidade_adjacente(Adjacente(contenda))
    
    araucaria.add_cidade_adjacente(Adjacente(curitiba))
    araucaria.add_cidade_adjacente(Adjacente(contenda))
    
    sao_jose.add_cidade_adjacente(Adjacente(curitiba))
    sao_jose.add_cidade_adjacente(Adjacente(tijucas))
    
    contenda.add_cidade_adjacente(Adjacente(bolsa_nova))
    contenda.add_cidade_adjacente(Adjacente(araucaria))
    contenda.add_cidade_adjacente(Adjacente(lapa))

    mafra.add_cidade_adjacente(Adjacente(tijucas, 99))
    mafra.add_cidade_adjacente(Adjacente(lapa, 57))
    mafra.add_cidade_adjacente(Adjacente(canoinhas, 66))
    
    tijucas.add_cidade_adjacente(Adjacente(mafra, 99))
    tijucas.add_cidade_adjacente(Adjacente(sao_jose, 49))

    lapa.add_cidade_adjacente(Adjacente(contenda, 26))
    lapa.add_cidade_adjacente(Adjacente(sao_mateus, 60))
    lapa.add_cidade_adjacente(Adjacente(mafra, 57))
    
    sao_mateus.add_cidade_adjacente(Adjacente(palmeira, 77))
    sao_mateus.add_cidade_adjacente(Adjacente(irati, 57))
    sao_mateus.add_cidade_adjacente(Adjacente(lapa, 60))
    sao_mateus.add_cidade_adjacente(Adjacente(tres_barras, 43))
    sao_mateus.add_cidade_adjacente(Adjacente(porto_uniao, 87))
    
    tres_barras.add_cidade_adjacente(Adjacente(sao_mateus, 43))
    tres_barras.add_cidade_adjacente(Adjacente(canoinhas, 12))

mapa = Mapa()
print(mapa.porto_uniao.nome)
print(mapa.porto_uniao.visitado)
print(mapa.porto_uniao.adjacentes)
for i in range(len(mapa.porto_uniaoadjacentes)):
    print(mapa.porto_uniao.adjacentes[i].cidade.nome)