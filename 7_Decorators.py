# Functions
# Python functions are first class citizens
# every function is an object
# functions can take other functions as paramaters

# Python has inner functions

def outer():
    def inner():
        return 'This is from inner function'
    print(inner())

def outer():
    def inner():
        return 'This is from inner function'
    return inner

outer()()

# Decorators

# *args - zero or many arguments

def my_decorator(func):
    def wrapper(*args):
        x = 'Before'
        x += func(*args)
        x += 'After'
        return x
    return wrapper

@my_decorator
def greet():
    return 'Hello'


@my_decorator
def msg(name):
    return f'hello {name}'







        

