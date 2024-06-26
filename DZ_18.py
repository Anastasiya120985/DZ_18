# Задание 1
class Car:
    def __init__(self, model, year, maker, engine_volume, colour, price):
        self.__model = model
        self.__year = year
        self.__maker = maker
        self.__engine_volume = engine_volume
        self.__colour = colour
        self.__price = price

    def show_car(self):
        print(self.__dict__)

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year in int:
            self.__year = new_year

    @property
    def maker(self):
        return self.__maker

    @property
    def engine_volume(self):
        return self.__engine_volume

    @property
    def colour(self):
        return self.__colour

    @property
    def price(self):
        return self.__price

    @model.setter
    def model(self, new_model):
        self.__model = new_model.capitalize()

    @maker.setter
    def maker(self, new_maker):
        self.__maker = new_maker.capitalize()

    @engine_volume.setter
    def engine_volume(self, new_engine_volume):
        if new_engine_volume in int:
            self.__engine_volume = new_engine_volume

    @colour.setter
    def colour(self, new_colour):
        self.__colour = new_colour

    @price.setter
    def price(self, new_price):
        if new_price in int:
            self.__price = new_price


my_car = Car('Step-way', 2017, 'Renaut', 80, 'blue', 700_000)
my_car.show_car()

# Задание 2
class Book:
    def __init__(self, name, year, publish, style, author, price):
        self.__name = name
        self.__year = year
        self.__publish = publish
        self.__style = style
        self.__author = author
        self.__price = price

    def show_book(self):
        print(self.__dict__)

    @property
    def name(self):
        return self.__name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year in int:
            self.__year = new_year

    @property
    def publish(self):
        return self.__publish

    @property
    def style(self):
        return self.__style

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, new_name):
        self.__name = new_name.capitalize()

    @publish.setter
    def publish(self, new_publish):
        self.__publish = new_publish.capitalize()

    @style.setter
    def style(self, new_style):
        self.__style = new_style

    @author.setter
    def author(self, new_author):
        self.__author = new_author.capitalize()

    @price.setter
    def price(self, new_price):
        if new_price in int:
            self.__price = new_price


my_book = Book('Dune', 2022, 'Neoclassic', 'science fiction novel', 'Frank Herbert', 1_250)
my_book.show_book()

# Задание 3
class Stadium:
    def __init__(self, name, date_open, country, city, capacity):
        self.__name = name
        self.__date_open = date_open
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def show_stadium(self):
        print(self.__dict__)

    @property
    def name(self):
        return self.__name

    @property
    def date_open(self):
        return self.__date_open

    @date_open.setter
    def date_open(self, new_date_open):
        self.__date_open = new_date_open

    @property
    def country(self):
        return self.__country

    @property
    def city(self):
        return self.__city

    @property
    def capacity(self):
        return self.__capacity

    @name.setter
    def name(self, new_name):
        self.__name = new_name.capitalize()

    @country.setter
    def country(self, new_country):
        self.__country = new_country.capitalize()

    @city.setter
    def city(self, new_city):
        self.__city = new_city.capitalize()

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity in int:
            self.__capacity = new_capacity


my_stadium = Stadium('Dinamo', '06.05.1934', 'Russia', 'Ufa', 5_000)
my_stadium.show_stadium()