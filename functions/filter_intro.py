l = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, l))

print(evens)

# Combination of Map and Filter using Lambda functions

names = ["Jared", "Colt", "Steven"]


out = list(map(lambda name: f"Your instructor is {name}",
        filter(lambda value: len(value) < 5, names)))

print(out)


# With List Comprehension vs. above... Comprehension is more usuable and easier to read/write

outCom = [f"Your instructor is {name}" for name in names if len(name) < 5]

print(outCom)