class City:
    def __init__(self, name, country, population, capital):
        self.name = name
        self.country = country
        self.population = population
        self.capital = capital

    def __str__(self):
        capital_message = "this is the capital"
        if self.capital == "False":
            capital_message = "this is not the capital"
        return f"city name: {self.name},The country: {self.country}, {self.population} citizens in the cities, {capital_message}"
