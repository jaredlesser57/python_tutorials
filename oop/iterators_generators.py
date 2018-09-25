### Iterators versus Iterables...

"""
Iterator - an object that can be iterated upon. An object
which returns data, one element at a time when next() is
called on it.

Iterable - An object which will return an Iterator when
iter() is called on it.abs

"""

### EXAMPLES

name = "Jared"

# print(next(name)) # NOT an iterator
it = iter(name)
print(iter(name)) # IS an iterator

for char in name: # Iterating through the Iterable (name)
    print(char)

# One next() at a time - StopIteration
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

print("=" * 50)
### GENERATORS - uses YIELD

"""
Generators are iterators

Generators can be created with generator functions

Generator functions use the yield keyword

Generators can be created with generator expressions
----------------------------------------------------------
FUNCTIONS                   | GENERATOR FUNCTIONS
                            |
uses return                 | uses yield
returns once                | can 'yield' multiple times
returns the return value    | returns a generator  (when invoked for both)
----------------------------------------------------------
"""


# Generator Example


def count_up_to(max):
    count = 1 # Will start on 1, not 2
    while count <= max:
        yield count
        count += 1


counter = count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))

print("=" * 50)

counter = count_up_to(10)
next(counter) 
for num in counter: # ***This will continue from 2, because next() has been called once count += 1
    print(num)



