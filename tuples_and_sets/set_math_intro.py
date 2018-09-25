cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", " Los Angeles", "London", "Chicago"]

print(len(set(cities)))

print(list(set(cities)))


math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print(math_students | biology_students)
print(math_students & biology_students)