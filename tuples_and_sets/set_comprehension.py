set_comp = {x**2 for x in range (10)}

print(sorted(set_comp)) # IF NOT sorted, would be random

set_comp = {x:x**2 for x in range (10)}

print(set_comp) # IF NOT sorted, would be random