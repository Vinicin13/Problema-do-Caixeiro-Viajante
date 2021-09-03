import Funções

def Menu():

    nome = input("Digite o nome do arquivo que deseja trabalhar:\n Temos predefinos os arquivos:\n 'teste.txt'"
                 "\n 'a280.txt'\n 'ali535.txt'\n 'ch130.txt'\n 'fl1577.txt'\n 'gr666.txt'\n Digite:")

    if nome != "ali533.txt" and nome != "a280.txt" and nome != "teste.txt" and nome != "ch130.txt" and nome != "fl1577.txt" and nome != "gr666.txt":
        print("Digite o nome corretamente:")
        return(Menu())

    arquivo = open(nome,"r")
    lista = Funções.lista(arquivo)
    matriz = Funções.matriz(arquivo)

    caminho = Funções.Vizinho_Mais_Proximo(lista)

    print("Caminho:")
    print(caminho)
    custo = Funções.Custo(caminho,matriz)
    print("Custo:")
    print(custo)

    tempo = int(input("Deseja refinar por quantos segundos?\n OBS:O tempo maximo limite é de 60 segundos, após esse tempo o refinamento se encerrará automaticamnete!\n"))
    refinada = Funções.refinamento(tempo,caminho,matriz)
    print("Caminho refinado:")
    print(refinada)

    newcust = Funções.Custo(refinada,matriz)
    print("Custo Refinado:")
    print(newcust)
    arquivo2 = open("saida.txt", "w")
    arquivo2.write("%f"%custo)
    arquivo2.writelines(["%s\n" % item for item in caminho])
