from csv import reader, writer, DictReader, DictWriter
with open("fighersW.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])


# READ IN / ALTER / OUT

# OPEN to Read
with open('fighters.csv') as file1:
    csv_reader = reader(file1)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    # for row in fighters:
        # print(row)


with open('screaming_fighters.csv', 'w') as file2:
    csv_writer = writer(file2, lineterminator= '\n')
    for fighter in fighters:
        csv_writer.writerow(fighter)



### OUT as NESTED Statements

with open('fighters.csv') as file1:
        csv_reader = reader(file1)
        with open('screaming_fighters.csv', 'w') as file2:
            csv_writer = writer(file2, lineterminator= '\n')
            for fighter in fighters:
                csv_writer.writerow([[s.upper() for s in row] for row in csv_reader]) 



### WRITING TO CSV USING DictWriter, fieldnames, writeheader and writerow

with open("example.csv", "w") as file:
    headers = ["Character", "Move", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers, lineterminator= '\n')
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Jared",
        "Move": "Whirlwind-Kick",
        "Age": 29
    })



def cm_to_in(cm):
    return float(cm) * 0.393701

with open("fighters.csv") as file:
    csv_reader = DictReader(file, lineterminator= '\n')
    fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers, lineterminator= '\n')
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_in(f["Height (in cm)"])
        })






