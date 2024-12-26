

## data types

# int - 10 - practically infinite ("integer")
# float - 3.5 - optimal for calc (not money!)
# complex
# decimal (std lib)

# str

## collections
# list  (multiple types inside) (mutable)
# tuple (кортеж) - immutable (незмінний)
# set (множина) - max one membership (входить макс один раз) (mutable)
# frozenset (collections in std lib)


# dict - словник (hash-map)
# keys must be immutable, hashable
# values - any

# bool - True/False

# None - singleton


# bytes, bytearray


#### str literals ####
# a = 10  # assignment, variable (name), literal
# "abc"  # str literal
# a = "abc"
# b = a
#
# a = "abc \'asdf"
# b = 'string "asdf" '
# big_string = """ contains anything between triple  quotes ' "  "" """
# print(big_string)
#
# a = "str1 \n inner str'"
# print(a)
#
# lists

list_1 = [1, 2, 3, "a", None]  # diff types inside, mutable

# tuples
t1 = (1, 2, 3)
# t1.append(1)

# sets

# s1 = set(1,2,3)


# dicts
# d1 = {"a": 1, "b": 2.5}
# print(d1["a"])

# var naming
# students_count  # snake case
# can't use keywords (def, in ) or builtins
# _something  # valid
# _ (underscore) - valid name, "throwaway" value

# class names
# OurSuperClass

# OUR_CONSTANT = 123  # constant

# PEP - "python enhancement proposition" - good source of info about python firsthand

name = "Oleh"
# text = "Hello, {name}"
# text = "Hello, " + name  # concatenation
# f-strings
num = 10
text = f"Hello, {name}, {num}"
# print(text)

# interning

# a = input("Enter a number: ")  # return type is always a str
#
# b = input("Enter a number: ")  # return type is always a str
# print(int(a) + int(b))


