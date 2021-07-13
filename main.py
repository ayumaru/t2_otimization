#!/usr/bin/env python3
import numpy as np
import fileinput

melhor_caminho = []
   
# garantir que nao volta pelo caminho que acabei de passar
# no if da linha 22
def CaminhadaDFS_v1(vertice, visitados, matrizADJ, caminho, peso):

	if vertice not in caminho:
		caminho.append(vertice)
	#print("visitados[v] >> ", visitados[vertice], "\n ")
	if ( visitados[vertice] ):
		if (vertice == 0): #encontrou um caminho 
			#print("Achou um caminho :: caminho",caminho, "\n")
			if caminho not in melhor_caminho:
				melhor_caminho.append( ( caminho.copy(), "peso:: " +str(peso) ) ) 
			#	print("melhor caminho l18 >> ::: ", melhor_caminho, "\n")
		caminho = []
		peso = 0
		#print("melhor caminho aqui >> ", melhor_caminho, end="\n")
		return #melhor_caminho
		
	visitados[vertice] =  True

	for j in range( len( matrizADJ[vertice]) ):
		if vertice != j: 
			#print("caminho>> ", caminho[:-1]," | j >>>  ",j,"| vertice >>  " , vertice)
			if ( matrizADJ[vertice][j] != 0 ): #and caminho[:-1] != j ): # and not visitados[j]):
				peso+= matrizADJ[vertice][j]
				caminho.append(j)
			#	melhor_caminho.append( [vertice,j] )
			#	caminho.append( ( str(vertice)+"->"+ str(j) ) )
				CaminhadaDFS_v1(j, visitados, matrizADJ, caminho, peso)
				peso -= matrizADJ[vertice][j]
				caminho.pop()
	
	visitados[vertice] = False
	return #-1 #melhor_caminho


def BuscaEmProdundidade(matriz, qtdVertices):
	visitados = [False for i in range(qtdVertices)]
	caminho = []
	peso = 0
	CaminhadaDFS_v1(0, visitados, matriz, caminho, peso)
	print(" melhor caminho: >>> ", melhor_caminho, end="\n")
	


def Tratamento(dado, matriz_pesos):
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



def Leitura():
	entrada = []
	for linha in fileinput.input():
		entrada.append( linha.rstrip() )
	
	n = int(entrada[0])
	matriz_pesos = np.zeros( (n,n) , dtype=int)
	entrada = entrada[1:]
	matriz_pesos = Tratamento(entrada, matriz_pesos)
	
	return matriz_pesos, n










	
def main():
	matriz, n = Leitura() # retorna um np array da matriz simetrica dos pesos do grafo
	print(matriz)
	BuscaEmProdundidade(matriz, n) 
	
if __name__ == "__main__":
	main()


#gerar uma matriz so de 0 com tamanho n por n
#fazer a transposta e somar as duas.