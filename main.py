#!/usr/bin/env python3
import numpy as np
import fileinput
from itertools import permutations


def tentativa(matriz, n):
    vertices = [ i for i in range(1,n+1) ]   
    possibilidades = { i: [] for i in vertices } 
        
    #todas possibilidades >3 ate tamanho n
    for i in range(3,n+1):
        for j in list(permutations(vertices, i)):
            possibilidades[ j[0] ].append(j)

    #pego apenas as possibilidades comecadas com 1 ( nodo inicial )
    possibilidades2 = [] 
    for i in possibilidades[1]:
        possibilidades2.append(list(i))

    
    # retira todas as solucoes que o segundo vertice nao tem ligacao com o inicio, e o ultimo vertice nao tem caminho de volta para o inicio
    rmv = []
    for i in possibilidades2:
        if matriz[0][ i[1]-1 ] == 0:
            rmv.append(i)
        if matriz[ i[-1]-1 ][0] == 0:
            rmv.append(i)
    for i in rmv:
        if i not in possibilidades2: next
        else: possibilidades2.remove( i )

    # varre a matriz para verificar se existem vertices inuteis que nao tem como fazer parte da solucao
    vertice_inutil =[]
    for i in range(n):
        a = list(matriz[i]).count(0)
        if a > n-2:
            vertice_inutil.append(i)

    rmv = []
    #retira solucoes que possuem algum vertice inutil, ou seja, algum vertice que so e ligado por uma aresta com um unico vertice
    if vertice_inutil:
        for i in range(len(vertice_inutil)):
            for j in possibilidades2:
                if (vertice_inutil[i]+1) in j:
                    rmv.append(j)
        for i in rmv: 
            if i not in possibilidades2: next
            else: possibilidades2.remove( i )

    rmv = []
    #faz uma varredura buscando em cada possibilidade se os vertices do meio nao estao conectados com o proximo,
    #se nao estiver para de percorrer aquela "arvore" e ja corta ela das solucoes possiveis
    for i in possibilidades2: #[1,2,3...]
        for j in range(2,len(i)): 
            if matriz[ i[j-1]-1 ][ i[j] - 1 ] == 0:
                rmv.append(i)
                break
    for i in rmv:
        if i not in possibilidades2: next
        else: possibilidades2.remove( i )    
    
    encontra_sol(possibilidades2,matriz)
    


def encontra_sol(caminhos, matriz):
    
    pesos = 0

    for i in caminhos:
        temp = 0
        for j in range(len(i)): 
            temp += matriz[ i[j-1]-1 ][ i[j] - 1 ]
        
        if pesos < temp:
            melhor_caminho = i
            pesos = temp
    
    print("caminho: >> ",melhor_caminho, "\n peso: ", pesos, "\n")



    
        
    


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










    
def main():
    batata, n = leitura() # retorna um np array da matriz simetrica dos pesos do grafo
    print(batata)
    # print("aaa> \n",len(batata))
    tentativa(batata, n)
    # grafo = nx.from_numpy_matrix(batata)
    
    
    #debug_grafo(grafo)
   
    
if __name__ == "__main__":
    main()


#gerar uma matriz so de 0 com tamanho n por n
#fazer a transposta e somar as duas.