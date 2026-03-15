odd = []
s = 0
print("A sua lista de termos S são:")
for number in range(20):
    if number % 2 != 0:
        odd.append(number)
        for position in range(len(odd)):
            if position % 2 != 0:
                s -= 1 / (number ** 3)
                print(f" - 1 / {number}³", end="")
            elif position % 2 == 0:
                s += 1 / (number ** 3)
                print(f" + 1 / {number}³", end="")
print(odd)