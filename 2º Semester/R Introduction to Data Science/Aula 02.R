install.packages("dslabs")
library(dslabs)
library(dplyr)
data(murders)
population_in_millions = murders$population / 10 ^ 6
murders = mutate(murders, rate = total / population * 100000)
hist(murders$rate)

boxplot(rate~region, data = murders)

total_gun_murders = murders$total
plot(population_in_millions, total_gun_murders)


log10_population = log10(population_in_millions)
log10_total_gun_murders = log10(total_gun_murders)
plot(log10_population, log10_total_gun_murders)

s$median
s$maximum

us_murder_rate = murders %>% summarize(rate = sum(total / sum(population)) * 10^5)

quantile(x, c(0, 0.5, 1))
murders %>% filter (region == "West") %>% summarize(range = quantile(rate, c (0, 0.5, 1)))

my_quantile = function(x){r = quantile(x, c (0, 0.5, 1))
data.frame(minimum = r[1], median = r[2], maximum = r[3])}

muders %>% filter(region == "West") %>% summarize(my_quantile(rate))

us_murder_rate = murders %>% summarize(rate = sum(total / sum(population)) * 10^5) %>% pull(rate)
us_murder_rate = murders %>% summarize(rate = sum(total / sum(population)) * 10^5) %>% .$rate

murders %>% group_by(region)
murders %>% group_by(region) %>% summarize(median = median(rate))

murders %>% arrange(population) %>% head()

murders = mutate(murders, rate = total / population * 100000)
murders %>% arrange(rate) %>% head()
murders %>% arrange(desc(rate)) %>% head()
murders %>% arrange(region, rate) %>% head()
murders %>% arrange(region, rate)

murders %>% top_n(10, rate)
murders %>% arrange(desc(rate)) %>% top_n(10)


install.packages("data.table")
library(data.table)
murders = setDT(murders)
select(murders, state, region)
murders[, c("state", "region")] |> head()
murders[, .(state, region)] |> head()

murders = mutate(murders, rate = total / population * 10^5)
murders[, rate := total / population * 100000]
murders[, ":="(rate = total / population * 100000, rank = rank(population))]
murders

murders = data.table(a = 1)
z = x
y = copy(x)

install.packages("tidyverse")
library(tidyverse)
library(dplyr)
library(dslabs)
data(heights)
heights = setDT(heights)

s = heights %>% summarize(average = mean(height), standard_deviation = sd(height))
s = heights[, .(average = mean(height), standard_deviation = sd(height))]
s

