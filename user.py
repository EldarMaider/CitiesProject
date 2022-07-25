from abc import abstractmethod


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.logged = False


    def write_comment(self):
        pass

    def search_city(self, city_to_search, list_of_cities):
        for city in list_of_cities:
            if city_to_search == city.name:
                return f" The city is:{city.name}, country is:{city.country},is the city a capital? {city.capital},the population is: {city.population}"

        return "no description of the given city"

