from models.cidade import Cidade
from models.adjacente import Adjacente

class Mapa:
    porto_uniao = Cidade("Porto Uniao", 203)
    paulo_frontin = Cidade("Paulo Frontin", 172)
    canoinhas = Cidade("Canoinhas", 141)
    irati = Cidade("Irati", 139)
    palmeira = Cidade("Palmeira", 59)
    campo_largo = Cidade("Campo Largo", 27)
    curitiba = Cidade("Curitiba", 0)
    balsa_nova = Cidade("Balsa Nova", 41)
    araucaria = Cidade("Araucária", 23)
    sao_jose = Cidade("São José dos Pinhais", 13)
    contenda = Cidade("Contenda", 39)
    mafra = Cidade("Mafra", 94)
    tijucas = Cidade("Tijucas do Sul", 56)
    lapa = Cidade("Lapa", 74)
    sao_mateus = Cidade("São Mateus do Sul", 123)
    tres_barras = Cidade("Três Barras", 131)

    porto_uniao.add_cidade_adjacente(Adjacente(paulo_frontin, 46)) 
    porto_uniao.add_cidade_adjacente(Adjacente(canoinhas, 78))
    porto_uniao.add_cidade_adjacente(Adjacente(sao_mateus, 87))

    paulo_frontin.add_cidade_adjacente(Adjacente(porto_uniao, 46))
    paulo_frontin.add_cidade_adjacente(Adjacente(irati, 75))

    canoinhas.add_cidade_adjacente(Adjacente(porto_uniao, 78))
    canoinhas.add_cidade_adjacente(Adjacente(tres_barras, 12))
    canoinhas.add_cidade_adjacente(Adjacente(mafra, 66))
    
    irati.add_cidade_adjacente(Adjacente(paulo_frontin, 75))
    irati.add_cidade_adjacente(Adjacente(palmeira, 75))
    irati.add_cidade_adjacente(Adjacente(sao_mateus, 57))
    
    palmeira.add_cidade_adjacente(Adjacente(irati, 75))
    palmeira.add_cidade_adjacente(Adjacente(sao_mateus, 77))
    palmeira.add_cidade_adjacente(Adjacente(campo_largo, 55))

    campo_largo.add_cidade_adjacente(Adjacente(palmeira, 55))
    campo_largo.add_cidade_adjacente(Adjacente(balsa_nova, 22))
    campo_largo.add_cidade_adjacente(Adjacente(curitiba, 29))

    curitiba.add_cidade_adjacente(Adjacente(campo_largo, 29))
    curitiba.add_cidade_adjacente(Adjacente(balsa_nova, 51))
    curitiba.add_cidade_adjacente(Adjacente(araucaria, 37))
    curitiba.add_cidade_adjacente(Adjacente(sao_jose, 15))
    
    balsa_nova.add_cidade_adjacente(Adjacente(curitiba, 51))
    balsa_nova.add_cidade_adjacente(Adjacente(campo_largo, 22))
    balsa_nova.add_cidade_adjacente(Adjacente(contenda, 19))

    araucaria.add_cidade_adjacente(Adjacente(curitiba, 37))
    araucaria.add_cidade_adjacente(Adjacente(contenda, 18))

    sao_jose.add_cidade_adjacente(Adjacente(curitiba, 15))
    sao_jose.add_cidade_adjacente(Adjacente(tijucas, 49))

    contenda.add_cidade_adjacente(Adjacente(balsa_nova, 19))
    contenda.add_cidade_adjacente(Adjacente(araucaria, 18))
    contenda.add_cidade_adjacente(Adjacente(lapa, 26))

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

"""
TESTES
mapa = Mapa()
print(mapa.porto_uniao.nome)
print(mapa.porto_uniao.visitado)
print(mapa.porto_uniao.adjacentes)
for i in range(len(mapa.porto_uniaoadjacentes)):
    print(mapa.porto_uniao.adjacentes[i].cidade.nome)
"""