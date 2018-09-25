# """
# Doctests:

# - We can write tests for functions inside of the docstring
# - Write code that looks like it's inside a REPL (>>>)

# Example:

# Note: ''' below are actually double-quotes in real life

# '''add together x and y
# >>> add(1, 2)
# 3

# >>> add(8, "hi)
# Traceback (most recent call last):
#     ...
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# '''

# Running Doctests:

# >>> python -m doctest -v doctests_intro.py
# """



# def add(a, b):
#     """ 
#     >>> add(2, 3)
#     5
#     >>> add(100, 200)
#     300
#     """
#     return a + b


def double(values):
    """ double the values in a list
    
    >>> double([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> double([])
    []

    >>> double(['a', 'b', 'c'])
    ['aa','bb','cc']

    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
