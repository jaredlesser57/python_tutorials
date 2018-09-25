class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name=name)


class Lizard(Aquatic, Ambulatory): # Order matters here on what gets called...
    def __init__(self, name):
        Aquatic.__init__(self, name=name)
        Ambulatory.__init__(self, name=name)

jared = Penguin("Jared")
print(jared.swim())
print(jared.walk())
print(jared.greet()) # Why land and not sea???

steve = Lizard("Steve")
print(steve.greet())


# tom = Aquatic("Tom")

# print(tom.walk()) # AttributeError - Aquatic can't access Amulatory methods and vice versa


