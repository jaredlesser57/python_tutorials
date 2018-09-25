from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    # next(csv_reader) - this will skip headers
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}.")
        # each row is a list!
        # print(fighter)

# Making a list
with open("fighters.csv") as file1:
    csv_reader = reader(file1, delimiter="|")
    for row in csv_reader:
        print(row)
    # data = list(csv_reader)
    # print(data)



### DictReader

from csv import DictReader
with open("fighters.csv") as file2:
    csv_reader = DictReader(file2)
    # next(csv_reader) - this will skip headers
    for fighter2 in csv_reader:
        # print(fighter2)
        print(fighter2['Name'])
        # each row is a list!
        # print(fighter)