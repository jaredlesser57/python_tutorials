def square(num):
    return num * num

print(square(9))


def add(a, b):
    return a + b

print(add(5, 8))


# DEFAULT parameters

def exponent(num, power=3):
    return num ** power

print(exponent(3))


# Can make params set as built in python functions 

def add1(a, b, fn=add):
    return fn(a, b)

print(add1(3, 6))


# KEYWORD arguments

def full_name(first, last):
    return "Your name is " + first + " " + last

print(full_name(first='Jared', last='Lesser'))
print(full_name(last='Lesser', first='Jared'))
