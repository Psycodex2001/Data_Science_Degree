class No:
    def __init__(self,val):
        self.esq=None
        self.dir=None
        self.val=val
class ArvoreBinBusca:
    def __init__(self):
        self.raiz=None

    def inserirRec(self,raiz,val):
        if raiz is None:
            return No(val)
        if val<raiz.val:
            raiz.esq= self.inserirRec(raiz.esq,val)
        else:
            raiz.dir= self.inserirRec(raiz.dir,val)
        return raiz
    
    def buscaBinRec(self,raiz,val):
        if raiz is None:
            return False
        elif val==raiz.val:
            return True
        elif val<raiz.val:
            return self.buscaBinRec(raiz.esq,val)
        else:
            return self.buscaBinRec(raiz.dir,val)

    def inserirVal(self,val):
        if self.raiz is None:
            self.raiz=No(val)
        else:
            self.inserirRec(self.raiz,val)

    def imprimirEmOrdem(self,raiz):
        if raiz is not None:
            self.imprimirEmOrdem(raiz.esq)
            print(raiz.val)
            self.imprimirEmOrdem(raiz.dir)
    def imprimirComEsp(self,raiz,nivel):
        if raiz is not None:
            espacos=""
            for i in range(nivel):
                espacos+="  "
            print(espacos,raiz.val)
            self.imprimirComEsp(raiz.esq,nivel+1)
            self.imprimirComEsp(raiz.dir,nivel+1)
    def alturaArv(self,raiz):
        if raiz is None:
            return 0
        altEsq=self.alturaArv(raiz.esq)+1
        altDir=self.alturaArv(raiz.dir)+1
        return max(altEsq,altDir)

import random

arv= ArvoreBinBusca()
for i in range(10):
    arv.inserirVal(random.randint(0,100000))
#arv.imprimirComEsp(arv.raiz,0)
print("altura",arv.alturaArv(arv.raiz))
print(arv.buscaBinRec(arv.raiz,6))
