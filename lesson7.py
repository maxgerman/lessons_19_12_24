# dict methods

d = {"a": 1}

d["b"] = 2

d2 = {"c": 3}
d.update(d2)

print(d)

print(d.get("d", 10))

print(d.setdefault("c", 11))
# print(d["e"])

# for ...
d.setdefault("key", []).append("1")
print(d)

d.setdefault("key", []).append("2")
print(d)

from collections import defaultdict

dd = defaultdict(bool)

print(dd["arbitrary_key"])


print(d.pop("r", None))

# print(d.popitem())
# print(d.popitem())

for k in d.items():
    print(k)

# ===

from collections import namedtuple

Point = namedtuple("Point", "x y")

p = Point(x=1, y=2)

print(p)
print(p.x, p.y)

b, c = p

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


p = Point(x="abc", y=3)
p.y

print(p._asdict())

# ==============


def sum_ints(a, b, c=None):
    res = a * b
    c.append(res)
    return c

# print(sum_ints(2, 3))

s = []
sum_ints(2, 2, s)
print(s)

# Goals of function:

# - reuse of code
# - structure/readability
# - level of abstraction / black box
# - testability
# - clean namespace


# general rule: either change in-place or return val
