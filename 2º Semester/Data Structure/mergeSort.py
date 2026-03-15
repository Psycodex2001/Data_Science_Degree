from math import floor
def mergeSort(vetor,ini,fim):
    tam=fim-ini+1
   
    if tam>1:
       
        #primeira metade
        mergeSort(vetor,ini,ini+floor(tam/2)-1)
        #sewgunda metade
        mergeSort(vetor,ini+floor(tam/2),fim)
        
        vetor1=vetor[ini:(ini+floor(tam/2))]
        vetor2=vetor[(ini+floor(tam/2)):fim+1]
        
        indice=ini
        indice_v1=0
        indice_v2=0
        while indice_v1<len(vetor1) and indice_v2<len(vetor2):
            if vetor1[indice_v1]<vetor2[indice_v2]:
                vetor[indice]=vetor1[indice_v1]
                indice_v1+=1
            else:
                vetor[indice]=vetor2[indice_v2]
                indice_v2+=1
            indice+=1
        for i in range(indice_v1,len(vetor1)):
            vetor[indice]=vetor1[i]
            indice+=1
        for i in range(indice_v2,len(vetor2)):
            vetor[indice]=vetor2[i]
            indice+=1
import random
vetor=[random.randint(0,100000) for x in range(1000)]
import time
t_i=time.time()
mergeSort(vetor,0,len(vetor)-1)
print("tempo",time.time()-t_i)
    