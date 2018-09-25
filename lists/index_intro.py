names = ["Jared", "John", "Michael", "Steven", "Don", "Bob", "Justin"]

numbers = [1, 2, 13, 4, 5, 6, 4, 2, 1, 9, 11, 21, 8]

print(numbers.index(13)) # prints position that the number 13 is found [2]

print(numbers.index(2, 4)) # prints the number 2, starting after index position [4] - 2 appears again at [7], which is printed out

print(numbers.index(4, 4, 9)) # prints the number 4 between index positions [4] and [9] - 4 appears again at [6], which is printed out