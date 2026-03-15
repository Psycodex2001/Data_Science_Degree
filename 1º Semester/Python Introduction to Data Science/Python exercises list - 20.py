a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = - b ** 2 - 4 * a * c
x1 = (- b - delta ** (1 / 2)) / 2 * a
x2 = (- b + delta ** (1 / 2)) / 2 * a
print(f"Sua equação do 2º grau é essa:\n    {a}x² + {b}x + {c}")
if delta < 0:
    print("Não existe raiz real para essa equação do 2º grau!")
elif delta == 0:
    print("Há apenas uma raiz real para essa equação do 2º grau!")
else:
    print("há duas raízes reais para essa equação do 2º grau!")
if x1 != x2:
    print(f"As duas raízes reais dessa equação são:\n    x¹ = {x1} e x² = {x2}")
else:
    print(f"A única raiz real existente para essa equação é:\n    x = {x1}")
