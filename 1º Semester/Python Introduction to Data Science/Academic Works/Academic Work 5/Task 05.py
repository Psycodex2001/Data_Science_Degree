import pandas as pd
from math import ceil

# Leitura e transformção do Excel em Data Frame
worksheet = pd.read_excel("tabela 1.xlsx")
print(worksheet)
# Quantidade de cada legenda nos dados
legends = ["C", "B", "R", "N", "I"]
for legend in legends:
    globals()[legend.lower()] = worksheet[worksheet["Legendas"] == legend].count()
# Atribuindo apenas a quantidade de cada legenda concatenados em uma lista
quantity = [int(c.at["Legendas"]), int(b.at["Legendas"]), int(r.at["Legendas"]),
            int(n.at["Legendas"]), int(i.at["Legendas"])]
# Atribuindo apenas a porcentagem de cada legenda concatenados em uma lista
percentages = [float(f"{row / 35 * 100:.2f}") for row in quantity]
percentage_format = []
for percent in range(len(quantity)):
    percentage_format.append(f"{percentages[percent]}%")
# 1. Data Frame indicando cada legenda e sua respectiva quantidade
quantity_legend = pd.DataFrame({"Legendas": ["C", "B", "R", "N", "I"], "Quantidade": quantity})
# 2. Data Frame indicando cada legenda e sua respectiva porcentagem
percentage_legend = pd.DataFrame({"Legendas": ["C", "B", "R", "N", "I"], "Quantidade": percentage_format})
# Menu opcional customizado
print(f"\nQuantidade de fabricantes para cada legenda:\n{quantity_legend}")
print(f"\nPercentual de fabricantes para cada legenda:\n{percentage_legend}")
# Recebe a legenda escolhida como entrada
option = input("\nDigite a legenda desejada para consulta: ").strip().upper()
# Seleciona os dados correspondentes à legenda
if option == "C":
    legend_chart = [quantity[0], percentages[0]]
elif option == "B":
    legend_chart = [quantity[1], percentages[1]]
elif option == "R":
    legend_chart = [quantity[2], percentages[2]]
elif option == "N":
    legend_chart = [quantity[3], percentages[3]]
elif option == "I":
    legend_chart = [quantity[4], percentages[4]]
# 3. Imprime a lista da legenda selecionada
print(f"""\nA legenda especificada possui as seguintes características:
Legenda solicitada: {option}
Quantidade de fabricantes: {legend_chart[0]}
Percentual desta legenda na amostra: {ceil(legend_chart[1])}%""")
