# def current_beat():
#     nums = (1,2,3,4)
#     i = 0
#     while True:
#         if i >= len(nums):
#             i = 0
#             yield nums[i]
#             i += 1



# counter = current_beat()

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))



def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield "{} bottles of {} on the wall.".format(num, beverage)
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(beverage)
        else:
            yield "No more {}!".format(beverage)




