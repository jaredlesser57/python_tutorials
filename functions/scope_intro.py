### variables scoped OUTSIDE the function


instructor = "Jared"

def say_hello():
    return f'Hello {instructor}'

print(say_hello())



### variables scoped INSIDE the function - variables inside functions CANNOT be called outside


def say_hello1():
    instructor1 = "Jared"
    return f'Hello {instructor1}'

print(say_hello1())
print(instructor)
# print(instructor1) # NameError



### GLOBAL variables

total = 0

# def increment():
#     total += 1
#     return total

# print(increment()) # Error!

def increment1():
    global total
    total += 1
    return total

print(increment1())


### NONLOCAL variables - modify parent variables in a child (aka nested) function


def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

