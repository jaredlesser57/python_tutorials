class GrumpyDict(dict): # not defining __init__ this time. Will use existing (dict)
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"YOU WANT {key}? WELL, IT'S NOT HERE!")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY???")
        print(f"OKAY FINE, WE WILL UPDATE {key} with {value}")
        super().__setitem__(key, value)
    
    def __contains__(self, item):
        print("NO, IT AIN'T HERE...")
        return False


data = GrumpyDict({"first": "Tom", "animal": "Cat"})
print(data)
data['city']