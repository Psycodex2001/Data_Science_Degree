from math import floor
def buscaLinear(vetor,valor):
    for i in range(len(vetor)):
        if vetor[i]==valor:
            return i
    return False

def buscaBin(vetor,valor):
    cont=0
    ini=0
    fim=len(vetor)-1
    while ini<fim:
        cont+=1
        indice=floor((fim+ini)/2)
        if vetor[indice+1]==valor:
            print(cont)
            return indice+1
        if vetor[indice]==valor:
            print(cont)
            return indice
        if valor>vetor[indice]:
            ini=indice+1
        else:
            fim=indice-1        
    print(cont)


vetor = [i for i in range(1000000)]

#print(buscaLinear(vetor,1))
print(buscaBin(vetor,0))