# #  • Функція як параметр для іншої функції
# from black.trans import defaultdict
#
#
# def mul(a, b):
#     return a * b
#
#
# def my_sum(a, b):
#     return a + b
#
#
# funcs = [mul, my_sum]
#
# # functions as values - normal
# fd = {1: mul, 2: my_sum}
#
# for i in range(1, 3):
#     f = fd[i]
#     print(f(2, 4))
#
#
# # print(funcs)
# # print(hash(my_sum))
#
# # warning!
# dict_of_funcs = {my_sum: "abc"}
# # print(dict_of_funcs)
#
#
# a = 1
#
# if a == 2:
#
#     def func():
#         return 1
#
# else:
#
#     def func():
#         return 2
#
#
# print(func())
#
#
# #  • Документування функцій
#
#
# def func(a, b):
#     """
#     Return sum of a + b
#
#     Extra text
#     reStructuredText - syntax for docstrings supported
#     :param:
#     :param a: first num
#
#     :return: the sum
#     """
#     pass
#
#
# # print(func.__doc__)
#
#
# #  • Анотування типів у функціях
#
#
# import typing
# # mypy - static type checker
# def func(a: int, b: int | float) -> int | None:
#     return True
#
#
# lst1: list[int] = [1, 2, 3]
#
#
# #
# # Рекурсія
# #  • Що таке Рекурсія?
#
# # func calls itself
#
# def fibo(n):
#     a, b = 0, 1
#
#     for _ in range(n):
#         a, b = b, a + b
#
#     return a
#
#
# # not optimal, O(N) - 2^N
# def fibo_rec(n):
#     # base case
#     if n == 0:
#         return 0
#
#     if n in (1, 2):
#         return 1
#
#     # recursive case
#     return fibo_rec(n - 1) + fibo_rec(n - 2)
#
#
# print(fibo(10))
# print(fibo_rec(20))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #  • Анонімні функції lambda
#
# # function without name (aka anonymous)
#
#
# # lst1.sort(key=lambda: 1)
# lf = lambda a, b: a + b
#
# print(lf(2, 2))
#
# dd = defaultdict(lambda: 0)
# dd['a'] += 1
#
# #  • map, filter, zip
#
#
# functional style functions

lst1 = ["A", "B", "C", "d"]
lst2 = ["a", "b", "c"]


print(list(zip(lst1, lst2)))  # multiple iterables


f = filter(lambda c: not c.isupper(), lst1)

from itertools import filterfalse  # opposite of filter

# lazy (like range, zip, etc itertools (module))
# filters can be combined
print(list(f))
# f2 = filter(func, f)


def mul_x2(a):
    return a * 2

lst = [1, 2, 3]

print(list(map(mul_x2, lst)))






