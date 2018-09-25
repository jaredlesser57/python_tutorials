nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 35.572]]

# for loc in coords:
#     print(loc)

for loc in coords:
    for coord in loc:
        print(coord)

print("----------")


# NESTED List Comprehension

[[print(val) for val in l] for l in nested_list]


board = [[num for num in range(1,4)] for val in range(1,4)]

print(board)

x_o = [["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]

print(x_o)

