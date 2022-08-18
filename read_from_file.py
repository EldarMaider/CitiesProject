import pickle
from pprint import pprint
from city import City
from user import User


def initialize_cities_data():
    list_of_cities = []
    # todo- all of this part of the csv should only be done on the first run.
    # load will be done every time.
    # i suggest you put it in a seperate function and call it only once.
    with open("cities.csv", "r") as my_file:
        my_file.readline()
        raw_data = my_file.readlines()
        for line in raw_data:
            temp_list_city = line.split(",")
            city = City(name=temp_list_city[0],
                        country=temp_list_city[1],
                        population=int(temp_list_city[2]),
                        capital=temp_list_city[3][:-1])
            list_of_cities.append(city)

    with open("cities.pkl", "wb") as cities_file:
        pickle.dump(list_of_cities, cities_file)

def read_cities():
    with open("cities.pkl", "rb") as cities:
        return pickle.load(cities)


def initialize_users_data():
    list_of_users = []
    with open("updated_users.csv", "r") as users_file:
        users_file.readline()
        raw_usr_data = users_file.readlines()
        for line in raw_usr_data:
            temp_usr_list = line.split(",")
            user = User(name=temp_usr_list[0], password=temp_usr_list[1])
            list_of_users.append(user)
    with open("users.pkl", "wb") as users_for_pkl:
        pickle.dump(list_of_users, users_for_pkl)


def read_users():
    with open("users.pkl", "rb") as users:
        return pickle.load(users)


def initialize_comments_data():
    with open("comments.pkl", "wb") as comments:
        return pickle.dump([], comments)

def read_comments():
    with open("comments.pkl", "rb") as comments:
        return pickle.load(comments)