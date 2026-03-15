from arvoreAVL import ArvoreAVL, ArvoreBinBusca
class NO:
    def __init__(self,val,nome):
        self.val=val
        self.nome=nome
        self.esq=None
        self.dir=None
        self.cor="Vermelho"

def rotacaoEsq(a):
    x=a.dir
    x.cor=a.cor
    a.dir=x.esq
    x.esq=a
    a.cor="Vermelho"
    return x

def rotacaoDir(a):
    x=a.esq
    x.cor=a.cor
    a.esq=x.dir
    x.dir=a
    a.cor="Vermelho"
    return x

def subidaVermelho(a):
    a.dir.cor="Preto"
    a.esq.cor="Preto"
    a.cor="Vermelho"

def ehVermelho(no):
    if no is None:
        return False
    else:
        return no.cor=="Vermelho"

def imprimirComEsp(raiz,nivel):
    if raiz is not None:
        esp=""
        for i in range(nivel):
            esp+="  "
        print(esp+str(raiz.val),raiz.cor)
        imprimirComEsp(raiz.esq,nivel+1)
        imprimirComEsp(raiz.dir,nivel+1)

class ArvoreRN:
    def __init__(self):
        self.raiz=None
    
    def inserir(self,val):
        self.raiz=self.inserirRec(val,self.raiz)
        self.raiz.cor="Preto"
    


    def inserirRec(self,val,raiz):
        if raiz is None:
            return NO(val)
        elif val<raiz.val:
            raiz.esq=self.inserirRec(val,raiz.esq)
        else:
            raiz.dir=self.inserirRec(val,raiz.dir)
        
        if ehVermelho(raiz.dir) and not ehVermelho(raiz.esq):
            raiz=rotacaoEsq(raiz)
        if ehVermelho(raiz.esq) and ehVermelho(raiz.esq.esq):
            raiz=rotacaoDir(raiz)
        if ehVermelho(raiz.esq) and ehVermelho(raiz.dir):
            subidaVermelho(raiz)
        
        return raiz
    
def calcAlt(raiz):
    if raiz is None:
        return 0
    altEsq=calcAlt(raiz.esq)
    altDir=calcAlt(raiz.dir)
    return max(altEsq,altDir)+1

avRN=ArvoreRN()
avl=ArvoreAVL()
abb=ArvoreBinBusca()
import random
for i in range(10000):
    val=random.randint(0,1000000)
    avRN.inserir(val)
    avl.inserir(val)
    abb.inserirVal(val)

#imprimirComEsp(avRN.raiz,0)  
print("Altura AVL",calcAlt(avl.raiz))
print("Altura ARN",calcAlt(avRN.raiz))  
print("Altura ABB",calcAlt(abb.raiz))  
