"""
Using open():

file = open("file.txt")
file.read()
"""

# With Blocks

"""
 - Option 1 - 
file = open("file.txt)
file.read()
file.close()

file.closed # True

- Option 2 -
with open("file.txt) as file:
    file.read()

file.closed # True
"""