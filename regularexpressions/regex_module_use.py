# import the regex module
import re

# define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}') # r stands for raw string

# search a string with our regex
res = pattern.search('Call me at 415 555-4242!')
print(res)
print(res.group())

res2 = pattern.findall('Call me at 415 555-4242 or 412 784-2229!')
print(res2)

for i in res2:
    print(i)