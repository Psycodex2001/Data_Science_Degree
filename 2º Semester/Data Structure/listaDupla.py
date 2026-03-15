class No:
    def __init__(self,valor):
        self.valor=valor
        self.ant=None
        self.prox=None

class ListaDupla:
    def __init__(self):
        self.inicio=None
        self.ultimo=None

    def inserirFinal(self,val):
        novo_no=No(val)
        novo_no.ant=self.ultimo
        #lista vazia
        if self.inicio is None:
            self.inicio=novo_no
            self.ultimo=novo_no
        else:
            self.ultimo.prox=novo_no
            self.ultimo=novo_no
    
    def removerElm(self,val):
        no_val=self.inicio
        while no_val is not None:
            if no_val.valor==val:
                break
            no_val=no_val.prox
        if no_val is not None:
            if no_val.prox is not None:
                no_val.prox.ant=no_val.ant
            if no_val.ant is not None:
                no_val.ant.prox=no_val.prox
            if no_val == self.inicio:
                self.inicio=no_val.prox
            if no_val == self.ultimo:
                self.ultimo=no_val.ant


    def inserirIni(self,val):
        novo_no=No(val)
        novo_no.prox=self.inicio
        if self.ultimo is None:
            self.ultimo=novo_no
        if self.inicio is not None:
            self.inicio.ant=novo_no
        self.inicio=novo_no
    def imprimirRev(self):
        atual=self.ultimo
        while atual is not None:
            print(atual.valor)
            atual=atual.ant
    def imprimir(self):
        atual=self.inicio
        while atual is not None:
            print(atual.valor)
            atual=atual.prox

lista=ListaDupla()
lista.inserirIni(5)
lista.inserirIni(2)
lista.inserirIni(8)
lista.removerElm(5)
lista.imprimir()
lista.imprimirRev()

