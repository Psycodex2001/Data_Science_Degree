#Questão B

x = float(input("Digite o valor de x: "))
ln = 0
coefficient = 1
counter = 1
factorial = 1
if 0 < x < 1:
    for signal in range(2, 32):
        while counter <= coefficient:
            factorial *= counter
            counter += 1
        terms = ((-1) ** signal) * (x ** coefficient) / (factorial)
        ln += terms
        coefficient = coefficient + 1
    print(f"{ln:.11f}")