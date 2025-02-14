
# polymorphism

# ~obj -- unary operator
# 2 + 2 -- binary operator
#
# print(1 + 1)
# print("1" + "1")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point (x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(x=self.x + other.x, y=self.y + other.y)
        elif isinstance(other, int):
            return Point(x=self.x + other, y = self.y + other)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.x += other
            self.y += other
        return NotImplemented

    def __radd__(self, other): # right add
        return self + other

    def __iadd__(self, other):  # in-place add
        return NotImplemented


p1 = Point(1, 2)
p2 = Point(2, 3)

p1 += 3
print(p1)
# print(p2)
#
# print(p1 + p2)
# # print(p1 + 10)
# print(10 + p1)
# # print(p1+=p2)
#
# lst = [1, 2, 3]
# lst2 = [2, 3]
#
# lst += lst2  # mutable obj is changed
# lst = lst + lst2  # new obj
# lst.extend(lst2)
#
# print(lst)

