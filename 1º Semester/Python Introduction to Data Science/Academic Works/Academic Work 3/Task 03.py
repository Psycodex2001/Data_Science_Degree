from random import randint
from numpy import array

standard_deviation = 0

example = [[3, 3, 1, 3, 3], [5, 4, 2, 4, 5], [4, 3, 1, 3, 5], [4, 3, 2, 3, 5], [5, 3, 2, 3, 4],
           [4, 2, 2, 4, 5], [3, 3, 1, 3, 4], [3, 4, 2, 3, 5], [5, 4, 3, 3, 5], [5, 4, 2, 2, 4]]
subtotals = []
means = []
standard_deviations = []

answer = array([[randint(1, 5) for column in range(5)] for row in range(10)])

subcount = sum(1 for row in range(len(answer)))
for column in range(5):
    subtotal = 0
    respondents.clear()
    for row in range(len(answer)):
        respondents.append(answer[row][column])
        subtotal += answer[row][column]
    series.append(respondents)
    subtotals.append(subtotal)
    means.append(subtotal / subcount)
    for row in range(len(answer)):
        dispersion += (series[column][row] - means[column]) ** 2
        variance.append(dispersion)
    standard_deviation = (variance[column] / count) ** (1 / 2)
    standard_deviations.append(standard_deviation)

print(subtotals)
print(means)

standard_deviations = [subtotals]
for subtotal in standard_deviations:
    total = sum(subtotal)
weighted_mean = total / sum(standard_deviations)
n = (1.96 * weighted_mean / 0.2) ** 2

print(total, count, subtotal_1, subtotal_2, subtotal_3, subtotal_4, subtotal_5, subcount, matrix, sep="\n")

print(n)

for row in range(10):
    for column in range(5):
        standard_deviation += (((matrix[row][column] - mean) ** 2) / count) ** (1 / 2)
weighted_mean = standard_deviation / count
