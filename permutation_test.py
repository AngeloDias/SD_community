import pandas as pd
import numpy as np
import re
import time
import sys


def evaluateRule(rule, example):
    return all(map(lambda x: example[x[0]]==x[1], rule[0]))

def Qg(rule,df,target='community'):    
    examples = df.apply(lambda x: evaluateRule(rule,x), axis=1)
    tp = np.sum(df.loc[examples,target]==int(rule[1]))
    fp = np.sum(examples) - tp
#    print(tp,fp,np.argwhere(examples))
    return tp/(fp+1.0)


def permutation_test(rule,matrix,target='community',repetition=1000,seed=time.time()):
    np.random.seed(int(seed))    
    df = matrix.copy()
    def randomtest(i):        
        df.loc[:,target] = np.random.permutation(df[target])     
        return Qg(rule,df,target)
    return np.fromfunction(np.vectorize(randomtest),shape=(repetition,))


if __name__ == '__main__':

	if len(sys.argv) < 5:
		print('Numero insuficiente de argumentos.\n\
			Uso: python3 {} <repetition> <file_regras> <file_data> <out_file_qg_permutation>.'.format(sys.argv[0]))
		sys.exit(0)
	
	rep = int(sys.argv[1])
	arq_regras = sys.argv[2]	
	arq_dados = sys.argv[3]
	arq_qg_permutation = sys.argv[4]
	
	regex_regra = re.compile('{(.*?)}->(\w+)')
	regex_feat_value = re.compile('([\w\s]+)=([\w\s]+),?')

	with open(arq_regras) as f:    
	    regras = [regex_regra.match(a).groups() for a in f]
	    regras = [(regex_feat_value.findall(cond),target) for cond,target in regras]

	data_matrix = pd.read_csv(arq_dados)

	with open(arq_qg_permutation,'w') as f:
	    pvalue = []
	    for rule in regras:
	        a = permutation_test(rule,data_matrix,repetition=rep,seed=0)
	        f.write(','.join(map(lambda x: '{0:.3g}'.format(x),a)))
	        f.write('\n')        
	        f.flush()
	        qg = Qg(rule,data_matrix)
	        pvalue.append((np.sum(a>qg)+1)/(rep+1.0))
	print(','.join(map(lambda x: '{0:5e}'.format(x),pvalue)))

