# class User:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

# user1 = User("Jared", "Lesser", 28)
# user2 = User("Tom", "Lopez", 39)
# print(user1.first, user1.last, user1.age)
# print(user2.first, user2.last, user2.age)


class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

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

print(User.active_users)
user1 = User("Jared", "Lesser", 28)
user2 = User("Tom", "Lopez", 39)
print(User.active_users)