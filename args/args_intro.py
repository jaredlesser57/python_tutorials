### *ARGS - Stores into a tuple

def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3

print(sum_all_nums(4, 6, 9))



# def sum_all_nums1(*args):
#     print(args)


# print(sum_all_nums1(4,6,9,4,10))


def sum_all_nums1(*args): # or *nums
    total = 0
    for num in args: # nums
        total += num
    return total


print(sum_all_nums1(4,6,9,4,10))



### **KWARGS - Stores into a dictionary 


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print("=" * 50)
        print("{}'s favorite color is {}".format(person, color))
        print(f"{person}'s favorite color is {color}")
        


fav_colors(jared="blue", ruby="red", ethel="teal")