#!/usr/bin/env python3
import numpy as np
import fileinput
import copy
from datetime import datetime

melhor_caminhoBB = []
melhor_caminho = []
melhor_peso = 0
melhor_pesoBB = 0
nodos_BB = 0
nodos = 0

'''
falta fazer: adicionar medida de tempo, e se possivel quantidade de nos expandidos 
'''

# antes de chamar vou ter que ter numa var global o maior caminho e o maior peso
def bounding(vertice, visitados, matrizADJ, caminho, peso):
	global melhor_pesoBB

	#print("dentrou do bounding, caminho:: ", caminho)
	tam =  len(matrizADJ) - len(caminho)
	p_max = [ 0 for i in range(tam) ] 
	o = 0
	possiveis = []
	for i,_ in enumerate(visitados):
		if not visitados[i]: #true entao vira false
			for m in range(len(matrizADJ)):
				if m not in caminho:
					p_max[o] +=  matrizADJ[i][m]   # a soma das linhas dos vertices que ainda faltam podem ser melhor que o que ja temos
			o+=1		
	
	if p_max != []:
		if peso + max(p_max) < melhor_pesoBB:
			return False 
	
	return True

	
# Partindo de uma verificacao se existe aquele arco ou nao
# Varro a matriz de adjacencia na linha do possivel com os outros possiveis e somo os elementos || ou pego o maior 
# Repito para os outros, retorno o maximo possivel dentre eles e comparo com o maior ja achado
# Se for maior, deixa continuar
# 	caso contrario, esvazia o caminho, e retorna o maior caminho 




# verificar a linha de cada um dos que sobraram e ver o maximo, se a soma deles for maior que o peso atual continua. Caso contrario para
# 

## versao branch and bound
def CaminhadaDFS_BB(vertice, visitados, matrizADJ, caminho, peso):
	global melhor_pesoBB
	global melhor_caminhoBB
	global nodos_BB

	if vertice not in caminho:
		caminho.append(vertice)

	if ( visitados[vertice] ):
		if (vertice == 0): #encontrou um caminho 
			#print(caminho)
			if ( 1+len(caminho) - caminho.count(0) ) > 2:
				if peso > melhor_pesoBB:
					melhor_caminhoBB = caminho.copy() 
					melhor_pesoBB = peso

		caminho = []
		peso = 0
		
		return

	nodos_BB += 1
	visitados[vertice] =  True

	if not( bounding(vertice, visitados, matrizADJ, caminho, peso) ): 
		if caminho != []:
			caminho.pop()
		return

	for j in range( len( matrizADJ[vertice]) ):
		if vertice != j: 
			#print("caminho>> ", caminho[:-1]," | j >>>  ",j,"| vertice >>  " , vertice)
			
			if ( matrizADJ[vertice][j] != 0 ): 
				peso+= matrizADJ[vertice][j]
				caminho.append(j)

				CaminhadaDFS_BB(j, visitados, matrizADJ, caminho, peso)

				peso -= matrizADJ[vertice][j]
				if caminho != []:
					caminho.pop()
	
	visitados[vertice] = False
	return 


def CaminhadaDFS_v1(vertice, visitados, matrizADJ, caminho, peso):
	global melhor_peso
	global melhor_caminho
	global nodos

	if vertice not in caminho:
		caminho.append(vertice)

	if ( visitados[vertice] ):
		if (vertice == 0): #encontrou um caminho 
			# print("melhor caminho::: ", melhor_caminho, " || :: caminho >> ", caminho, "|| peso::", peso, "|| melhor peso::", melhor_peso, "\n" ) 
			if ( 1+len(caminho) - caminho.count(0) ) > 2: #so tem o vertice inicial e outro [ 0-> 1-> 0]
				if peso > melhor_peso:
					melhor_caminho = caminho.copy() 
					melhor_peso = peso
			
		caminho = []
		peso = 0
		#print("melhor peso depois do peso =0 ", melhor_caminho)
		return

	nodos+=1
	visitados[vertice] =  True

	for j in range( len( matrizADJ[vertice]) ):
		if vertice != j: 
			#print("caminho>> ", caminho[:-1]," | j >>>  ",j,"| vertice >>  " , vertice)
			
			if ( matrizADJ[vertice][j] != 0 ): #and caminho[:-1] != j ): # and not visitados[j]):
				peso+= matrizADJ[vertice][j]
				caminho.append(j)

				CaminhadaDFS_v1(j, visitados, matrizADJ, caminho, peso)#, melhor_peso)

				peso -= matrizADJ[vertice][j]
				caminho.pop()
	
	visitados[vertice] = False
	return 

def BuscaEmProdundidade(matriz, qtdVertices):
	visitados = [False for i in range(qtdVertices)]
	caminho = []
	
	peso = 0
	print("dfs :: ")
	dfs_time = datetime.now()
	CaminhadaDFS_v1(0, visitados, matriz, caminho, peso)#, melhor_peso)
	dfs_time = datetime.now() - dfs_time

	for i in melhor_caminho:
		print(i+1, "->", end=" ")
	print("\n peso:: ", melhor_peso, "\n nodos::", nodos, "\n tempo:: ", dfs_time)


	peso = 0
	print("dfsBB:: ")
	dfs_time = datetime.now()
	CaminhadaDFS_BB(0, visitados, matriz, caminho, peso)
	dfs_time = datetime.now() - dfs_time
	#print(" melhor caminho: >>> ", melhor_caminho,"\n m_peso:: ", melhor_peso ,end="\n")
	for i in melhor_caminhoBB:
		print(i+1, "->", end=" ")
	print("\n peso:: ", melhor_pesoBB, "\n nodos::", nodos_BB, "\n tempo:: ", dfs_time)

	#print(" melhor caminho: >>> ", melhor_caminhoBB,"\n m_peso:: ", melhor_pesoBB ,end="\n")




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



def verificacao_integridade(entrada, n, matriz_pesos):
	
	if n < 3:
		exit("Quantidade de nodos insuficiente, N precisa ser maior que 2.")
	
	numeros = []
	i = 0
	j = 1
	jj = 1
	k = 1

	if entrada == []:
		exit("Elementos insuficientes. Quantidade de elementos por linha tem que ser N-i, onde i= [0..n]")
	
	for pesos in entrada:
		temp = pesos.split()
		if ( len(temp) != n-k ):
			exit("Quantidade de elementos fornecidos por linha estao errados. Quantidade de elementos por linha tem que ser N-i, onde i= [0..n]")
		else:
			for v in temp:
				if v.isdigit():
					matriz_pesos[i][j] = int(v)
					j+=1
				else:
					exit("Formato de dados da matriz incorreto")
		k+=1
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
	#matriz_pesos = Tratamento(entrada, matriz_pesos)
	
	matriz_pesos = verificacao_integridade(entrada, n, matriz_pesos)

	return matriz_pesos, n


	
def main():
	
	matriz, n = Leitura() # retorna um np array da matriz simetrica dos pesos do grafo
	print(matriz)
	BuscaEmProdundidade(matriz, n) 
	
if __name__ == "__main__":
	main()




