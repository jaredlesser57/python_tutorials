from time import time
from functools import wraps

def speed_test(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(10000000))

print(sum_nums_gen())


@speed_test
def sum_nums_list():
    return sum([x for x in range(1000000)])

print(sum_nums_list())


### More

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"Hi there, {name}")

greet("Tom")
greet(name="Jared") # This will fail because it is a kwarg (key/value)