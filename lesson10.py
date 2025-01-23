 # • Функції генератори yield


# generator function
# can pause (suspend) - and keep state
# lazy

def gen():
    yield "value 1"
    a = yield "value 2"
    return

g = gen()  # generator object

# we can iterate over generator obj
# 1. by loop (for)
# 2. next

# for val in g:
#     print(val)

print(next(g))
print(next(g))
print(next(g))



# =====   closures ======


# LEGB

# closure = func obj + enclosing scope

def multiply_by(n):
    # n is local for multiply_by and is enclosing for inner
    def inner(b):
        return n * b
    return inner


double = multiply_by(2)  # factory
triple = multiply_by(3)

print(double(2))
print(triple(2))


print(double.__closure__)
print(double.__closure__[0].cell_contents)
print(double.__code__.co_freevars)


def mean():  # no args
    sample = []

    def _mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return _mean

mean1 = mean()
print(mean1(10))
print(mean1(15))

mean2 = mean()
print(mean2(5))
print(mean2(6))

from functools import wraps


#  ======

def log(f):
    def wrapper():
        print(f"starting function {f.__name__:.>20}")
        f()
        print(f"finishing function {f.__name__:.>20}")
    return wrapper


def log_with_prefix(prefix: str):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(f"{prefix} -- starting function {f.__name__:.>20}")
            f(*args, **kwargs)
            print(f"{prefix} -- finishing function {f.__name__:.>20}")
        return wrapper
    return decorator


@log_with_prefix("my_prefix")
def func(a, b):  # signature
    print("func1 is running!")


@log_with_prefix("pre2")
def func2():
    print("func2 is running!")


# decorator pattern
# func = log_with_prefix("my_prefix")(func)
# func2 = log(func2)

func()
func2()
print(func.__name__)

# realpython.com

