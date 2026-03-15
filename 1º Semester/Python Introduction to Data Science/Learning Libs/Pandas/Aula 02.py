import pandas as pd


data = {'Quantidade': [6.1, 5.8, 5.7, 5.7, 5.8, 5.6, 5.5, 5.3, 5.2, 5.2],
'Preço': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
}

grafico = pd.DataFrame(data)
grafico.plot(x='Quantidade', y='Preço', kind='scatter')
