matriz=[
    [1,0,0,0,0],
    [2,3,0,0,0],
    [4,5,6,0,0],
    [7,8,9,10,0],
    [11,12,13,14,15]
]

class MatrizLinear:
    def __init__(self,linhas,colunas):
        self.linhas=linhas
        self.colunas=colunas
        self.vetor = [0]*linhas*colunas
    def get(self,i,j):
        indice=self.colunas*i+j
        return self.vetor[indice]
    def set(self,i,j,val):
        indice=self.colunas*i+j
        self.vetor[indice]=val

class MatrizTriangularInf:
    def __init__(self,n):
        self.n=n
        self.vetor=[0]*int(((n+1)*n)/2)
    
    def get(self,i,j):
        if j>i:
            return 0
        indice=int(((i+1)*i)/2)
        indice+=j
        return self.vetor[indice]

    def set(self,i,j,val):
        if j>i:
            if val!=0:
                print("Matriz invalida")
        else:
            indice=int(((i+1)*i)/2)
            indice+=j
            self.vetor[indice]=val

matLinear=MatrizLinear(5,5)
matTriangular=MatrizTriangularInf(5)
for i in range(5):
    for j in range(5):
        matLinear.set(i,j,matriz[i][j])
        matTriangular.set(i,j,matriz[i][j])

print(matriz)
print(matLinear.vetor)
print(matTriangular.vetor)

for i in range(5):
    linha=""
    for j in range(5):
        linha+=str(matriz[i][j])+" "
    print(linha)

for i in range(3):
    linha=""
    for j in range(4):
        linha+=str(matLinear.get(i,j))+" "
    print(linha)


class MatrizEsparsa:
    def __init__(self,linhas,colunas):
        self.linhas=linhas
        self.colunas=colunas
        self.mat=[]
        for x in range(linhas):
            self.mat.append([])
        
    def get(self,i,j):
        lista=self.mat[i]
        for item in lista:
            if item[0]==j:
                return item[1]
        return 0
    def set(self,i,j,val):
        lista=self.mat[i]
        for item in lista:
            if item[0]==j:
                item[1]=val
                return
        lista.append([j,val])

matrizEsp=MatrizEsparsa(3,4)
matrizEsp.set(0,2,5.2)
matrizEsp.set(2,3,4)
matrizEsp.set(2,1,3)

print(matrizEsp.mat)
print("matriz esparsa")
for i in range(matrizEsp.linhas):
    linha=""
    for j in range(matrizEsp.colunas):
        linha+=str(matrizEsp.get(i,j))+" "
    print(linha)


