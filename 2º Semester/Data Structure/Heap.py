class Heap:
    def __init__(self):
        self.vetor=[]
    def inserirHeap(self,valor):
        self.vetor.append(valor)
        i=len(self.vetor)-1
        while i>0:
            pai=int((i-1)/2)
            #maior que o pai
            if self.vetor[i]>self.vetor[pai]:
                aux=self.vetor[pai]
                self.vetor[pai]=self.vetor[i]
                self.vetor[i]=aux
                i=pai
            else:
                break

    def remover(self):
        ult=len(self.vetor)-1
        self.vetor[0],self.vetor[ult]=self.vetor[ult],self.vetor[0]
        val=self.vetor.pop()
        i=0
        while i*2+1<ult:
            f1=i*2+1
            f2=i*2+2
            max_f=f1
            if f2<ult and self.vetor[f2]>self.vetor[f1]:
                max_f=f2
            
            if self.vetor[i]<self.vetor[max_f]:
                self.vetor[i],self.vetor[max_f]=self.vetor[max_f],self.vetor[i]
                i=max_f
            else:
                break
        return val
    
    def consultaTopo(self):
        if len(self.vetor)>0:
            return self.vetor[0]
        return None
    
maxheap=Heap()
maxheap.inserirHeap(8)
maxheap.inserirHeap(1)
maxheap.inserirHeap(20)
maxheap.inserirHeap(3)
maxheap.inserirHeap(15)
maxheap.inserirHeap(25)
maxheap.inserirHeap(4)
print(maxheap.vetor)
while len(maxheap.vetor)>0:
    print(maxheap.remover())


