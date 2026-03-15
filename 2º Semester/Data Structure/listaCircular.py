class No:
    def __init__(self,val):
        self.valor=val
        self.prox=None
        self.ant=None

class ListaCircular:
    def __init__(self):
        self.ini=None
        self.fim=None
    def inserirIni(self,val):
        novo_no=No(val)
        #lista vazia
        if self.ini is None:
            self.ini=novo_no
            self.fim=novo_no
            novo_no.prox=novo_no
            novo_no.ant=novo_no
        else:
            novo_no.prox=self.ini
            novo_no.ant=self.fim
            self.ini.ant=novo_no
            self.fim.prox=novo_no
            self.ini=novo_no
    def imprimir(self):
        atual=self.ini
        if atual is not None:
            while atual!=self.fim:
                print(atual.valor)
                atual=atual.prox
            print(self.fim.valor)

listaC=ListaCircular()
listaC.inserirIni("teste")
listaC.inserirIni("Ola")
listaC.inserirIni("Mundo")
listaC.imprimir()
        