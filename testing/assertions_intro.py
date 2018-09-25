""" 
Assertions:


- We can make simple assertions with the 'assert' keyword
- 'assert' accepts an expression
- Returns 'None' if the epxression is truthy
- Raises an 'AssertionError' if the epxression is falsy
- Accepts an optionsl error message as the second argument

ASSERTS are NOT guranteed to run (because of -O which ignores all assertions)
"""


# def add_positive_numers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y

# add_positive_numers(1, 1)
# add_positive_numers(1, -1)



def eat_junk(food):
    junk_list_items = ["pizza", "candy", "fries", "burrito", "ice cream"]
    assert food in junk_list_items, "You ate a NON-junk food item!"
    return f"You ate {food}!"


food = input("ENTER A FOOD PLEASE: ")

print(eat_junk(food))

"""
Assertions Warning:

If a Python file is run with the -O flag,
assertions will NOT be evaluated! 
(ignores assertions)

>>>python -O assertions_intro.py
"""



 
