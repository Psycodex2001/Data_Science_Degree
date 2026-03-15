class NoB:
    def __init__(self,nchaves):
        self.chaves=[None for i in range(nchaves)]
        self.filhos=[None for i in range(nchaves+1)]
 
    def ehFolha(self):
        for f in self.filhos:
            if f is not None:
                return False
        return True
    def inserir(self,val):
        i=0
        for x in range(len(self.chaves)):
            i=len(self.chaves)-1-x
            i_f=i+1
            if i>0:
                self.chaves[i]=self.chaves[i-1]
                self.filhos[i_f]=self.filhos[i_f-1]
            if self.chaves[i] is not None:
                if val>self.chaves[i]:
                    break
        self.chaves[i]=val
        return i
             
            

def imprimirNivel(raiz,nivel):
    
    aux=""
    for i in range(nivel):
        aux+="  "
    for val in raiz.chaves:
        if val is not None:
            aux+=str(val)+" "
    print(aux)
    for f in raiz.filhos:
        if f is not None:
            imprimirNivel(f,nivel+1) 

class ArvoreB:
    def __init__(self,t):
        self.raiz=NoB(t*2-1)
        self.t=t
    def inserirVal(self,val):
        self.inserirRec(self.raiz,val)
    
    def dividir(self,raiz,val):
        
        pai=None
        if raiz==self.raiz:
            pai=NoB(self.t*2-1)
            self.raiz=pai
        else:       
            atual=self.raiz
            while atual is not None:
                if raiz in atual.filhos:
                    pai=atual
                    break
                else:
                    for i in range(len(atual.chaves)+1):
                        if i==len(atual.chaves) or atual.chaves[i] is None or val<atual.chaves[i]:
                            atual=atual.filhos[i]
                            break
            
        if None in pai.chaves:
            val= raiz.chaves[self.t-1]
            i=pai.inserir(val)
            f1=NoB(self.t*2-1)
            f2=NoB(self.t*2-1)
            for i_1 in range(self.t-1):
                f1.chaves[i_1]=raiz.chaves[i_1]
                f1.filhos[i_1]=raiz.filhos[i_1]
            f1.filhos[self.t-1]=raiz.filhos[self.t-1]

            for i_2 in range(self.t,len(raiz.chaves)+1):
                if i_2<len(raiz.chaves):
                    f2.chaves[i_2-self.t]=raiz.chaves[i_2]
                f2.filhos[i_2 - self.t]=raiz.filhos[i_2]

            
            
            pai.filhos[i]=f1
            pai.filhos[i+1]=f2
        else: 
            self.dividir(pai,val)
        return pai

    def inserirRec(self,raiz,val):
        if raiz.ehFolha():
            if None in raiz.chaves:
                raiz.inserir(val)
                return
            else:
                raiz=self.dividir(raiz,val)
            
        for i in range(len(raiz.chaves)+1):
            if i==len(raiz.chaves) or raiz.chaves[i] is None or val<raiz.chaves[i]:
                self.inserirRec(raiz.filhos[i],val)
                break

    def imprimir(self):
        imprimirNivel(self.raiz,0)

def calcAlt(raiz):
    if raiz is None:
        return 0
    maior=0
    for f in raiz.filhos:
        alt= calcAlt(f)
        if alt>maior:
            maior=alt
    return maior+1
        
arvB=ArvoreB(5)


for i in range(500000):
    arvB.inserirVal(i)

print("Altura ",calcAlt(arvB.raiz))
#arvB.imprimir()




