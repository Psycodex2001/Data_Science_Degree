from csv import reader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns

l1 = []
result = []

with open("cotação do dólar (venda).csv", "r") as dolar:
    data = reader(dolar)

##########

tabela = pd.read_csv("dolarAgosto.csv")

df = pd.DataFrame(tabela)

tam = len(df)

for i in range(1,tam):
  df['Variação percentual no dia'][i] = ((df['Cotação(Venda – R$)'][i])/(df['Cotação(Venda – R$)'][i-1])-1)*100

display(df)

X = []

for i in range(len(df['Data'])):
   X.append(int(df['Data'][i][0:2]))

Y = df['Variação percentual no dia']

Z = df["Cotação(Venda – R$)"]


fig = plt.figure(figsize=(15, 15))
ax = fig.add_subplot(projection='3d')

ax.set(xlabel=("Data"), ylabel=("Variação percentual do dia"), zlabel=("Cotação(Venda – R$)"))

ax.plot_trisurf(X, Y, Z, cmap = cm.coolwarm)
ax.set_title("GRÁFICO 3D - DATA, COTAÇÃO E PERCENTUAL DE VARIAÇÃO DIÁRIA DO DÓLAR\n\n")

plt.show()
