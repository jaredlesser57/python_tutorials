### NOT EVER DONE, but to show how things work behind the scenes

# for num in [1,2,3]:
#     print(num)

# for char in "Hello":
#     print(char)

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("---END OF ITERATOR---")
            break


my_for("Jared")

my_for(range(0, 101, 10))

### ALSO...


def my_for2(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            print("---END OF ITERATOR---")
            break
        else:
            func(thing)

my_for2("lol", print)


def square(x):
    print(x * x)

my_for2([1,2,3,4,5], square) # can call a different function
