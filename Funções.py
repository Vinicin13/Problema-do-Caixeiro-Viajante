from random import randint
from tqdm import tqdm
import numpy as np
import copy
import time

def lista(arq):

    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])

    Lista = [[] for x in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = float(Aresta[2])
        Lista[x].append((y, z))
        Lista[y].append((x, z))

    return Lista

def matriz(arq):

    arq.seek(0)
    FirstLine = arq.readline().rstrip()
    FirstLine = FirstLine.split()
    Vertices = int(FirstLine[0])
    Arestas = int(FirstLine[1])
    Matriz = [[0 for _ in range(Vertices)] for _ in range(Vertices)]

    for i in range(0, Arestas):
        Aresta = arq.readline()
        Aresta = Aresta.split(" ")
        x = int(Aresta[0])
        y = int(Aresta[1])
        z = float(Aresta[2])
        Matriz[x][y] = z
        Matriz[y][x] = z

    return Matriz

def Vizinho_Mais_Proximo(Lista):

   destinos = [x for x in range(len(Lista))]
   origens = [0 for x in range(len(Lista))]

   aux = None
   u = 0
   caminho = []
   caminho.append(u)
   origens[0] = 1

   while len(destinos) != 1:
      menor = float('inf')
      for i in Lista[u]:
         if i[1] < menor and origens[i[0]] == 0:
            menor = i[1]
            aux = i[0]
      origens[aux] = 1
      caminho.append(aux)
      destinos.remove(u)
      u = aux

   caminho.append(caminho[0])
   return caminho


def Custo(caminho, Matriz):
   custo = 0
   for i in range(len(caminho) - 1):
      x = caminho[i]
      y = caminho[i + 1]
      custo = custo + Matriz[x][y]
   return custo

def refinamento(tempo, caminho, Matriz):

    aux1 = []
    aux2 = 0
    tentativa = []
    for _ in tqdm(range(tempo),desc="Refinando...", ascii=False, ncols=75):
        vertice = randint(1, len(caminho) - 2)
        vertice2 = randint(1, len(caminho) - 2)

        if vertice != vertice2 and (vertice, vertice2) not in tentativa:

            tentativa.append((vertice, vertice2))

            aux1 = copy.deepcopy(caminho)
            aux2 = aux1[vertice]
            aux1[vertice] = aux1[vertice2]
            aux1[vertice2] = aux2
            if Custo(aux1, Matriz) < Custo(caminho, Matriz):
                caminho = copy.deepcopy(aux1)
                tentativa = []

        time.sleep(0.99)

    return caminho
