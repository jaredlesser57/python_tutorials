### SPECIAL METHODS

# 8 + 2
# "8" + "2"

"""
The + operator is shorthand for a special method called __add__() that gets
called on the first operand.

If the first (left) operand is an instance of int, __add__() does mathematical 
addition. If it's a string, it does string concatenation.abs

Example below:
"""
from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first 
        self.last = last
        self.age = age    

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first='Newborn', last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance (other, int):
            return [copy(self) for i in range(other)] # copy package
        return "Can't multiply!"



j = Human("Jared", "Lesser", 29)
print(j)
print(len(j))

k = Human("Kevin", "Jones", 49)
print(k)
print(k + j) # last name taken based on first
print(j * 2) # ORDER MATTERS

triplets = j * 3
triplets[1].first = "Jessica" # this will make change to all three in list
print(triplets)
babies = (k + j) * 3
print(babies)
