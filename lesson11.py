from abc import abstractmethod


# algorithms

# CS50 Harvard
# complexity - O(N)


# bubble sort
def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Initialize swapped to track if any swaps occur
        swapped = False

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                # Mark that a swap has occurred
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break


# # Sample list to be sorted
# arr = [39, 12, 18, 85, 72, 10, 2, 18]
# print("Unsorted list is:")
# print(arr)
#
# bubble_sort(arr)
#
# print("Sorted list is:")
# print(arr)
#

# binary tree, (b-tree, more nodes)
# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# O(N)

# nested loop


# O(N2)
# for i in ...
#     for j in ...


# space complexity - same O(N) notation



## files

# text files - text and encodings
# binary files - bits and bytes, random data

# modes: r (read), w (write), a (append)
# file = open('my_file.txt', 'a')
# file.write("\nhello world again")
# file.close()



# file = open('my_file.txt', 'rt')
# text = file.read()
# ...
# file.close()
# print(text)

# file - file-like object / buffer / stream
with open('my_file.txt', 'rt') as file:
    print(file.read())  # exeptions
    # context manager block (indented)
    file.seek(0)
    print("read again: ", file.read())
print("context manager closed -- file closed")

from io import StringIO




# one more example of context manager - for db
# with session() as db:
#     db.query(stmt)

# db connection closed

# ====================


# OOP - object-oriented programming - paradigm

# entities:
# - classes - blueprint - e.g. Car
# -- instantiation / creation of obj
# - instance (aka екземпляр, object) (e.g. Corolla, 1994, green)

# - fields (data of the object) -- described in class; concrete values in instances
# - methods

class Car:
    # constructor
    # def __new__(cls, *args, **kwargs):
    #     ...

    # initializer
    def __init__(self, model: str, year: int):  # dunder = double underscore / magic methods
        self.model = model
        self.year = year
        # returns None

    def beep(self, n: int):
        for _ in range(n):
            print(f"{self.model} beeps!")

    def _gas_pump_start(self):
        pass

    def __super_internal(self):
        pass

    def drive(self):
        self._gas_pump_start()
        pass


car = Car("Corolla", 1994)
car2 = Car("Accord", 2000)
print(car)
print(car.model)
print(car.year)
print(car2.model)
print(car.beep(3))
print(car2.beep(1))
# car.__super_internal()


class Animal:  # parent class, base class, superclass, батьківський клас
    def speak(self):
        print("woof-woof")

    def identify(self):
        print("I'm animal")

    def digest_food(self):
        # complex
        pass



class AbstractAnimal:  # parent class, base class, superclass, батьківський клас
    @abstractmethod
    def speak(self):
        pass

class ConcreteAnimal1(AbstractAnimal):
    def speak(self):



class Dog(Animal):  # subclass, child class, підклас
    def speak(self):
        super().speak()
        print("bark!")

dog = Dog()
dog.speak()
dog.identify()
car._gas_pump_start()

for animal in [cat1, dog2, ...]:
    animal.speak()  # polymorphism

# OOP principles:

# 1. inheritance
# 2. polymorphism
# 3. encapsulation - "black box", implementation details - "private" attributes
# 4. (abstraction)


# patterns


# float + float = float
# int + int = int
#
# square1 + square2 = square3
# "a" + "b"

def counter(func):
    c = 0
    def wrapper(*args, **kwargs):
        nonlocal c
        c += 1
        func(*args, **kwargs)
        return c
    return wrapper

@counter
def example_function():
    print("Inside the function")
