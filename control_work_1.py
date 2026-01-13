class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def make_sound(self):
        return "animal sound."

class Dog(Animal):

    def init(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "dog sound: gaf gaf"

class Cat(Animal):

    def init(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        return "cat sound: mwy mwy!"

my_dog = Dog("reks", 3)
my_cat = Cat("snow", 5)

print(f"{my_dog.get_name()}: {my_dog.make_sound()}")
print(f"{my_cat.get_name()}: {my_cat.make_sound()}")

my_dog.set_age(4)
my_cat.set_name("nig")

print(f"\nnew age {my_dog.get_name()}: {my_dog.get_age()} years old.")
print(f"new name: {my_cat.get_name()}.")