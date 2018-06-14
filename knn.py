#lista de amostras(cada lista vai conrespoder uma coluna)
treinamento=[]
teste=[]

#cada linha é uma amostra
with open('treinamento.txt', 'r') as f:
    for linha in f.readlines():
        
        atrib= linha.replace('\n','').split(',')
        treinamento.append( [ float(atrib[0]), float(atrib[1]), float(atrib[2]), float(atrib[3]), int(atrib[4]) ])


with open('teste.txt', 'r') as f:
    for linha in f.readlines():
       
        atrib= linha.replace('\n','').split(',')
        teste.append( [ float(atrib[0]), float(atrib[1]), float(atrib[2]), float(atrib[3]) ])

#aqui temos uma funcao so para pegar infmacoes da quantidade de rotulos
def info_dataset(treinamento, verbose=True):
    if(verbose):
        print('total de amostrat: %d' %len(treinamento))
    rotulo1, rotulo2, rotulo3 = 0, 0, 0
    for amostra in amostras:
        if(treinamento[-1] == 0):
            rotulo1+=1
        elif(treinamento[-1] == 1):
            rotulo2+=1

        else:
            rotulo3+=1
    if(verbose):
        print('total rotulo1: %d ' %rotulo1)
        print('total rotulo2: %d ' %rotulo2)
        print('total rotulo3: %d ' %rotulo3)
    
    return [len(treinamento), rotulo1, rotulo2, rotulo3]



import operator
from collections import Counter
import math

#aqui vamos fazer a distancia euclidiana

def dist_euclidiana(v1, v2):
    dim, soma= len(v1), 0
    for i in range(dim-1): #o -1 é para não pegar a saída
        soma+= math.pow(v1[i] - v2[i], 2)
    
    return math.sqrt(soma)


def knn(treinamento, nova_amostra, k):
    distancia = []
    
    #nova_amostra= dados de teste
    with open('result.txt','w') as f:
        for dado in nova_amostra:
            #dado= lista de teste
            dists_class, tam_treino = [], len(treinamento)
            #dists_class= pega a distancia eclidiana mais a sua classificacao
            for dado2 in treinamento:
                
                d = dist_euclidiana(dado, dado2)
                dists_class.append([d,dado2[4]])#passo a distancia e a classificao para a lista
            dists_class.sort(key=operator.itemgetter(0))#aqui faCo a ordenacao do menor para o maior, que nesse caso ordeno so pelas as distancias

            classificacao=[]#lista com classificao do tipo 0, 1 ou 2
            for i in range (k):
                classificacao.append(dists_class[i][1])
                
            cnt = Counter(classificacao)
            contador_dos_classificadores = (cnt.most_common()) #conta o valor mais comum da lista, so pego quem tem o maior valor
            print(contador_dos_classificadores)
            f.write(str(contador_dos_classificadores[0][0])+'\n')
            #print(classificacao)
           
                    


knn(treinamento,teste,1)

resultado=[]#o meu classifcador
with open('result.txt', 'r') as f:
    for linha in f.readlines():       
        atrib= linha.replace('\n','')
        resultado.append(atrib)


rotuloTes=[]
with open('rotulos-teste.txt', 'r') as f:
    for linha in f.readlines():       
        atrib= linha.replace('\n','')
        rotuloTes.append(atrib)


acertos=0.0
for i in range(len(rotuloTes)):
    if(rotuloTes[i] == resultado[i]):
        acertos+=1
        

cal= 100*(acertos/len(resultado))

print(cal)
       
                   



        
        

    
    

