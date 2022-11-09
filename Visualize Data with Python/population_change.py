city_name = 'Istanbul, Turkey'
pop_1927 = 691000
pop_2017 = 15029231
pop_1950 = 983000
pop_2000 = 8831800
pop_change = pop_2017 - pop_1927
percentage_gr = (pop_change / pop_1927) * 100
annual_gr = percentage_gr / (2017 - 1927)


def population_growth(city_name, year_one, year_two, population_one, population_two):

    year_change = year_two - year_one
    pop_change = population_two - population_one
    percentage_gr = (pop_change / population_one) * 100
    growth_rate = percentage_gr / year_change

    report = "The population of " + str(city_name) + " grew from " + str(population_one) + " in " + str(
        year_one) + " to " + str(population_two) + " in " + str(year_two) + ", with a total change of " + str(
        pop_change) + ". The annual growth % was: " + str(growth_rate)

    return report

    # return str("The growth rate for ") + str(city_name) + str(" during this time period was: " ) + str(float(
    # growth_rate))


set_one = population_growth('Istanbul, Turkey', 1927, 2017, pop_1927, pop_2017)
print(set_one)

set_two = population_growth('Istanbul, Turkey', 1950, 2000, pop_1950, pop_2000)
print(set_two)
