import pickle
import city
import user
import read_from_file
import comment
import datetime


def user_authenticate(user_name, user_password, list_of_users):
    """
    This function returns user interface if the parameters entered appear in the db. else it will return None
    """
    for user_info in list_of_users:
        if user_name == user_info.name and user_password == user_info.password:
            return user_info
    return None


def add_usr(user_db, new_user_name, new_user_password):
    """
    This function adds a new user to the db(list_of_users)
    """
    New_User = user.User(new_user_name, new_user_password)
    user_db.append(New_User)
    with open("users.pkl", "wb") as users_for_pkl:
        pickle.dump(user_db, users_for_pkl)
    return "User registration succeeded. redirecting to main manu"


def add_city(cities_db, city_name_input, city_country_input, city_population_input, city_capital_input):
    """
    This function adds a new city to the db(list_of_cities)
    """
    new_user_city = city.City(city_name_input, city_country_input, city_population_input, city_capital_input)
    cities_db.append(new_user_city)


def add_comment(all_comments):
    with open("comments.pkl", "wb") as comments:
        return pickle.dump(all_comments, comments)


def main():
    #cities_data = read_from_file.initialize_cities_data()
    # users_data = read_from_file.return_customers()
    # all_comments = read_from_file.initialize_comments_data()
    # called only once for creating pickle files with initial data
    while True:
        users_data = read_from_file.read_users()
        cities_data = read_from_file.read_cities()
        comments_data = read_from_file.read_comments()
        print("Hello and welcome to CityTourAdvisory")
        user_decision = int(input("for log in press 1,for registration press 2,to exit the site press any other key"))
        if user_decision == 1:
            usr_name = input("please provide your name")
            user_password = input("please enter your password")
            user_instance = user_authenticate(usr_name, user_password, users_data)
            if user_instance:
                print(f"{user_instance.name}, welcome to World Cities tour guide! \n")
                while True:
                    user_input = int(input(f"which action"
                                           f" would you like to perform?"
                                           "\n""for city search press 1,for commenting a city press 2,to add"
                                           " a new city press"
                                           " 3 "
                                           "to return to main menu press any other key"))
                    if user_input == 1:
                        city_for_search = input("what is the city you want to search?")
                        city_details = user_instance.search_city(city_for_search, cities_data)
                        if (city_details):
                            print(f"here is what we found: {city_details}")
                            user_comments_decision = input("would you like to see the comments for this city? yes/no")
                            if user_comments_decision == "yes":
                                for city_comment in comments_data:
                                    if city_comment.city.name == city_details.name:
                                        print(city_comment.text)
                            else:
                                print("going back to actions selection \n")
                        else:
                            print(f"no city found")
                    elif user_input == 2:
                        city_name_input = input("which city would you like to comment on?")
                        city_for_comment = user_instance.search_city(city_name_input, cities_data)
                        if city_for_comment:
                            user_comment = input("enter your comment: ")
                            new_comment = comment.Comment(user_instance, city_for_comment, user_comment, datetime.datetime.now())
                            comments_data.append(new_comment)
                            add_comment(comments_data)
                            print("thanks for sharing, sharing is caring")
                        else:
                            print(f"no city found")
                    elif user_input == 3:
                        print("enter the following information")
                        city_name_input = input("enter the name of the city")
                        city_country_input = input("enter the name of the country")
                        city_population_input = input("enter the population of the city")
                        city_capital_input = input("is the city a capital yes or no?")
                        new_user_city = city.City(city_name_input, city_country_input, city_population_input,city_capital_input)
                        cities_data.append(new_user_city)
                        print("the city has been added, thank you for your contribution")
                        print("redirecting to main manu")
                    else:
                        print("redirecting to main manu")
                        break
            else:
                print("no such user found,try again or register")
        elif user_decision == 2:
            print("we are glad you decided to register to our site")
            new_user_name = input("enter your user name")
            new_user_password = input("enter your user password")
            print(add_usr(users_data, new_user_name, new_user_password))
            print("you have successfully registered")
        else:
            print("hope to see you again soon, goodbye!")
            break


if __name__ == '__main__':
    main()
