import builtins
import operator


# functions

# - reuse of code
# - organization of code
# - names as verbs (typically): get_** handle_** etc.
# - separation of concern, SRP (single responsibility principle)


def func(a, b):
    # early exit
    if b == 0:
        return ...

    return a + b


# returns - can be multiple, but only one will execute


# assert 2 + 2 == 5, "Assert message"  # python -o


# # mutable default argument
# def func(param=None):
#     param = param or []  # idiom
#     param.append(1)
#     print(param)


# func([1])
# func()
# func()
# func()
#
# LEGB, variable scope
# LEGB: local, enclosing, global, built-in

import collections

#
#
# CONSTANT = "abc"
#
# a = 1  # global scope (module level)
#
# def func():
#     global a
#     a = 2
#
# print(a)
# func()
# print(a)
#
# def outer():
#     # local scope
#     a = 2
#     def inner():
#         nonlocal a
#         print(f"from inner: {a}")  # a - enclosing
#     return inner
#
# func()
#
#
#
#

# calling functions


# args:
# - positional
# - positional with defaults
# - *args (packing positional args) - optional / variable count - tuple
# - keyword arguments
# - **kwargs - the rest of kw args (var len) - dict


def func(a, b, c, *, d, **kwargs):
    print(f"{a=}")
    print(f"{b=}")
    print(f"{c=}")
    # print(f"{args=}")
    print(f"{d=}")
    print(f"{kwargs=}")


func(2, 3, 4, d=5, kw1=1, kw2=2)


def func2(*args, **kwargs):
    print(args, kwargs)


def any_params(*args, **kwargs):
    """This is func description"""
    print(args)
    print(kwargs)
    func2(1, 2, c=3)


any_params(1, 2, c=3)


def func_with_bool(a, b, /, *, c=False):
    pass



print(type(func_with_bool))


ops = {
    "+": operator.add,
}

f = ops["+"]
print(f)
print(f(2, 2))

print(sum((2, 2, 1)))


def add_all(*args):
    return sum(args)

print(add_all(2, 3, 4))


print(add_all.__name__, add_all.__code__)  # introspection