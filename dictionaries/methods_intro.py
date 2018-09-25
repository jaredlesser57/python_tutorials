instructor = {
    "name": "Jared",
    "owns_dog": False,
    "age": 28,
    "favorite_language": "Python",
    57: "my favorite number!"
}
print()


# CLEAR DICTIONARY
print("---Initial Dictionary---")
print(instructor)
print("---Cleared Dictionary---")
instructor.clear()
print(instructor)


instructor = {
    "name": "Jared",
    "owns_dog": False,
    "age": 28,
    "favorite_language": "Python",
    57: "my favorite number!"
}


# COPY DICTIONARY
copy_dict = instructor.copy()
print("---Copied Dictionary---")
print(copy_dict)


# fromkeys DICTIONARY - creates a DICTIONARY with a key/value pair (good for creating/setting default dictionaries)
print("---fromkeys Dictionary---")
new_dict_ketPair = {}.fromkeys("a", "b") # {'a': 'b'}
print(new_dict_ketPair)
unknown_dict = {}.fromkeys(['name', 'score', 'email', 'portfolio bio'], 'unknown') # sets 'unknown' as value for each key
print(unknown_dict)


# GET DICTIONARY
print("---Get Dictionary---")
dict_get = instructor.get('age')
print(dict_get)


# ADD to DICTIONARY
print("---Add Dictionary---")
instructor["favorite_cookie"] = 'peanut butter'
print(instructor)






