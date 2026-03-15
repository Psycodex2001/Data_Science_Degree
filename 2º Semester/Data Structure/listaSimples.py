class No:
    def __init__(self,valor):
        self.valor=valor
        self.prox=None

def imprimirLista(ini):
    atual=ini
    while atual is not None:
        print(atual.valor)
        atual=atual.prox

def inserirValor(valor, ini):
    novo_no=No(valor)
    if ini is not None:
        novo_no.prox=ini
    return novo_no

def inserirFinal(val,ini):
    novo_no=No(val)
    if ini is None:
        return novo_no
    ultimo=ini
    while ultimo.prox is not None:
        ultimo=ultimo.prox
    ultimo.prox=novo_no
    return ini

def removerElm(ini,valor):
    if ini is None:
        return ini
    if ini.valor==valor:
        ini=ini.prox
        return ini
    ant=ini
    atual=ini.prox
    while atual is not None:
        if atual.valor==valor:
            ant.prox=atual.prox
            break
        ant=atual
        atual=atual.prox
    return ini

iniLista = None
iniLista=inserirFinal(5,iniLista)
iniLista=inserirFinal(3,iniLista)
iniLista=inserirValor(1,iniLista)
iniLista=inserirFinal(4,iniLista)
iniLista=inserirFinal(8,iniLista)
imprimirLista(iniLista)
iniLista=removerElm(iniLista,5)
imprimirLista(iniLista)


