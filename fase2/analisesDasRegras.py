# coding=utf-8

# Arquivo de análise usando a frequência: analise_doc_term_matriz_freq_with_header_discrete_AND.txt
# Arquivo de análise usando tf-idf: analise_doc_term_matriz_tfidf_with_header_discrete_AND.txt

############################# Sequência de leitura #############################
# Nome do arquivo que gerei para a análise
# Nome do arquivo que o professor gerou para a análise
# Nome do arquivo base usado para gerar os grupos
# Número total Colunas (atributos)
# Número total de Linhas (exemplos/amostras)
# Nome da métrica de avaliação
# Operador entre características usado pelo SSDP
########## // A partir daqui se repete até a última classe // ##########
# Quebra de linha
# Número identificador da classe avaliada
# Quebra de linha
# O conjunto de regras gerado a partir do PageRank
# Quebra de linha
# O conjunto de regras gerado a partir do total
############################# Sequência de leitura #############################

import pandas as pd

headerList = []
# {ID: {'rulesA': [], 'rulesB': [], 'intersection': [], 'somenteEmA': [], 'somenteEmB': []}}
# dfCommunity = {}
dfCommunity = pd.DataFrame(columns=['rulesA', 'rulesB', 'intersection', 'somenteEmA', 'somenteEmB'])
# dfCommunity = pd.DataFrame()

def colectDataFromFile(fileName):
	readHeader = False

	with open('./testingPageRank/' + fileName) as f:
		lastID = ''
		gotFirstSetOfRules = False
		countSets = 0

		for line in f:
			cleanLine = line.replace('\n','').strip()

			if not readHeader:
				headerList.append(cleanLine)
			else:
				if cleanLine.isdigit():
					dfCommunity = pd.DataFrame(columns=['rulesA', 'rulesB', 'intersection', 'somenteEmA', 'somenteEmB'])
					# dfCommunity[cleanLine] = {'rulesA': [], 'rulesB': [], 'intersection': [], 'somenteEmA': [], 'somenteEmB': []}
					lastID = cleanLine
					gotFirstSetOfRules = False
					countSets = 0

				elif '{' in cleanLine:
					cleanLine = cleanLine[1:-1]

					if countSets < 20:
						dfCommunity['rulesA'].append(cleanLine)
					else:
						dfCommunity['rulesB'].append(cleanLine)

					countSets += 1

				if countSets > 0 and len(dfCommunity['rulesB']) == 20:
					setA = set(dfCommunity['rulesA'])
					setB = set(dfCommunity['rulesB'])
					inter = list(setA.intersection(setB))
					dfCommunity['intersection'] = inter
					dfCommunity['somenteEmA'] = list(setA - setB)
					dfCommunity['somenteEmB'] = list(setB - setA)

					# dfCommunity = pd.DataFrame.from_dict(dfCommunity[lastID])

					dfCommunity.to_csv('fase2/filesResults/rules_community_' + lastID + '.csv', header=True, index=False, sep=';')

			if cleanLine == 'AND' or cleanLine == 'OR':
				readHeader = True

#	print(dfCommunity['6']['rulesA'])
#	print(len(dfCommunity['6']['rulesA']))
#	print(len(dfCommunity['6']['rulesB']))
# 	print 'Intersection:', dfCommunity['256']['intersection']
#	print ()
	print ('Somente em B:', dfCommunity['256']['somenteEmB'])
	print ('Size somente em B:', len(dfCommunity['256']['somenteEmB']))

colectDataFromFile('analise_doc_term_matriz_freq_with_header_discrete_AND.txt')
# colectDataFromFile('analise_doc_term_matriz_tfidf_with_header_discrete_AND.txt')

