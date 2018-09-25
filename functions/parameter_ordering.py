# How to order parameters in a function declaration

# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs


def display_info(a, b, *args, instructor="Jared", **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name="Lesser", job="Instructor"))

# a - 1
# b - 2
# args- (3)
# default -  "Jared" (because nothing was passed in)
# kwargs - {'last_name': "Lesser", 'job': "Instructor"} (a dictionary was created with last to key/value pairs (**kwargs))