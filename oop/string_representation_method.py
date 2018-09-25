### __repr__  - one of several ways to provide a nicer string representation

class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"

# print(User.active_users)
user1 = User("Jared", "Lesser", 28)
user2 = User("Tom", "Lopez", 39)
print(User.display_active_users())

bob = User.from_string("Bob,Jones,45")
print(bob.first)
print(User.display_active_users())
print(bob.birthday())
print(bob) # this is being printed from __repr__

j = User("Judy", "Steele", 17)
j = str(j)
print(j)
