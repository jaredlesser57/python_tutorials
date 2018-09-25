# ADD

s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s) # it will not add something that already exists in the set

print("=" * 50)

# REMOVE

set1 = {1,2,3,4,5,6,7,8,9}
set1.remove(7)
print(set1)
set1.discard(7) # this will not throw an error if key is NOT found
print(set1)
# set1.remove(7)

print("=" * 50)

# COPY

set2 = set([1,2,3])
set2_duplicate = set2.copy()
print(set2_duplicate)

print("=" * 50)

# CLEAR

set3 = set([1, 2, 3])

set3.clear()

print(set3)



