numbers = [1, 2, 3, 4, 5]

# LOOPING METHOD
print("---LOOP METHOD---")
doubled_numbers = []
for num in numbers:
    double_number = num * 2
    doubled_numbers.append(double_number)
print(doubled_numbers)

# COMPREHENSION METHOD
print("---COMP METHOD---")
comp_numbers = [num * 2 for num in numbers]
print(comp_numbers)


print("---------LC with Conditional Logic---------")

numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]
mult_div = [num*2 if num % 2 == 0 else num/2 for num in numbers]

print(evens)
print(odds)
print(mult_div)

with_vowels = "This is so much fun!"

no_vowels = ''.join(char for char in with_vowels if char not in "aeiou")

print(no_vowels)



