# {} and are key/value pairs

instructor = {
    "name": "Jared",
    "owns_dog": False,
    "age": 28,
    "favorite_language": "Python",
    57: "my favorite number!"
}

print(instructor["name"])

try:
    print(instructor["thing"])
except KeyError:
    print("Key/Value pair does not exist")