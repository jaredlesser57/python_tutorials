import re

# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')


pattern = re.compile(r"""
    ^([a-z0-9_\.-]+)    #first part of the email address 
    @                   #single @ symbol
    ([0-9a-z\.-]+)      #email provider
    \.                  #single period symbol
    ([a-z\.]{2,6})$  #com, org, etc, etc
""", re.VERBOSE) # or re.X, re.IGNORECASE ( | between params as well)


match = pattern.search("thomas123@yahoo.com")
print(match.group())
print(match.groups())