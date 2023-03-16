import time

def time_decorator(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()  
        print(f'execution time was {end - start}') 
        return result
    return wrapper

@time_decorator
def add(*args):
    return sum(args)

print(add(3, 5, 6, 7))

