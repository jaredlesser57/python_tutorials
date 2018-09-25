# If one false, whole is false, 

all([0,1,2,3]) # False

all([char for char in 'eio' if char in 'aeiou'])

all([num for num in [4,2,10,6,8] if num % 2 == 0]) # True


### ANY


any([0,1,2,3]) # True

any([ val for val in [1,2,3] if val > 2]) # True

any([ val for val in [1,2,3] if val > 5]) # False


####### If using any/all, you can use () without the brackets - uses less bytes (sys.getSizeOf)






