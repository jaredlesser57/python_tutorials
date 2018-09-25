instructor = {
    "name": "Jared",
    "owns_dog": False,
    "age": 28,
    "favorite_language": "Python",
    57: "my favorite number!"
}


pop_dict = instructor.pop("name")
print(pop_dict + " removed")
print(instructor)


# POPITEMS - random key removal

instructor = {
    "name": "Jared",
    "owns_dog": False,
    "age": 28,
    "favorite_language": "Python"
}


pop_dicts = instructor.popitem()
print(pop_dicts)


# UPDATE 

first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first) # updates second dictionary with key/values from first dictionary
print(second)
second['a'] = "AMAZING" # update single value for key
print(second)