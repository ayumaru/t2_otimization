#!/usr/bin/env python3
import numpy as np
import fileinput
from itertools import permutations



def tentativa2(matriz,n):
    
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
    
    possibilidades2 = [] 
    for i in possibilidades[1]:
        possibilidades2.append(i)

    #print(possibilidades2)
    
    rmv = []
    for i in possibilidades2:
        if (matriz[0][ i[1]-1 ] == 0  ):
            rmv.append(i)
        if i[-1] != 1 and matriz[ i[-1]-1 ][0] == 0:
            rmv.append(i)

    
    for i in rmv:
        possibilidades2.remove( i )


    rmv = []
    for i in range(n):
        print(matriz[i])



    #print("pos>> \n",possibilidades2)

    return 0






def tentativa(matriz, n):
    vertices = [ i for i in range(1,n+1) ]   
    possibilidades = { i: [] for i in vertices  } 
        
    #todas possibilidades >3 ate tamanho n, agrupando em dicionario
    for i in range(3,n+1):
        for j in list( permutations(vertices, i)):
            possibilidades[ j[0] ].append(j)

    possibilidades2 = [] 
    for i in possibilidades[1]:
        possibilidades2.append(list(i))

    
    rmv = []
    for i in possibilidades2:
        if ( matriz[0][ i[1]-1 ] == 0  ):
            rmv.append(i)
        if matriz[ i[-1]-1 ][0] == 0:
            rmv.append(i)

 
    for i in rmv:
        if i not in possibilidades2: next
        else: possibilidades2.remove( i )

 
    rmv = []
    vertice_inutil =[]
    for i in range(n):
        a = list(matriz[i]).count(0)
        if a > n-2:
            vertice_inutil.append(i)

    for i in range(len(vertice_inutil)):
        for j in possibilidades2:
            if (vertice_inutil[i]+1) in j:
                rmv.append(j)
    
    for i in rmv:
        if i not in possibilidades2: next
        else: possibilidades2.remove( i )

    # print(possibilidades2,"\n ** \n")

    rmv = []
    flag = False
    for i in possibilidades2: # [ 1,2 ,3 ...]
        #print("i before for: >>", i, "--\n")
        for j in range(2,len(i)): 
            #print("i>> ||", i ,"i[j]: >> ", i[j-1] ," || j: >>", i[j] ," || matriz[ ", i[j-1]-1," ][ ",i[j] - 1," ]: ",matriz[ i[j-1]-1 ][ i[j] - 1 ], "\n")
            if matriz[ i[j-1]-1 ][ i[j] - 1 ] == 0:
                #print("entrou ^")
                rmv.append(i)
                break
    
    for i in rmv:
        if i not in possibilidades2: next
        else: possibilidades2.remove( i )    
    

    
    # print(possibilidades2)
    encontra_sol(possibilidades2,matriz)
    #return possibilidades2



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






# def caixeiro_viajante(deslocamento, vertice, matriz, caminho, melhor_custo, melhor_caminho): #talvez C seja a matriz?
#     if deslocamento == len(matriz):
#         custo = caminho[0][ caminho[1] ]
#         for v in range(2,len(caminho):
#             custo +=  matriz[  caminho[v-1] ][caminho[v]]

#         if custo < melhor_custo:
#             melhor_custo = custo
#             melhor_caminho = caminho

#     if (deslocamento == 0):


# caixeiro ( distancia l ):
# global C_l onde eh o custo da distancia , distancia (l = 0,1, .. n-1)
# if distancia l = nivel | vertices (?)
#   entao: C <- custo ( vertices da solucao (?) [x0 ... x-1])
#       if C < Custo otimo:
#       entao: Custo otimo <- C
#               Caminho otimo <- [x0 ... x-1]
# if distancia l = 0
#   entao C_l <- {0}
#   se nao :
#       if distancia l = 1
#       entao: C_l <- {1...n-1}
#        senao: C_l <- C_l-1 (custo anterior?) \ (divido ou exclusao?) { x_l-1 }
#   para cada x pertencente ao C_l:
#   faca: x_l <- x
#         caixeiro(l+1) 



    
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