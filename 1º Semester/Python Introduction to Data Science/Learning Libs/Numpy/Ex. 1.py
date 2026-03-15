import numpy as np

A = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# média das linhas de A
media1 = np.mean(A, axis = 1)
print("\nMédia das colunsas de A: ")
#display(media1)
print(media1)

# média das  colunas de A
media2 = np.mean(A, axis = 0)
print("\nMédia das colunsas de A: ")
#display(media2)
print(media2)

# média da segunda coluna de A
media2 = np.mean(A, axis = 0)
primcolunamedia = media2[1]
#display("\nMédia da segunda coluna de A: ", primcolunamdeia)

