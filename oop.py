car_cost = 90000
company_name = "Republic Inc."
favourite_films = ['Star Wars', 'Pulp Fiction', 'Shrek']

anakin = ["Anakin Skywalker", 20, "General", 2041]
obiwan = ["Obiwan Kenobi", 36, "General", 2035]
palpatine = ["Palpatine", "Senator", 2020]

anakin_name = anakin[0]


class RepublicEmployee:

    def __init__(self, name, age, position, year_of_join):
        self.name = name
        self.age = age
        self.position = position
        self.year_of_join = year_of_join


class Dog:
    pass


class Parent:
    def __init__(self):
        attribute = "some attribute"


class Child(Parent):
    pass
