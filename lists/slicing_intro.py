first_list = [1, 2, 3, 4]


 # index lines to START slicing from
print(first_list[3:])
print(first_list[1:]) 
print(first_list[3:])
print(first_list[0:])
print(first_list[-1:])
print(first_list[-3:])

print("=" * 40)


 # index lines to END slicing from
print(first_list[:2])
print(first_list[:4])
print(first_list[:-2])
print(first_list[:-3])

print("=" * 40)


 # index lines to START and END slicing from
print(first_list[1:3])
print(first_list[-1:4])
print(first_list[-1:-4])
print(first_list[1:-1])

print("=" * 40)

second_line = [1, 2, 3, 4, 5, 6, 7, 8]

# index lines START at index and SKIP by X (or START at 0 (::X))
print(second_line[1::2])
print(second_line[::2])
print(second_line[::-1])
print(second_line[1::4])
print(second_line[::4])
print(second_line[1::-1])
print(second_line[:1:-4])
print(second_line[2::-1])


