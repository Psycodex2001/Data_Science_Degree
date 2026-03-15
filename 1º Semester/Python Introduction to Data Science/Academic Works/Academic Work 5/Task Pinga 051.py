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
total = (total + quantity[number] for number in quantity)
# Atribuindo apenas a porcentagem de cada legenda concatenados em uma lista
percentages = [[float(row / total * 100) for row in quantity], [float(f"{row / total * 100:.2f}") for row in quantity]]
percentage_format = [[], []]
for percent in range(len(quantity)):
    percentage_format[0].append(f"{percentages[0][percent]}%")
    percentage_format[1].append(f"{percentages[1][percent]}%")
# 1. Data Frame indicando cada legenda e sua respectiva quantidade
quantity_legend = pd.DataFrame({"Legendas": ["C", "B", "R", "N", "I"], "Quantidade": quantity})
# 2. Data Frame indicando cada legenda e sua respectiva porcentagem
percentage_legend = pd.DataFrame({"Legendas": ["C", "B", "R", "N", "I"], "Quantidade": percentage_format[1]})
# 4. Porcentagem bruta
raw_percentage_legend = pd.DataFrame({"Legendas": ["C", "B", "R", "N", "I"], "Quantidade": percentage_format[0]})
# Menu opcional customizado
option = 999
while option != 0:
    option = int(input("""\nSelecione a opção desejada:

    [ 1 ] Quantidade de todas legendas
    [ 2 ] Porcentagem de todas legendas
    [ 3 ] Porcentagem bruta de todas legendas
    [ 4 ] Escolher os dados de apenas uma legenda
    [ 0 ] Sair

    Selecione um número: """))
    while option not in [0, 1, 2, 3, 4]:
        option = int(input("""\nNão chora que já está uma mamata, selecione um número novamente: """))
    if option == 1:
        print(f"\nQuantidade de fabricantes para cada legenda:\n{quantity_legend}")
    elif option == 2:
        print(f"\nPercentual de fabricantes para cada legenda:\n{percentage_legend}")
    elif option == 3:
        print(f"\nPercentual de fabricantes para cada legenda:\n{raw_percentage_legend}")
    elif option == 4:
        option = "O"
        # Recebe a legenda escolhida como entrada
        while option not in "CBRNI":
            option = input("\nDigite a legenda desejada para consulta: ").upper().strip()
        # Seleciona os dados correspondentes à legenda
        if option == "C":
            legend_chart = [quantity[0], percentages[0][0]]
        elif option == "B":
            legend_chart = [quantity[1], percentages[0][1]]
        elif option == "R":
            legend_chart = [quantity[2], percentages[0][2]]
        elif option == "N":
            legend_chart = [quantity[3], percentages[0][3]]
        elif option == "I":
            legend_chart = [quantity[4], percentages[0][4]]
        # 3. Imprime a lista da legenda selecionada
        sleep(0.5)
        print(f"""\nA legenda especificada possui as seguintes características:
        Legenda solicitada: {option}
        Quantidade de fabricantes: {legend_chart[0]}
        Percentual desta legenda na amostra: {ceil(legend_chart[1])}%""")
print("\nMuito obrigado, e volte sempre!")
