if __name__ == "__main__":
    filename = "Countries.txt"
    country_populations = fileRead(filename)

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