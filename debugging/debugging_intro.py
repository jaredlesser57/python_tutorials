### RAISE - raising own errors for detection 


def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("Color must be a string...")
    if type(text) is not str:
        raise TypeError("Text must be a string...")
    if color not in colors:
        raise ValueError(f"{color} is an invalid color")
    print(f"Printed {text} in {color}")

# colorize("Hello", 123) # TypeError because type(color) is not a string

colorize("Hello", "yellow")
# colorize("Hello", "red") # ValueError because red is not in list(colors)




### TRY and EXCEPT Blocks

# try:
#     foobar
# except:
#     print("Except")
# print("After the Except, try...")

d = {"name": "Jared"}

# d["city"] # KeyError since key = "city" not in dictionary 'd'

def get(d, key):
    try:
        print(d[key])
    except KeyError:
        print("That is not a valid key to choose from in that dictionary...Try again...")

get(d, "name")
get(d, "city")




### TRY, EXCEPT, ELSE and FINALLY blocks (else and final NOT required...)




# try: 
#     num = int(input("Please enter a number: "))
# except:
#     print("That's not a number!")
# else:
#     print("I am in the ELSE...")
# finally:
#     print(f"You entered {num}") # finally will run no matter what

while True:
    try: 
        num = int(input("Please enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        print(f"You entered {num}.")
        break
    finally:
        print("RUNS NO MATTER WHAT!") # finally will run no matter what
print("REST OF GAME LOGIC RUNS!")


def divide(a, b):
    try:
        result =  a/b
    except ZeroDivisionError:
        print("You can't divide by 0...")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")

print(divide(4, 2))
print(divide(1, 'a'))