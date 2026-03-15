install.packages("dslabs")
library(dslabs)
data(murders)
pop = murders$population
pop_sort = sort(pop)
menor_sort = pop_sort[1]
menor_sort
pop_order = order(pop)
menor_order = pop_order[1]
menor_order

murders$state[menor_order]
which.min(murders$total)
which.min(pop)
which(murders)
murders$state[which.min(murders$total)]
which.min(murders$population)
states = murders$state
states[51]

temp = c(35, 88, 42, 84, 81, 30)
city = c("Beijing", "Lagos", "Paris", "Rio de Janeiro", "San Juan", "Toronto")
data.frame(row.mames=1:length(city), city, temp)
ranks = rank(murders$population)
my_df = data.frame(states, ranks)

ranks = rank(murders$population)
ind = order(murders$population)
my_df2 = data.frame(states = states[ind], ranks = ranks[ind])

library(dslabs)
data(na_example)
str(na_example)
mean(na_example)
ind = is.na(na_example)
x = c(1, 2, 3)
ind2 = c(FALSE, TRUE, FALSE)
x[!ind2]
mean(na_example[!ind])
mean(na_example,na.rm=TRUE)

murders$state[which.max(murders$population)]
max(murders$population)

murder_rate = murders$total / murders$population * 100000
murder_rate
murders$state[order(murder_rate, decreasing = TRUE)]

city2 = c("Pequim", "Lagos", "Paris", "Rio de Janeiro", "San Juan", "Toronto")
temp = c(35, 88, 42, 84, 81, 30)
temp_celsius =  5 * (temp - 32) / 9
temp_celsius

x = (1:100)
cálculo = 1/x^2
cálculo
sum(cálculo)


library(dslabs)
data(murders)
murder_rate = murders$total / murders$population * 100000
indexis = murder_rate < 0.71
murders$state[index]
print(indexis)

west = murders$region == "west"
safe = murder_rate <= 1
index3 = safe & west
index
murders$state[index]

index4 = which(murders$state == "Massachusetts")

index5 = match(c("New York", "Florida", "Texas"), murders$state)
murders$state[index5]

c("Boston", "Dakota", "Washington") %in% murders$state
which(murder_rate < 1)
low = murder_rate < 1
print(low)


abbs = c("AK", "MI", "IA")
ind = match(abbs, murders$abb)
murders$state[ind]

abbs2 = c("MA","ME","MI","MO","MU")
ind2 = which(!abbs2%in%murders$abb)
abbs[ind2]

install.packages("dplyr")
library(dplyr)
library(dslabs)
data("murders")
murders = mutate(murders, rate = total / population * 100000)
x4 = c(88, 110, 83, 92, 94)
rank(x4)
rank(-x4)

rate = murders$stotal / murders$population * 100000
murders = mutate(murders, rank = rank(-rate))
print(murders)

select(murders, state, abb)

murders2 = mutate(murders, rate = total / population * 100000, rank = rank(-rate))
top_5 = filter(murders2, rank <= 5)
print(top_5)

no_south = data.frame(murders$state[which(murders$region != "South")])
no_south = filter(murders, region != "South")
print(no_south)
nrow(no_south)

murders_nw = filter(murders, "Northeast" & "West" %in% region) 

murders_nw = filter(murders, region %in% c("Northeast", "West"))
nrow(murders_nw)

murders2 = mutate(murders, rate = total / population * 100000, rank = rank(-rate))

murders_in_nw = filter(murders2, region %in% c("Northeast", "West") & rate < 1)
print(murders_in_nw)

my_states = select(murders_in_nw, state, rate, rank)
print(my_states)

my_states = filter(murders2, region %in% c("Northeast", "West") & rate < 1) %>% select(state, rate, rank)
print(my_states)


data(murders)
order_states = my_states[order(my_states, rank)]
print(order_states)


