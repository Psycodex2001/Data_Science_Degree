x = float(input("Digite o valor do ângulo: "))
cossenox = 1
exp = 2

for i in range(20):
  cont = 1
  fat = 1
  while cont <= exp:
    fat *= cont
    cont += 1
  serie = ((-1)**i) * (x**exp)/(fat)
  cossenox += serie
  exp = exp+2
print("%.10f" %cossenox)
