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

headerList = []
# {ID: {'rulesA': [], 'rulesB': [], 'intersection': [], 'somenteEmA': [], 'somenteEmB': []}}
dictCommunities = {}

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
					dictCommunities[cleanLine] = {'rulesA': [], 'rulesB': [], 'intersection': [], 'somenteEmA': [], 'somenteEmB': []}
					lastID = cleanLine
					gotFirstSetOfRules = False						
					countSets = 0

				elif '{' in cleanLine:
					if countSets < 20:
						dictCommunities[lastID]['rulesA'].append(cleanLine)
					else:
						dictCommunities[lastID]['rulesB'].append(cleanLine)

					countSets += 1

				if countSets > 0 and len(dictCommunities[lastID]['rulesB']) == 20:
					setA = set(dictCommunities[lastID]['rulesA'])
					setB = set(dictCommunities[lastID]['rulesB'])
					inter = list(setA.intersection(setB))
					dictCommunities[lastID]['intersection'] = inter
					dictCommunities[lastID]['somenteEmA'] = list(setA - setB)
					dictCommunities[lastID]['somenteEmB'] = list(setB - setA)

			if cleanLine == 'AND' or cleanLine == 'OR':
				readHeader = True

#	print(dictCommunities['6']['rulesA'])
#	print(len(dictCommunities['6']['rulesA']))
#	print(len(dictCommunities['6']['rulesB']))
# 	print 'Intersection:', dictCommunities['256']['intersection']
#	print 
# 	print 'Somente em B:', dictCommunities['256']['somenteEmB']
# 	print 'Size somente em B:', len(dictCommunities['256']['somenteEmB'])

colectDataFromFile('analise_doc_term_matriz_freq_with_header_discrete_AND.txt')
# colectDataFromFile('analise_doc_term_matriz_tfidf_with_header_discrete_AND.txt')

