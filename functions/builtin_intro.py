### SORTED, not same as SORT

print("=" * 25 + " SORTED " + "=" * 25)
more_numbers = [6,1,8,2]

sorted(more_numbers)
print(more_numbers)
print("*" * 25)
more_numbers.sort()
print(more_numbers)


# But to use it correctly --- it MUST have a sort by (e.g. key=len)


users = [
    {"username": "Jared", "tweets": ["I love cake", "I love dogs", "I like chicken"]},
    {"username": "Tom", "tweets": ["I like skiing", "I love to drive fast cars", "I love to taste new beers", "I hate the beach"]},
    {"username": "Justin", "tweets": []},
    {"username": "Megan", "tweets": ["I love ice cream!", "I love cats"]},
    {"username": "Lucy", "tweets": ["I love to go hiking"]},
    {"username": "Steve", "tweets": []}
]
print("*" * 25)
out = sorted(users,key=lambda user: user['username'])
print(out)

print("*" * 25)

out1 = sorted(users,key=lambda user: len(user["tweets"]))
print(out1)

print("*" * 25)
# Reverse the order with additional parameters
out2 = sorted(users,key=lambda user: len(user["tweets"]), reverse=True)
print(out2)

print("=" * 25 + " MIN and MAX " + "=" * 25)

### MIN and MAX

print(max(3, 67, 99, 57))
print(max('c', 't', 'f', 'h').upper())
print("*" * 25)
nums = [40, 26, 18, 29, 67]
minNums = min(nums)
print("{} is the min number".format(minNums))

# With parameters --- 

names = ["Jared", "Tom", "Susan", "Michael", "Brittany"]

print(min(len(name) for name in names))
print(max(len(name) for name in names))

maxName = max(names, key=lambda n: len(n)) # This will help print out key for name (e.g Jared (not 5 --- length of Jared))
print(maxName)


minTweets = min(users, key=lambda user: len(user['tweets']))
print(minTweets)
maxTweets = max(users, key=lambda user: len(user['tweets']))
print(maxTweets)


### REVERSED 

print("=" * 25 + " REVERSED " + "=" * 25)

numsX = [1, 2, 3, 4, 5]

numRev = numsX.reverse() # NOT the same as reversed
print(numRev)

numReved = list(reversed(numsX))
print(numReved)

for char in reversed("hello world"):
    print(char)

print("Hello"[::-1])


reverseStr = ''.join(list(reversed("hello"))) # NEED .join or else get a list [.,.,.]
print(reverseStr)



### LEN --- "length"


# len('awesome') # 7 
# len((1,2,3,4) # 4 
# len([1,2,3,4]) # 4
# len(range(0,10)) # 10 
# len({1,2,3,4}) # 4
# len({'a': 1, 'b': 2, 'c':3}) # 3

print("hello".__len__())

length = len("Hello")
print(length)



### Abs(), Sum(), Round() - NOT for strings...


# ABS = returns absolute value of a number (e.g. -5 would return 5)

print(abs(-2354))

# SUM = retuns iterable with an optional start (left to right) - starts at 0

print(sum([1,2,3,4,5,6,7]))
print(sum([1,2,3,4,5,6,7], 10))
print(sum([1,2,3,4,5,6,7], -6))

# ROUND = return number rounded to ndigits

print(round(10.2))
print(round(10.5134, None)) # rounds up to nearest whole
print(round(10.4134, None)) # rounds up to nearest whole
print(round(10.2342351, 5)) # five being to the fifth decimal place (can be whatever as needed)
print(round(10.6342351, 5)) # five being to the fifth decimal place (can be whatever as needed)
print(round(10.9999999999999999999999999999, 15)) # precision slips at some point, so it just rounds to whole nearest number
print(round(10.0000000000000000000000000001, 15)) # precision slips at some point, so it just rounds to whole nearest number




### ZIP - Make an iterator that aggregates elements from each of the iterables

first_zip = zip([1, 2, 3], [4, 5, 6])
print(list(first_zip))

first_zip = zip([1, 2, 3], [4, 5, 6])
print(dict(first_zip))

zipNums1 = [1,2,3,4,5]
zipNums2 = [6,7,8,9,10]

z = zip(zipNums1, zipNums2)
print(list(z))
z = zip(zipNums1, zipNums2)
print(dict(z))


five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))




