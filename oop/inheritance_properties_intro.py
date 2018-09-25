### Inheritance - A key feature of OOP is the ability to define a class which inherits from another class (a "base" or "parent" class)


# pass parent class as an argument to the definition of the child class

"""
class Animal:
    def make_sound(self, sound):
        print(sound)

    cool = True

class Cat(Animal): # Here we passed the 'parent' class to the 'child' class
    pass

jared = Cat()
jared.make_sound("meow") # meow
jared.cool # True

"""
class Animal:
    cool = True

    def make_sound(self, sound):
        print(f"The animal says {sound}!")


class Cat(Animal):
    pass


jared = Cat()
jared.make_sound("meow")

print(isinstance(jared, Cat)) # True, because jared is Cat (or 'object')


### Properties


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        # self.age = age # prevent ages that are negative???
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property # age is a proxy to _age - GETTER
    def age(self):
        return self._age

    @age.setter # SETTER
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            self._age = 0 # or raise ValueError


    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ") # NOT Recommended 

jane = Human("Jane", "Lesser", -17)
# print(jane.get_age())
# jane.set_age(45)
# print(jane.get_age())
print(jane.age)
jane.age = 57
print(jane.age)
print(jane.full_name)
jane.full_name = "Jared Hienz"
print(jane.full_name)
print(jane.__dict__)
