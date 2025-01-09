# tuples


# sequence, immutable

a = 1, 2  # literal
a = (1, 2)  # literal

b = tuple([1, 2, 3])
# print(b)
del b

a = 2 + 2


# assert a == 5

# fail early


def show_args(*args):
    print(args)
    for arg in args:
        ...


# show_args("hello")
# show_args(1, "string", True)

# bytes type
s = "abc"  # str, contains symbols, always UTF-8 (Python 3)
a = b"hello"  # bytes, contains bytes
# ASCII - basic encoding (1 byte per symbol)
print(a)

b = s.encode(encoding="utf8")
print(b)
s2 = b.decode(encoding="utf8")
print(s2)

# hashlib

# hash-function: receives data and produces fixed-length value (aka digest, hash)
# changes considerable with small changes to input
# hash algor. - open


# dict - the best in set/get value by key
# key - value


# literals
d = {"a": 1}

print(d)

d2 = dict(a=1, b=2)
print(d2)

d3 = dict([("a", 1), ("c", 3)])
print(d3)

d["new_key"] = 10
print(d["a"])
print(d)

# keys in dicts must be hashable: strings, int, float, bytes, tuple (without mutable elements)
# 1. immutable
# 2. support certain methods (__eq__, __hash__)

# values can be any: mutable, other dicts


# hash is tightly tied to value

d = {1: "a", 1.0: "b"}
print(d)

# str, bytes hashes differ between restarts (of python) for security
