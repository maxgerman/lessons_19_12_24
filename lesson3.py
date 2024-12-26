
# comparison
a = 1  # assignment
a == 5  # comparison


# bool,

# if (expression)
a = b = None
a = 1
# if a == 1 or b == 2 and ... ():  # several conditions with `and` / `or`
#     print("condition True")
# if not None:
#     print("cond 2")

# "truthy", "falsy"
# falsy values: False, 0, None, empty containers (including str), empty str  # remember!
# all other - True
# and, or
# "short-circuiting" - evaluate until result is clear/known

# n = 11
# print(n % 2 and "odd" or "even")


# if-else-elif
# n = 1
# if n == 0:
#     print("condition 0")
# elif n == 1:
#     print("cond 1")
# # elif ...  # multiple elif cases
# else:
#     print("else")

# pattern matching
n = 1
match n:  # special syntax
    case 0:
        print("cond 0")
    case 1 if True:  # optional condition
        print("cond 1")
    case _:  # only once (or zero)  # "catch-all"
        print("other")

# ternary operator, conditional assignment
# var1 = <exp> if <cond> else <exp2>


# list
# # mutable
# # diff types
# # ordered, indexed

# # list slices
# e = a[-8:-1:2]  # 3 params: start, stop, [step=1]
# step can be negative

# list method "reverse" (note absent "d") - in-place operation (returns None)


# extend(<iterable>)

# builtin "sorted" function - returns iterator
# list method "sort" - in-place
