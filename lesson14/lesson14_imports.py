import numbers
import sys

# modules

# packages, like modules (have __path__)
# __init__

# import statement
# 3d party libs
# find+load(exec), cache
# ModuleNotFoundError
# target namespace (don't shadow)
# absolute, relative (only in package, don't run directly)
# circular (ImportError)
# PEP8 (abs; categorize by cr)

# import process:
# - sys.modules
# - import protocol: finders + loaders, can be extended by hooks
#   (sys.meta_path (builtins, PathFinder), sys.path_hooks)
# - sys.path (cwd, PYTHONPATH, inst-dep) -- env variables

import sys
# print(sys.meta_path)

from package1 import mod1
# import package1

# print(mod1.__name__)
# print(mod1.__doc__)
# print(mod1.__file__)


# print(package1.__path__)
# print("module __name__:", mod1.__name__)
# if __name__ == "__main__"

# package1.mod1.func_hello()
# mod1.func_hello()

# print(sys.meta_path)
# print(sys.path_hooks)


# print(sys.path)  # full, with diff additions
# runtime check if module is imported
import xml
print("xml imported: ", "xml" in sys.modules)


# print([v for v in sys.path if "lesson" in v])  # current file

#
# print("builtin", sys.builtin_module_names)
# print("stdlib", sys.stdlib_module_names)
#
# print("xml" in sys.modules)
# import xml
# print("xml" in sys.modules)
# print(xml.__name__)
# # print(xml.__doc__)
# print(xml.__file__)
#
import collections
print(collections)
print(collections.__name__)
print(collections.__doc__)
print(collections.__file__)
print(collections.__path__)

# import math
# # print(math.__path__)
#
#
# # from importlib import util
# # print(util.find_spec("itertools"))
#
#
#
# # example
# # pip_importer.py
#
# from importlib import util
# import subprocess
# import sys
#
#
# # class PipFinder:
# #     @classmethod
# #     def find_spec(cls, name, path, target=None):
# #         print(f"Module {name!r} not installed.  Attempting to pip install")
# #         cmd = f"{sys.executable} -m pip install {name}"
# #         try:
# #             subprocess.run(cmd.split(), check=True)
# #         except subprocess.CalledProcessError:
# #             return None
# #
# #         return util.find_spec(name)
#
# # sys.meta_path.append(PipFinder)
#
#













# # ========== OOP, operator overloading
#
# # /, *, **, +, -
#
# # __add__     __radd__     __iadd__      Складання чи конкатенація
# # __sub__     __rsub__     __isub__      Віднімання
# # __mul__     __rmul__     __imul__      Множення чи повторення
# # __truediv__ __rtruediv__ __itruediv__  Справжній поділ
# # __floordiv__ __rfloordiv__ __ifloordiv__ Поділ із округленням
# # __mod__     __rmod__     __imod__      Розподіл по модулю
# # __pow__     __rpow__     __ipow__      Зведення на ступінь
#
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         # TODO: isinstance, NotImplemented
#         print("add executed")
#         return Point(x=self.x + other.x, y=self.y + other.y)
#
#     def __radd__(self, other):
#         print("radd executed")
#         return NotImplemented
#         return self + other
#
#     def __repr__(self):
#         return f"Point (x={self.x}, y={self.y})"
#
#
# p1 = Point(1, 2)
# p2 = Point(2, 3)
#
#
# p3 = p1 + p2
# print(p3)
#
# # 10 + p3
#
#
#
# # x == y	x.__eq__(y)	y.__eq__(x)	Рівне
# # x != y	x.__ne__(y)	y.__ne__(x)	Не дорівнює
# # x > y	x.__gt__(y)	y.__lt__(x)	x більше y
# # x < y	x.__lt__(y)	y.__gt__(x)	x менше за y
# # x >= y	x.__ge__(y)	y.__le__(x)	x більше чи дорівнює y
# # x <= y	x.__le__(y)	y.__ge__(x)	x менше або дорівнює y
#
# # gt + eq != ge
#
#
class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)

    def __iadd__(self, other):
        return Box.__add__(self, other)

    def __radd__(self, other):
        return Box.__add__(self, other)

    def __add__(self, other):
        if isinstance(other, Box):
            print("add")
            return Box(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, numbers.Real):
            return Box(self.x + other, self.y + other, self.z + other)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Box(self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def volume(self):
        return self.x * self.y * self.z

    def __eq__(self, other):
        if isinstance(other, Box):
            # дві коробки вважаються рівними у разі рівності об'ємів
            return self.volume() == other.volume()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Box):
            return self.volume() > other.volume()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Box):
            return self.volume() >= other.volume()
        return NotImplemented


    # def __lt__(self, other):
    #     # if isinstance(other, Box):
    #     # return self.volume(self) < self.volume(other)
    #     # return NotImplemented
    #     return not self > other

box_a = Box(1, 2, 4)
box_b = Box(3, 2, 1)
print(box_a == box_b)
print(box_a > box_b)
print(box_a >= box_b)
print(box_a < box_b)
