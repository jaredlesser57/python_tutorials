from functools import wraps

### Writing to ensure first ARG is a decorator MATCH



def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First argument needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    return foods

print(fav_foods("burrito", "ice cream"))
print(fav_foods("ice cream", "burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12))
print(add_to_ten(1, 2))


### Enforcing argument types with a decorator

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append( t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)
        print(time) # this does NOT have to be here, just to make pylint STFU

repeat_msg("HELLO", 6)
repeat_msg("HELLO", "6") # it knows to make this an INT

repeat_msg("57", 3)
repeat_msg(7, 2)


@enforce(float, float)
def divide_nums(num1, num2):
    print(num1 / num2)

divide_nums('78', '6')
# print(divide_nums("time", "2"))





