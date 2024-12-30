# loops


# conditions for entry
# conditions for exit
# iteration - body of the loop


# for loop
# while loop


# # for
# for ind, val in enumerate([1, 2, 3])
#     print(f"{ind} -> {val}")
#

# for val in <iterable>  # set, dict, ... list, tuple
# __iter__


# range - generates sequence of integers (immutable sequence)
# range is "special" - not like lists or generators
# lazy

range(100)  # if one param - "end"

# has start, end, [step]
# starts from 0 by default
# end is not included


# for i in range(10):
#     print("action")
#
# # str is an iterable
# for char in "string":
#     print(char)


# comprehensions (list, dict, set ...)
# one line

lst = []
for i in range(10):
    lst.append(i)
# print(lst)

# syntax [<exp_appended_to_list> for <name> in <iterable> if <condition>]
# "if" is optional
# print([i + 10 for i in range(10) if i + 10 != 11])

# {"key": "value"}
# diff keys, same value; by dict comprehension
d = {k: 1 for k in ["a", "b", "c"]}
print(d)

# same as above, by "fromkeys" method (same values)
d2 = dict.fromkeys(["a", "b", "c"], 1)
print(d2)

# unpacking both keys and values
d3 = {k: v for k, v in [("a", 1), ("b", 1)]}
print(d3)

# s = {i for i in range(10)}
# print(s)

# gen = (i for i in range(10))
# print(gen)

a = ["a", "b", "c"]
b = [1, 2, 3]

# print(list(zip(a, b)))

# module random - pseudo random numbers - float from 0 to 1
# except security, encryption function
# for security - use "secrets" module

# seed - defines the sequence - accepts int / bytes / str


# jupyter notebook / google colab
