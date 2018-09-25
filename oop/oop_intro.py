""" Object oriented programming is a method of programming
    that attempts to model some process or thing in the world as
    a class or object
"""

# Definine the simplest possible class

# class User:
#     pass


# user1 = User()



class User:
    def __init__(self, first, last, age=0):
        self.first = first
        self.last = last
        self.age = age
        print("A new user has been made for {} {}... They are {} years old...".format(first, last, age))


user1 = User("Jared", "Lesser", 27)
user2 = User("Steven", "Madrid", 35)
user3 = User("Justin", "Lee", 19)
user4 = User("John", "Doe")
