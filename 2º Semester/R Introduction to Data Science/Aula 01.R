a = 1
b = 2
c = 3
# ls()
options(digits=8)
paises = c("Brasil", "Eua")
rank = c(1, 3)
class(rank)
names(rank) = paises
rank[1]
installed.packages()
data()
CO2
help(CO2)
n = 1000
x = seq(1,n)
x
sum(x)
install.packages("dslabs")
library(dslabs)
data(murders)
help(murders)
murders
class(murders)
str(murders)
head(murders)
murders$population #acessor $
names(murders)
murders$population[1]
pop = murders$population
length(pop)
class(pop)
class(murders$state)
levels(murders$region)
murders$region == murders[["region"]]
x = c("a", "a", "b", "b", "b", "c")
table(x)
a = 2
b = -1
c = -4
delt = b^2 - 4*a*c
x1 = (-b + sqrt(delt))/2*a
x2 = (-b - sqrt(delt))/2*a
data(movielens)
movielens
str(movielens)
levels(movielens)
names(movielens)
help(movielens)
summary(movielens)
codes1 = c(italy = 360, canada = 124, egypt = 818)
codes2 = c("italy" = 360, "canada" = 124, "egypt" = 818)
class(codes2)
codes1[0]
seq(5)
seq(1, 10, 1)
class(seq(1, 10, 0.2))
codes2[c(1, 3)]
c(1,2,3) == 1:3
class(c(1, 2, 3)) == class(1:3)
codes1["canada"]
x = TRUE
y = as.character(x)
print(y)
as.numeric(TRUE)
temp = c(50, 75, 90, 100, 150)
city = c("Brasília", "Paris", "Japonvar", "Itu", "Roma")
x3 = 13:71
seq(0, 10, length.out = 101)
vector("numeric", length = 15)
sort(murders$total)
order(c(31, 4, 15, 92, 65))
murders$state[1:10]
murders$abb[1:10]
index = order(murders$total)

install.packages("dplyr")
library(dplyr)
library(dslabs)
data("murders")
murders = mutate(murders, rate = total / population * 100000)
head(murders)
filter(murders, rate <= 0.71)
new_table = select(murders, state, region, rate)
filter(new_table, rate <= 0.71)
murders %>% select(state, region, rate) %>% filter(rate <= 0.71)
