import numpy as np

data = np.loadtxt("precipitacao.txt")
with open('precipitacao.txt', 'r') as archive:
    print(data)
    max = np.amax(dados)
    min = np.amin(dados)
    med = np.average(dados)
    print('O valor maximo foi: ', max)
    print('O valor minimo foi: ', min)
    print('A media foi de: ', med)
    with open('resultados.txt', 'w') as f:
        f.write('Os resultados foram \n')
        f.write('\nO valor maximo foi: '), f.write(str(max))
        f.write('\nO valor minimo foi: '), f.write(str(min))
        f.write('\nA media foi de: '), f.write(str(med))