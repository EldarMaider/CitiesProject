import city
import all_city_list
import user
import all_users_list
import pickle
import read_from_file


def user_authenticate(user_name, user_password, list_of_users):
    for user_info in list_of_users:
        if user_name == user_info.name and user_password == user_info.password:
            return user_info
    return None


def add_usr(user_db, new_user_name, new_user_password):
    New_User = user.User(new_user_name, new_user_password)
    user_db.append(New_User)


def add_city(cities_db, city_name_input, city_country_input, city_population_input, city_capital_input):
    new_user_city = city.City(city_name_input, city_country_input, city_population_input, city_capital_input)
    cities_db.append(new_user_city)


def main():
    cities_data = read_from_file.return_cities_data()
    users_data = read_from_file.return_customers()
    while True:
        print("Hello and welcome to CityTourAdvisory")
        user_decision = int(input("for log in press 1 for registration press 2,for adding new city press 3 "
                                  "to quit press any other key"))
        if user_decision == 1:
            usr_name = input(" please provide your name")
            user_password = input(" please enter your password")
            user_instance = user_authenticate(usr_name, user_password, users_data)
            if user_instance:
                while True:
                    user_input = int(input("welcome to World Cities tour guide\n which action would you like to perform?"
                                           "\n""for city search press 1,for commenting press 2, to return to main menu "
                                           "press any other key"))
                    if user_input == 1:
                        city_for_search = input("what is the city you want to search?")
                        print(f"here is what we found:{user_instance.search_city(city_for_search, cities_data)}")
                    elif user_input == 2:
                        pass
                    else:
                        print("back to main manu")
                        break
            else:
                print("no such user found,try again or register")
        elif user_decision == 2:
            print("we are glad you decided to register to our site")
            new_user_name = input("enter your user name")
            new_user_password = input("enter your user password")
            add_usr(new_user_name, new_user_password)
        elif user_decision == 3:
            print("enter the following information")
            city_name_input = input("enter the name of the city")
            city_country_input = input("enter the name of the country")
            city_population_input = input("enter the population of the city")
            city_capital_input = input("is the city a capital yes or no?")
            new_user_city = city.City(city_name_input, city_country_input, city_population_input, city_capital_input)
            cities_data.append(new_user_city)
        else:
            print("hope to see you again soon, goodbye!")
            break


if __name__ == '__main__':
    main()
