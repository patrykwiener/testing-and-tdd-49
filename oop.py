car_cost = 90000
company_name = "Republic Inc."
favourite_films = ['Star Wars', 'Pulp Fiction', 'Shrek']

# imie, wiek, stanowisko, rok dolaczenia
anakin = ["Anakin Skywalker", 20, "General", 2041]
obiwan = ["Obiwan Kenobi", 36, "General", 2035]
palpatine = ["Palpatine", "Senator", 2020]

anakin_name = anakin[0]
anakin_position = anakin[2]
palpatine_name = palpatine[0]
palpatine_position = palpatine[2]

anakin = {
    'name': 'Anakin Skywalker',
    'position': 'General',
    'year_of_join': 2041,
}
anakin['name']
anakin.get('name')


class RepublicEmployee:

    def __init__(self, name, age, position, year_of_join):
        self.name = name
        self.age = age
        self.position = position
        self.year_of_join = year_of_join


anakin = RepublicEmployee('Anakin Skywalker', 20, 'General', 2041)
palpatine = RepublicEmployee('Palpatine', 500, 'Senator', 2020)
print(palpatine.age)


class Dog:
    def __init__(self, color, sex, age, height):
        self.height = height
        self.age = age
        self.sex = sex
        self.color = color
        self.paws = 4
        self.hungry = True

    def wave_tail(self):
        pass

    def eat(self):
        pass

    def bark(self):
        pass


class AustralianShepherd(Dog):
    pass


class Bullterrier(Dog):
    def __init__(self, color, sex, age, height, teeth_size):
        super().__init__(color, sex, age, height)
        self.teeth_size = teeth_size
        self.short_hair = True
        self.attitude = 'calm'


ciapek = Bullterrier('white', 'M', 10, 40, 'L')
ciapek.short_hair = False


# barry = Bullterrier()

# nugat = Dog(
#     color='brown',
#     sex='M',
#     age='0.75',
#     height=50,
# )


# class Parent:
#     def __init__(self):
#         attribute = "some attribute"
#
#
# class Child(Parent):
#     pass


def print_text(text):
    print(text)


moj_ulubiony_text = 'Ala ma kota'
print_text(text=moj_ulubiony_text)


class Car:

    def __init__(self, brand):
        self._producer = brand
        self.brand = brand

    def print_text(self, text):
        print(text)

    def some_method(self):
        self._producer = 'Fiat'

    def get_producer(self):
        return self._producer


car = Car('BMW')

car.print_text(text=moj_ulubiony_text)
