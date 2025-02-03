# #
# #
# # class Person(object):
# #     # don't mess with __new__
# #     def __new__(cls, *args, **kwargs):
# #         # obj creation
# #         print("instance is created")
# #         return super().__new__(cls)
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     # representation for humans
# #     # def __str__(self):  # called when print(), str(), f-string
# #     #     return f"Person ({self.name}, {self.age})"
# #
# #     def __repr__(self):  # technical representation, ideally can be used for obj recreation
# #         return f"Person(name={self.name}, age={self.age})"
# #
# #
# #
# # p = Person("Vasa", 20)
# # lst = [p]
# #
# # print(p)
# # print(lst)
# import datetime
# from abc import abstractmethod, ABC
# from typing import Self
#
#
# class Car:
#     count = 0
#
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#         # type(self).count += 1
#         self.__class__.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     # from...
#     @classmethod
#     def from_model_of_year_2020(cls, model):
#         return cls(model, 2020)
#
#     def count_age_of_a_car(self):
#         return datetime.datetime.now().year - self.year
#
#     @staticmethod
#     def kmh_to_mph(kmh: int):
#         return kmh * 0.8
#
#     @staticmethod
#     def print_hello():
#         print("hello")
#
#
# print("mph", Car.kmh_to_mph(100))
#
#
# class BMW(Car):
#     def __init__(self, model, year, m_pack: bool):
#         super().__init__(model, year)
#         self.m_pack = m_pack
#
# Car.print_hello()
# car = Car("Audi RS6", 2024)
# car = Car("Audi RS6", 2024)
# car = Car("Audi Q7", 2025)
# b = BMW("M5", 2000, True)
# # car.kmh_to_mph()  # Car.method_name(car, args)
#
# print(Car.count)
# print(BMW.count)
# print(b.m_pack)
# #
#
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         ...
#
#     @abstractmethod
#     def go(self):
#         ...
#
#
# class DefenderMixin:
#     def defend(self):
#         print("defending!")
#
#
# class Dog(Animal, DefenderMixin):
#     def sound(self):
#         print("arrh")
#
#     def go(self):
#         print("running")
#
#
# d = Dog()
# d.sound()
# d.defend()
#
#
#
# # multiple inheritance, and C3 linearization
#
#
# #  A
# # B  C
# #  D
#
# class A:
#     def show(self):
#         print("A")
#
#
# class B(A):
#     def show(self):
#         print("B")
#
#
# class C(A):
#     def show(self):
#         print("C")
#
#
# class D(B, C):
#     pass
#
#
# D().show()
# print(D.__mro__)  # method resolution order
# # C3 linearization
# # DRF - Django Rest Framework
#
#
# # mixin
#
#
#


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __repr__(self):
        # This helps when printing or debugging phone instances
        return f"<Phone brand={self.brand}, model={self.model}, price={self.price}>"

    @classmethod
    def create_used(cls, brand, model):
        """
        A class method (alternate constructor).
        For example, we may define used phones at a certain special price.
        """
        used_price = 25  # Example special price for used
        return cls(brand, model, used_price)


class PhoneShop:
    def __init__(self, name):
        self.name = name
        # Use a dict with Phone objects as keys and int quantities as values
        self.inventory = {}

    def get_name(self):
        return self.name

    @classmethod
    def from_city_name(cls, name, city_name):
        instance = cls(name)
        instance.name = instance.name + f"_{city_name}"
        return instance

    @staticmethod
    def usd_to_eur(usd_amount: int):
        rate = 1.1
        return usd_amount * rate

    def add_phone(self, phone: Phone, quantity=1):
        """
        Add a phone to the inventory, or increase its quantity.
        """
        # phone must be hashable
        if phone in self.inventory:
            self.inventory[phone] += quantity
        else:
            self.inventory[phone] = quantity

        print(f"Added {quantity} x {phone.model} to {self.name}")

    def sell_phone(self, phone, quantity=1):
        """
        Sell (remove) a phone from the inventory.
        If there isn't enough inventory, it won't go negative.
        """
        if phone not in self.inventory:
            print(f"{phone.model} is not in the inventory.")
            return

        if self.inventory[phone] < quantity:
            print(f"Not enough {phone.model} in stock. Selling what's available.")
            quantity = self.inventory[phone]

        self.inventory[phone] -= quantity

        # If quantity hits zero, remove from inventory to keep it clean
        # if self.inventory[phone] == 0:
        #     del self.inventory[phone]

        print(f"Sold {quantity} x {phone.model} from {self.name}")

    def get_inventory(self):
        """
        Pretty print the current inventory with counts and total price.
        """
        total_price = 0
        print(f"\nInventory of {self.name}:")
        print(f"{"Brand":<10} {"model":<20} {"price/pc"} {"count"} {"subtotal"}")
        for phone, quantity in self.inventory.items():
            phone_total = phone.price * quantity
            total_price += phone_total
            print(
                f"{phone.brand:<10} {phone.model:<20} | {phone.price}$ | {quantity} pcs | {phone_total}$"
            )

        print(f"Total inventory value: ${total_price:.>30}\n")
        return total_price


# Create the PhoneShop
shop = PhoneShop("RetroShop")

# Create some phone instances
nokia_3310 = Phone("Nokia", "3310", 500)
nokia_n8 = Phone("Nokia", "N8", 900)
sony_xperia = Phone("Sony", "Xperia", 200)
iphone_original = Phone("Apple", "iPhone_1", 150)
phone = Phone("Samsung", "S500", 200)

# Also use the class method to create a refurbished phone
used_siemens_c35 = Phone.create_used("Siemens", "C35")

# Add them to the shop
shop.add_phone(nokia_3310, 10)
shop.add_phone(nokia_n8, 5)
shop.add_phone(sony_xperia, 3)
shop.add_phone(iphone_original, 2)
shop.add_phone(used_siemens_c35, 1)

# View inventory
shop.get_inventory()

# # Sell some phones
shop.sell_phone(nokia_3310, 2)
shop.sell_phone(sony_xperia, 1)
shop.sell_phone(used_siemens_c35, 1)
shop.sell_phone(used_siemens_c35, 1)
shop.sell_phone(sony_xperia, 150)
#
# # View inventory again
shop.get_inventory()
