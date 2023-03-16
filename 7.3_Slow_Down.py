import time


def slow_down(func):
    def wrapper(*args):
        result = func(*args)
        time.sleep(1)
        return result
    return wrapper


@slow_down
def countdown(n):
     if not n:   # 0 is false, not false is true
         return n
     else:
         print(n, end=' ')
         return countdown(n-1) # call the same function with n as one less


countdown(5)