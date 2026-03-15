chart = []
exchange = []
count = 1

option = int(input("""Escolha um valor para a opção desejada!

    [ 1 ] Valor médio mensal em agosto
    [ 2 ] Média móvel semanal
    [ 3 ] Desvio padrão amostral da cotação mensal
    [ 0 ] sair

Opção: """))

with open("dólar.txt", "rt") as monthly_dolar:
    with monthly_dolar.readlines() as dolar_list:
        dolar_list.split(";")
        print(monthly_dolar)
        for position, line in enumerate(monthly_dolar):
            chart += monthly_dolar.readlines()[position]
        print(monthly_dolar)
        print(chart)
        monthly_dolar.close()

matrix = chart[0:31][0:1]

column_1 = "Data"
column_2 = "Taxa de Câmbio"
print(f"{column_1:<10}", f"{column_2:>10}")
for dolar in range(len(matrix)):
    if matrix[dolar] % 2 == 0:
        total += dolar
        count += 1
        exchange.append(dolar)
        print(f"R${dolar}")
        if 0 <= matrix[dolar] <= 2:
            sample += dolar
            period += 1
    else:
        print(f"R${dolar}")

media = total / count
mobile_media = sample / period
for sample in len(total):
    standard_deviation += (((exchange[sample] - media) ** 2) / count - 1) ** (1 / 2)

if option == 0:
    print("Obrigado, até a próxima!")
elif option == 1:
    print(f"A média do dólar no mês de agosto foi de: R${media:.2f}")
elif option == 2:
    print(f"A média móvel dos 3 últimos dias da cotação do dólar de agosto é de: R${mobile_media:.2f}")
elif option == 3:
    print(f"O desvio padrão amostral da cotação mensal é de: R${standard_deviation:.2f}")
else:
    print("Opção inválida, volte sempre!")
