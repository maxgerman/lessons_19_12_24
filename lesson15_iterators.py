# how to make an obj iterable
# what is iterable, iterator
from typing import Iterator

# iterable - obj we can iterate over (take elements one by one)
# iterator - obj which know how to get elements from ^^ iterable it belongs to

lst = [1, 2, 3]

lst_iterator = iter(lst)

# for element in lst_iterator:
#     print(element)
#
#
# for element in lst_iterator:  # same old iterator
#     print(element)


# "Iteration protocol"
# iteration (including under-the-hood iteration: list(obj), tuple(obj) etc)

# iter(obj) -> iterator (new): __iter__ -> iterator obj

# next(iterator) repeatedly -> gets next element until StopIteration exception
# StopIteration is handled silently - end of iterable

# __next__ -> element until raising StopIteration


# "duck-typing"












class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"


# class BasketIterator:
#     """ Клас ітератор, який знає як обробляти наповнення Кошика,
#     щоб віддавати по одному елементу при кожному запиті
#     """
#
#     def __init__(self, goods_list):
#         """При ініціалізації отримує список товарів
#         і встановлює значення індексу 0"""
#         self.goods_list = goods_list
#         self.index = 0
#
#     def __next__(self):
#         """ Якщо значення індексу не виходить за межі розміру
#         списку, надаємо елемент Кошика.
#         В іншому випадку - викликаємо виняток"""
#         if self.index < len(self.goods_list):
#             res = self.goods_list[self.index]
#             self.index = self.index + 1
#             return res
#         else:
#             raise StopIteration
#
#     def __iter__(self):
#         return self


class Basket:
    def __init__(self, user):
        self.user = user
        self.goods_list = list()

    def add_good(self, good):
        self.goods_list.append(good)

    def __str__(self):
        result = f"User: {self.user}\n"
        for good in self.goods_list:
            result += str(good) + "\n"
        return result

    def __iter__(self) -> Iterator:
        """Повертаємо екземпляр класу Ітератора"""
        return iter(self.goods_list)  # list_iterator
        # return BasketIterator(self.goods_list)



basket = Basket("Vasa")

a = Product("Apple", 35)
b = Product("Milk", 50)

basket.add_good(a)
basket.add_good(b)

for prod in basket:
    # print(prod)
    pass

# print('**' * 6)
# c = Product("Oil", 100)
# basket.add_good(c)



class MyIterator():
    def __next__(self):
        if self.i < 5:
            self.i += 1
            return (f'This is the next element ({self.i})')
        else:
            raise StopIteration

    # to make object iterable, we define the __iter__ method
    def __iter__(self):
        return self

    def __init__(self):
        self.i = 0


mi = MyIterator()
# print(MyIterator.mro())

for el in mi:
    print(el)
    pass




# iteration backup/fallback way: Sequence protocol is used
# get element by index, starting from 0 until IndexError

#
# for element in obj:
#     print(element)
#














class MyMap:
    def __getitem__(self, item):  # item is int or slice
        """Python will call this with index starting from 0 until IndexError"""
        if item <= 5:
            return item * 2
        raise IndexError

    # works without it
    # def __keys__(self, item):
    #     return [1, 2, 3]



mm = MyMap()
# print(mm[0:4])
print(mm[1])


for value in mm:
    print(value)














class DictIteratingOverValues(dict):
    def __iter__(self):
        return iter(self.values())


mi = MyIterator()
# print(MyIterator.mro())

for el in mi:
    # print(el)
    pass


for el in MyMap():
    # print(el)
    pass

original_dict = {"a": "val_a", "b": "val_b"}
# dict constructor accepts another mapping (as one of options)
test_dict = dict(original_dict)
print(test_dict)
dv = DictIteratingOverValues((("key_1", "value_1"), ("key_2", "value_2")))

for v in dv:
    print(v)
    pass


class UserSequence:
    """Реалізація послідовності квадратів чисел
    """
    def __init__(self, number):
        self.number = number

    def __getitem__(self, index):
        if index < self.number:
            return index ** 2 # поверне квадрат значення index
        else:
            raise IndexError

    # def __len__(self):
    #     return self.number

seq = UserSequence(10)
# Отримуємо елементи послідовності у циклі
for element in seq:
    print(element, end=', ') # виведе 0, 1, 4, 9, 16, 25, 36, 49, 64, 81,
    pass

# Можемо отримати елемент послідовності за індексом
# print(seq[9]) # виведе 81

# Можемо отримати всі елементи послідовності у вигляді списку
print()
seq_list = tuple(seq)  # виведе [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("seq list", seq_list)


d = {"a": 1, "b": 2}

key = next(iter(d))

print(key)

lst = list(d.values())
print(lst)
