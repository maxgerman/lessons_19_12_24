# from functools import cached_property
# from typing import Any
#
#
# class Dog:
#     # __slots__ = "name", "colour", "nickname"  # no __dict__ in this instance
#
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#         self.__secret = "secret value"
#
#
#
# dog = Dog("Pes Patron", "white")
#
#
# dog.colour = "white-brown"
# dog.nickname = "Sharik"
#
# print(dog.nickname)
# # print(dog.__secret)
#
#
# # name-mangling
# print(dog._Dog__secret)
#
#
# def bark(self):
#     print(f"{self.name} says bark!")
#
# Dog.bark = bark  # class, not instance
# # print(dog.bark())
#
#
# # most cases
# # print(dog.__dict__)  # dict of attributes of instance
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
# # setattr(Dog, "bark", bark)
# # print(getattr(dog, "name"))
# # delattr(dog, "nickname")  # del dog.nickname
#
# # print(dog.name)
# # print(dog.colour)
# # print(dog.bark())
#
#
# dog.colour = "brown"
# setattr(dog, "colour", "brown")
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
#
#
#
#
#
#
#
# ### diff between _attr and __attr, name mangling
#
# class Database:
#     def __init__(self):
#         self.__connection = "MySQL"
#         self._config = "Default config"
#
#     def get_connection(self):
#         return self.__connection
#
#
# class SpecialDatabase(Database):
#     def __init__(self):
#         super().__init__()
#         self.__connection = "PostgreSQL"  # This is actually a different variable!
#         self._config = "Special config"  # This overwrites the parent's _config
#
#
# db = SpecialDatabase()
# print(db._config)                        # Special config
# print(db.get_connection())               # MySQL (parent's __connection)
# print(db._SpecialDatabase__connection)   # PostgreSQL (child's __connection)
#
#
# # getattr
# # setattr
#
# # for k, v some_dict.items():
# #     if v is not None:
# #         setattr(other_obj, k, v)
#
#
#
#
#
#
from typing import Any


# __getattribute__, ...

class Phone:
    # __slots__ = ("brand", "model", "price")
    class_atr: str = "I live in class"

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __repr__(self):
        # This helps when printing or debugging phone instances
        return f"Phone(brand={self.brand}, model={self.model}, price={self.price})"


    def __getattribute__(self, item: str) -> Any:
        raise AttributeError
        # print(f"__getattribute__ for {item}")
        # # return getattr(self, "item")
        # # avoid recursion by using super or object!
        # # return object.__getattribute__(self, item)  # method 1
        # # return super(Phone, self).__getattribute__(item)
        # return super().__getattribute__(item)  # method 2

    def __getattr__(self, item):
        # not in object
        print(f"o-oh, no such name: '{item}'")
        return None

    def __setattr__(self, key, value) -> None:
        # called in __init__ too
        print(f"setting '{key}' -> '{value}'")
        # assign to an instance attribute by calling the base class method:
        super().__setattr__(key, value)
        # object().__setattr__(self, key, value)

        # setattr(self, "key", value)
        # self.key = value
        # can write to a dict (already set attr)
        # works but __getattribute__ is called each time
        # self.__dict__[key] = value  # __slots__ = ("name", "surname")

    def __delattr__(self, item) -> None:
        print(f"deleting attr {item} from {self}")
        super().__delattr__(item)


# phone = Phone("Nokia", "3310", 100)

# # print(phone)
# print(phone.model)
# phone.price = 120
# print(phone.__dict__)
# print(phone.class_atr)
#
# print(phone.missing)
# del phone.price
# print("price: ", getattr(phone, "price"))



# try to predict


class Tricky:
    def __init__(self):
        self.existing = "I exist"

    def __getattr__(self, name):
        return f"Created on the fly: {name}"

    def __getattribute__(self, name):
        raise AttributeError
        # raise AttributeError if not found
        if name.startswith('_'):
            return object.__getattribute__(self, name)
        return f"Intercepted: {name}"


t = Tricky()
#
# print(t.existing)
# print(t.nonexisting)

### properties, descriptors


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._age = None

    # @property
    # def full_name(self):
    #     ...
    #

    @property
    def full_name(self):
        # print("getting full name")
        return f"{self.first_name} {self.last_name}"

    # params: getter, setter, deleter
    # full_name = property(get_full_name, doc="full name property")

    @property
    def age(self):
        if self._age is not None:
            return self._age
        return 20

    @age.setter
    def age(self, value):
        # print("setting age", value)
        if value < 20:
            raise ValueError("too young!")
        self._age = value

    # @age.deleter
    # def ..



p = Person("Vasa", "Petrenko")
# print(p.get_full_name())
print(p.full_name)
# can't delete
# del p.first_name
# del p.full_name

print(p.age)
p.age = 21
print(p.age)
# p.age = 18

# print(p.calc)
# p.calc = 5
# print(p.calc)
# print(p.getter_func())



# example of descriptor


# subexample: the simplest descriptor

# def getter_func(self):
#     return 11
#
# class A:
#     pass
#
# obj = A()
# obj.__get__ = getter_func
# attr = obj


class SimpleDescriptor:
    def __get__(self, instance, owner_cls):
        return "some dynamic value"
    #
    # def __set__(self, instance, value):
    #     # owner_cls = type(instance)
    #     # owner_cls = instance.__class__
    #     self.value = value
    #
    # def __delete__(self, instance):
    #     del self.value
    #

class A:
    # class attribute, one shared instance
    attr1 = SimpleDescriptor()


a = A()
print(a.attr1)




class MultVolume:
    def __init__(self, n):
        self.n = n

    def __get__(self, instance_self, instance_class):
        # print(self)
        # print(instance_self)
        # print(instance_class)
        return self.n * instance_self.volume


class Box:
    volume_x2 = MultVolume(2)  # Створення поля керованого дескриптором
    volume_x3 = MultVolume(3)  # Створення поля керованого дескриптором

    def __init__(self, x, y, z):
        self.volume = x * y * z


box1 = Box(1, 2, 3)

print(box1.volume)
print(box1.volume_x2)
print(box1.volume_x3)


# example: overwritable  descriptor

class OverwritableDescriptor:
    def __init__(self, initial_value=None):
        self._value = initial_value
        # print(f"Created descriptor at {id(self)}")

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        # print(f"Getting value through descriptor for instance {id(instance)}")
        return self._value

    # Notice: No __set__ method!


class Employee:
    # Create a non-data descriptor at the class level
    title = OverwritableDescriptor("Default Title")


# Let's demonstrate the difference
employee = Employee()

# print("Initial value:")
print(employee.title)

# print("Setting through normal attribute assignment:")
employee.title = "Manager"  # This will overwrite the descriptor!

# print("Reading value after setting:")
print(employee.title)  # Gets the value directly from __dict__

# print("Let's look at the instance's __dict__:")
print(employee.__dict__)  # Shows our overwritten value




# descriptor - protected field
class ProtectedField:
    def __init__(self, field):
        self.field = field

    def __get__(self, instance_self, instance_class):
        field = f'_{instance_class.__name__}{self.field}'  # _Cat__name
        return getattr(instance_self, field)

    # def __set__(self, instance_self, value):
    #     # instance_class у метод __set__ не передається, тому отримуємо його з об'єкта
    #     instance_class = instance_self.__class__
    #     field = f'_{instance_class.__name__}{self.field}'
    #     setattr(instance_self, field, value)


    # def __delete__(self, instance_self):
    #     instance_class = instance_self.__class__
    #     field = f'_{instance_class.__name__}{self.field}'
    #     delattr(instance_self, field)


class Cat:
    name = ProtectedField('__name')
    age = ProtectedField('__age')

    def __init__(self, _name, _age):
        self.__name = _name
        self.__age = _age


cat = Cat('Barsik', 3)
print(cat.name)



# descriptor example, positive value

class PositiveValue:

    def __init__(self):
        self.val = None

    def __get__(self, instance_self, instance_class):
        return self.val

    def __set__(self, instance_self, value):
        if value < 0:
            raise ValueError('Value must be greater than zero')
        self.val = value


class Box:
    x = PositiveValue()
    y = PositiveValue()
    z = PositiveValue()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# box = Box(1, 2, 3)
# print(box.x)
# box.x = -1  # ValueError




# sharing one descriptor instance

class CountingDescriptor:
    def __init__(self):
        self.access_count = 0
        print(f"Creating descriptor at {id(self)}")

    def __get__(self, instance, owner_class):
        self.access_count += 1
        print(f"Accessed descriptor {id(self)} {self.access_count} times")
        return 42


class Example:
    # This is a class variable - one descriptor instance shared by all
    shared_value = CountingDescriptor()


# Let's create multiple instances
obj1 = Example()
obj2 = Example()
obj3 = Example()

# Watch how they all share the same descriptor
print(obj1.shared_value)
print(obj2.shared_value)
print(obj3.shared_value)


# how this sharing is used
class SimpleCachedProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner_class):
        # access via class, not instance
        if instance is None:
            return self

        # We store the computed value in the instance's __dict__
        # This way, each instance has its own cached value
        if self.name not in instance.__dict__:
            instance.__dict__[self.name] = self.func(instance)
        return instance.__dict__[self.name]


class DataProcessor:
    def __init__(self, data):
        self.data = data

    @SimpleCachedProperty
    def processed(self):
        print(f"Processing data for {id(self)}")
        return [x * 2 for x in self.data]


# Each instance caches its own result
dp1 = DataProcessor([1, 2, 3])
dp2 = DataProcessor([4, 5, 6])

print(dp1.processed)  # Computes and caches
print(dp1.processed)  # Uses cache
print(dp2.processed)  # Computes and caches for dp2
print(dp2.processed)  # Uses dp2's cache


