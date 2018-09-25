# _name # private attribute/variable 
# __name # 
# __name__ # Dunder methods (only really used for __init__)

class Person:
    def __init__(self): # only using __<>__ when attempting to overwrite Dunder methods (not likely to use this for anything other than INIT)
        self.name = "Tony"
        self._secret = "hi!" # private attribute/variable 
        self.__msg = "I like turtles"
        self.__lol = "HAHAHAHAHA"
    def doorman(self, guess):
        if guess == self._secret:
            return("You may enter!")
        else:
            return("You may NOT enter...")

    

p = Person()

print(p.doorman("hi!")) # call a def within a class
print(p.doorman("hello"))

print(p.name)
print(p._secret)
print(dir(p))
#print(p.__msg) # name mangling - will not print - python will mangle the name '_Person__msg'
# print(p._Person__lol)