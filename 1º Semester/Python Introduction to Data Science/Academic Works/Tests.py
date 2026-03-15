import pandas as pd
from math import ceil
from time import sleep

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