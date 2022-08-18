import datetime


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.logged = False

    def write_comment(self):
        """
        This function allows the user to write comments on cities he visited
        """
        pass

    def search_city(self, city_to_search, list_of_cities):
        """
        This function allows the user to search for a city in the DB and receive the information about it
        including comments
        """
        for city in list_of_cities:
            if city_to_search == city.name:
                return city

        return None
