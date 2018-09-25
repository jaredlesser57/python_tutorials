# MAP variables to an iterable with lambda functions

nums = [2,4,6,8,10]

doubles = map(lambda x: x * 2, nums)
print(list(doubles))

print("=" * 50)

# OR

doubles = list(map(lambda x: x * 2, nums))

print(doubles)

print("=" * 50)

for num in doubles:
    print(num)

# Include a function into a mapped Lambda function

print("=" * 50)

def double(x):
    return x * 2

doubles = map(double, nums)

print(list(doubles))