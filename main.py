#!/usr/bin/env python3
import numpy as np
import fileinput
from itertools import permutations
#daqui pra baixo provavelmente nao vou usar
import networkx as nx
from numpy.core.einsumfunc import _parse_possible_contraction
import pylab as plt
from collections import defaultdict


def tentativa(matriz, n):
    vertices = [ i for i in range(1,n+1) ]
    t_possibilidades = list(permutations(vertices))
   
    possibilidades = {} 

    #mostra todas as possibilidades, agrupando por quem inicia
    j = 1
    for v in vertices:
        tmp = []
        for i in t_possibilidades:
            if i[0] == v:
                tmp.append(list(i))
        possibilidades[v] = tmp
    
    
    rmv = []
    for i in possibilidades:
        for j in possibilidades[i]:
            if (matriz[i-1][ j[1]-1 ] == 0  ):
                rmv.append((i,j))
    for i in rmv:
        possibilidades[i[0]].remove(i[1])
    print(possibilidades)
    retirada_sol_inv(possibilidades, n, matriz) #primeiro elemento com segundo elemento   

    print(possibilidades)
    #ir atras das possiveis solucoes montando a arvore ali so dos elementos do 1
    ## a partir da chave 1, verificar o segundo elemento
    # segundo elemento vai ir pra chave dele, e verificar se o segundo elemento dele corresponde ao esperado ( empilha ) pra dizer que ja passou ali
    # segue o rumo ate chegar no ultimo elemento que seja 1
        
    

## por algum motivo ele so ta retirando 1 e 4, e ainda retira todos os elemento
def retirada_sol_inv(possibilidades, n, matriz):
    rmv = []
    for i in possibilidades:
        for j in possibilidades[i]:
            if (matriz[i-1][ j[1]-1 ] == 0  ):
                rmv.append((i,j))
    for i in rmv:
        possibilidades[i[0]].remove(i[1])
    print(possibilidades)
    rmv = []




def tratamento(dado, matriz_pesos):
    numeros = []
    i = 0
    j = 1
    jj = 1
    for valores in dado:
        temp = valores.split()
        for v in temp:
            if v.isdigit():
                # numeros.append(int(i))
                matriz_pesos[i][j] = int(v)
                j+=1
            else:
                exit("Formato de dados da matriz incorreto")
        i+=1
        jj+=1
        j=jj
    
    matriz_pesos = np.add(matriz_pesos,matriz_pesos.transpose())
    
    return matriz_pesos



def leitura():
    entrada = []
    for linha in fileinput.input():
        entrada.append( linha.rstrip() )
    
    n = int(entrada[0])
    matriz_pesos = np.zeros( (n,n) , dtype=int)
    entrada = entrada[1:]
    matriz_pesos = tratamento(entrada, matriz_pesos)
    
    return matriz_pesos, n


def debug_grafo(matriz):
    grafo = nx.from_numpy_matrix(matriz)
    layout = nx.spring_layout(grafo)
    nx.draw(grafo, layout ,with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(grafo, pos=layout)

    plt.show()



def main():
    batata, n = leitura() # retorna um np array da matriz simetrica dos pesos do grafo
    print(batata)
    tentativa(batata, n)
    # grafo = nx.from_numpy_matrix(batata)
    
    
    #debug_grafo(grafo)
   
    
if __name__ == "__main__":
    main()


#gerar uma matriz so de 0 com tamanho n por n
#fazer a transposta e somar as duas.