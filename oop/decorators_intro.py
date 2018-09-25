# Passing funcs as args to other functions


def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x):
    return x * x

def cube(x):
    return x * x * x

print(sum(3, square))
print(square(3))
print(cube(3))




from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))


"""
Decorators are functions

Decorators wrap other functions and enhance their behavior

Decorators are examples of higher order functions (HOF)

Decorators have their own syntax, using "@" (syntactic sugar)
"""

### EXAMPLES


def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite # this prints out the wrapper of the function above as well...a
def greet():
    print("My name is Jared.")

# @be_polite
def rage():
    print("I HATE YOU!")

greet()
rage()


### DECORTOR SYNTAX

"""
@be_polite
def greet():
    print("My name is Jared.")


- Don't need to set
"""



### Functions with Different Signatures - e.g. # of arguments

# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# @shout 
# def greet(name):
#     return f"Hi, I'm {name}!"

# @shout
# def order(main, side): # Issue with two arguments
#     return f"Hi, I'd like the {main}, with a side of {side}, please."

# print(greet("jared"))

# print(order("hamburger", "fries"))


### resolving issue below with *args, **kwargs

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout 
def greet(name):
    return f"Hi, I'm {name}!"

@shout
def order(main, side): # Issue with two arguments
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout # don't need to pass anything as well (see below)
def lol():
    return "lol"

# print(greet("jared"))

# print(order("hamburger", "fries"))

print(lol())


"""
Preserving Metadata - can present a problem though
"""

def log_function_data(fn):
    def wrapper(*args, **kwargs):
        print(f"You are about to call: {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """ Adds two numbers together """
    return x + y

print(add(10,30))

print(add.__doc__)
print(add.__name__)
help(add) # does not give us add doc, but the wrapper above


""" Using functools (@wraps) - we can preserve this data"""

print("=" * 50)


from functools import wraps

def log_function_data1(fn1):
    @wraps(fn1)
    def wrapper1(*args, **kwargs):
        print(f"You are about to call: {fn1.__name__}")
        print(f"Here's the documentation: {fn1.__doc__}")
        return fn1(*args, **kwargs)
    return wrapper1


@log_function_data1
def add1(x1, y1):
    """ Adds two numbers together ----- fn1"""
    return x1 + y1

print(add1(10, 60))
print(add1.__doc__)
print(add1.__name__)
help(add1)
