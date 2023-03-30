if __name__ == "__main__":
    filename = "Countries.txt"
    country_populations = fileRead(filename)
    printPopulation(country_populations)

def fileRead(filename):

    country_populations = {}

    with open(filename, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(", ")
            population = int(population)

            if country in country_populations:
                country_populations[country].append((year, population))
            else:
                country_populations[country] = [(year, population)]

    return country_populations



def printPopulation(country_populations):
    for country, populations in country_populations.items():
        print(country + ":")
        for i in range(len(populations) - 1):
            year1, pop1 = populations[i]
            year2, pop2 = populations[i + 1]
            pop_change = pop2 - pop1
            print(year1 + " -> " + year2 + ": " + str(pop_change))
