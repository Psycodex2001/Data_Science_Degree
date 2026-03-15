from arvorebinBusca import ArvoreBinBusca

class No:
    def __init__(self,val):
        self.esq=None
        self.dir=None
        self.val=val

def rotacaoEsq(y):
    x=y.dir
    y.dir=x.esq
    x.esq=y
    return x

def rotacaoDir(y):
    x=y.esq
    y.esq=x.dir
    x.dir=y
    return x

def rotacaoRL(y):
    y.dir=rotacaoDir(y.dir)
    return rotacaoEsq(y)
def rotacaoLR(y):
    y.esq=rotacaoEsq(y.esq)
    return rotacaoDir(y)

def calcAlt(raiz):
    if raiz is None:
        return 0
    altesq=calcAlt(raiz.esq)+1
    altdir=calcAlt(raiz.dir)+1
    return max(altesq,altdir)

def fatorBalanceamento(raiz):
    return calcAlt(raiz.esq)-calcAlt(raiz.dir)


class ArvoreAVL:
    def __init__(self):
        self.raiz=None
    
    def inserirRec(self,raiz,val):
        if raiz is None:
            return No(val)
        elif val<raiz.val:
            raiz.esq=self.inserirRec(raiz.esq,val)
        else:
            raiz.dir=self.inserirRec(raiz.dir,val)
        
        fatorR=fatorBalanceamento(raiz)
        if fatorR==-2:
            fatorDir=fatorBalanceamento(raiz.dir)
            #caso RR
            if fatorDir ==-1:
                raiz=rotacaoEsq(raiz)
            #caso RL
            elif fatorDir == 1:
                raiz=rotacaoRL(raiz)
        elif fatorR==2:
            fatorEsq=fatorBalanceamento(raiz.esq)
            #caso LL
            if fatorEsq==1:
                raiz=rotacaoDir(raiz)
            #caso LR
            elif fatorEsq==-1:
                raiz=rotacaoLR(raiz)

        return raiz
    def inserir(self,val):
        self.raiz=self.inserirRec(self.raiz,val)

    def imprimirEmOrdem(self,raiz):
        if raiz is not None:
            self.imprimirEmOrdem(raiz.esq)
            print(raiz.val)
            self.imprimirEmOrdem(raiz.dir)
    

#avl=ArvoreAVL()
#abb=ArvoreBinBusca()
#avl.inserir(10)
#avl.inserir(9)
#avl.inserir(8)
#print("Raiz",avl.raiz.val)
#avl.inserir(7)
#import random
#import time
#t=time.time()
#for i in range(0):
#    val=random.randint(0,100000)
#    avl.inserir(val)
#    abb.inserirVal(val)
#print(time.time()-t)
#print("Altura AVL:",calcAlt(avl.raiz))
#print("Altura ABB:",calcAlt(abb.raiz))



#avl.imprimirEmOrdem(avl.raiz)




    