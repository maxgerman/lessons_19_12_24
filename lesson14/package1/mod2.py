def func():
    from . import mod1
    mod1.func_hello()


class MyClass:
    print("Class definition runs!")  # This runs immediately

    def __init__(self):
        print("Instance created")


def func(a):
    pass