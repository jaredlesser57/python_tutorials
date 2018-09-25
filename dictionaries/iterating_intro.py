instructor = {
    "name": "Jared",
    "owns_dog": False,
    "age": 28,
    "favorite_language": "Python",
    57: "my favorite number!"
}

for value in instructor.values():
    print(value)

print()

for value in instructor.keys():
    print(value)

print()

for value in instructor.items():
    print(value)

print()

for key,value in instructor.items():
    print(key,value, sep=': ')
