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
dictCommunities = {ID: '', rulesA: [], rulesB: []}

def readFiles(fileName):
	readHeader = False

	with open('../testingPageRank/' + fileName) as f:
		lastID = ''
		gotFirstSetOfRules = False

		for line in f:
			cleanLine = line.replace('\n','').strip()

			if not readHeader:
				headerList.append(cleanLine)
			else:
				if cleanLine.isdigit():
					dictCommunities[ID] = cleanLine
					lastID = cleanLine
					gotFirstSetOfRules = False

				elif '{' is in cleanLine:
					

			if cleanLine == 'AND' or cleanLine == 'OR':
				readHeader = True

readFiles('analise_doc_term_matriz_freq_with_header_discrete_AND.txt')