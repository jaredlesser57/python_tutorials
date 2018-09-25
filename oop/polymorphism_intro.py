"""
A key principle in OOP is the idea of polymorphism - an object can take on many (poly) forms (morph)...

Two important practical applications below:

1. The same class method works in a similar way for different classes:
    Cat.speak() # meaow
    Dog.speak() # woof
    Human.speak()# hello

2. The same operation works for different kinds of objects:
    sample_list = [1,2,3]
    sample_tuple = (1,2,3)
    sameple_string = "awesome"

    len(sample_list)
    len(sample_tuple)
    len(sample_string)

    *** len() can work the same with three different types of objects
""" 

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method...")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = Dog()
print(d.speak())

f = Fish()
print(f.speak()) # NotImplementedError because Fish class does NOT have speak method


### SPECIAL METHODS = Polymorphism - same operation works for different kinds of objects (just different results)

print(8 + 2) # 10
print("8" + "2") # 82

