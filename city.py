

class City:
    def __init__(self, name, country, population, capital):
        self.name = name
        self.country = country
        self.population = population
        self.capital = capital

    def __str__(self):
        return f"{self.name},{self.country},{self.population},{self.capital}"
