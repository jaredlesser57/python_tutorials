class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"The animal says {sound}!")



class Cat(Animal):

    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat") # This grabs the __init__ function from the parent class Animal - Also, do not need to inlude self; Can also set vars to defaults like 'cat'
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Scottish Fold", "String")

print(blue)
blue.play()


"""
Animal
    species
    name

Cat
    species
    name
    breed
    favorite_toy

"""