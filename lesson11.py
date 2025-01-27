import functools
import inspect
import time
from collections import defaultdict


count = defaultdict(int)  # dict with count by func name, k = func name, v = count


def count_calls(func):
    def wrapper(*args, **kwargs):
        count[func.__name__] += 1
        return func(*args, **kwargs)

    return wrapper


def remember_params(save_to: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            save_to.append([args, kwargs])
            return func(*args, **kwargs)

        return wrapper

    return decorator


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()  # big float
        res = func(*args, **kwargs)
        if len(inspect.stack()) <= 3:
            print(f"func {func.__name__} ran for {time.time() - start:.5f} sec")
        return res

    return wrapper


param_list_1 = []  # recipient


@remember_params(save_to=param_list_1)
@count_calls
def api_call(a: str):
    # this is paid, fixed price
    # similar func are in the proj
    return {"key": f"paid value for {a}"}


# @remember_params(save_to=param_list_1)
# @count_calls


@timer
def api_call_2(a: str, b: int):
    return {"key": f"paid value for {a} and {b}"}


# print(api_call("abc"))
# print(api_call("dfe"))
# print(api_call_2("one", b=2))
#
#
# print(dict(count))
# print(param_list_1)


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("cache hit!")
            return cache[args]

        res = func(*args)
        print("running function without cache")
        cache[args] = res
        return res

    return wrapper


# Redis


# @functools.lru_cache  # LRU - least recently used
@timer
@memoize
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


# print(fibo(15))  # func fibo ran for 3.55941 sec

# print(fibo(50))


########


def print_table(n):
    width = 5
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i*j:{width}d}", end=" ")
        print()  # new row


# print_table(15)

# generators
database = range(1_000_000000000000)  # limit, offset


def get_next_page(page_number: int = 1):
    page_size = 10  # limit
    while True:
        yield list(
            database[page_size * page_number - page_size: page_size * page_number]
        )  # simulation of db query
        page_number += 1


gen = get_next_page()
print(next(gen))
print(next(gen))

print(next(gen))
print(next(gen))


for _ in range(10):
    print(next(gen))

# for element in gen:
#     print(element)


def fibonacci_gen():
    a, b = 0, 1
    while True:
        val = yield a
        a, b = b, a + b


fibo_gen = fibonacci_gen()
for el in range(10):
    print(next(fibo_gen))
    fibo_gen.send(123)

# async / await
# threads, race condition

# asyncio
