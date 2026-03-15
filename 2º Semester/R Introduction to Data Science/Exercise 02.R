install.packages("dslabs")
library(dslabs)
library(dplyr)
data(murders)

population_in_millions = murders$population / 10 ^ 6
hist(population_in_millions)

murders = mutate(murders, rate = total / population * 100000)
boxplot(population~region, data = murders)
