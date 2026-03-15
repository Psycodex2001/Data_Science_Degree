import numpy as np
import random

matriz = []
tabela = np.array([])
lista_q = 0
desvio_q = 0
soma_desv_pad = 0

for l in range(10):
    linha = []
    for c in range(5):
        x = random.randint(1, 5)
        linha.append(x)
    matriz.append(linha)

answer = [[3, 3, 1, 3, 3], [5, 4, 2, 4, 5], [4, 3, 1, 3, 5], [4, 3, 2, 3, 5], [5, 3, 2, 3, 4],
          [4, 2, 2, 4, 5], [3, 3, 1, 3, 4], [3, 4, 2, 3, 5], [5, 4, 3, 3, 5], [5, 4, 2, 2, 4]]


tabela = np.array(answer)

print("Simulação aleatória das respostas dadas por 10 pessoas:\n\n", tabela, '\n')

def desvio(lista):
    media = (sum(lista))/10
    lista[0] = (lista[0]-media)**2
    lista[1] = (lista[1]-media)**2
    lista[2] = (lista[2]-media)**2
    lista[3] = (lista[3]-media)**2
    lista[4] = (lista[4]-media)**2
    lista[5] = (lista[5]-media)**2
    lista[6] = (lista[6]-media)**2
    lista[7] = (lista[7]-media)**2
    lista[8] = (lista[8]-media)**2
    lista[9] = (lista[9]-media)**2
    resultado = ((sum(lista))/10)**(1/2)
    return resultado


for i in range(0, 5):
    lista_q = []
    for j in range(0, 10):
        lista_q.append(tabela[j,i])
    desvio_q = desvio(lista_q)
    print("O desvio padrão populacional das respostas obtidas com a questão %i é: %.17f" %(i, desvio_q))
    soma_desv_pad = soma_desv_pad + desvio_q

formula_var = (soma_desv_pad)/5
print("\nA medida geral de variabilidade é: ", formula_var)

tam_amostra = ((1.96 * formula_var)/0.2)**2

print("\nO tamanho mínimo da amostra para realização da pesquisa é: ",tam_amostra)
