# function layout
def say_hi():
    print("Hi!")

say_hi()

# Return values from functions

def print_square_of_7():
    print(7**2)

print_square_of_7()


def square_or_7():
    return 7**2 # MUST have return to call outside function / nothing will execute after return is run, so place other executions before
result = square_or_7()
print(result)