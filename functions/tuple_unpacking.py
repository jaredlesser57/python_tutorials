### * as an argument in unpacking

def sum_all_nums1(*args): # or *nums
    total = 0
    for num in args: # nums
        total += num
    print(total)

# sum_all_nums1(1, 30, 2, 5, 6)


nums = (1,2,3,4,5,6) # or []

sum_all_nums1(*nums) # nums would throw error - need *nums



### ** as an argument in unpacking

def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Jared", "second": "John"}

display_names(first="Charle", second="Sue")

display_names(**names)


def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF.....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data, cat="blue")