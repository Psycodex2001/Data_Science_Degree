
def selectionSort(vetor):
    #print(vetor)
    for i in range(len(vetor)-1):
        menor=i
        for j in range(i,len(vetor)):
            if vetor[j]<vetor[menor]:
                menor=j
        (vetor[i],vetor[menor])=(vetor[menor],vetor[i])
        #print(vetor)
    #print(vetor)
import random
vetor=[ random.randint(0,1000000) for x in range(1000)]
import time
t=time.time()
selectionSort(vetor)
print("tempo",time.time()-t)



